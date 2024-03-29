from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.shortcuts import HttpResponseRedirect
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm, PostForm, ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages


def page_404(request, exception):
    return render(request, '404.html', status=404)


def page_505(request):
    return render(request, '505.html', status=505)


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def blog(request):
    return render(request, 'blog.html', {})


def home(request):
    return render(request, 'home.html', {})


def home(request):
    recent_posts = Post.objects.filter(status=1).order_by('-created_on')[:6]
    return render(request, 'home.html', {'recent_posts': recent_posts})


def CategoryView(request, category):
    category_post = Post.objects.filter(category=category.replace('-', ' '))
    return render(
        request, 'categories.html', {
            'category': category.title().replace('-', ' '),
            'category_post': category_post
        })


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = [
        'author', 'title', 'slug', 'content', 'excerpt', 'status',
        'featured_image', 'category'
    ]


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post.id)
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = [
        'author', 'title', 'slug', 'content', 'excerpt', 'status',
        'featured_image', 'category'
    ]

    def get_success_url(self):
        # Redirect to the post_detail page for the edited post
        return reverse('post_detail', kwargs={'slug': self.object.slug})


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        post.increment_views()
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Get the next and previous posts
        next_post = queryset.filter(created_on__gt=post.created_on).order_by('created_on').first()
        prev_post = queryset.filter(created_on__lt=post.created_on).order_by('-created_on').first()

        return render(
            request,
            "post_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "next_post": next_post,
                "prev_post": prev_post,
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.info(request, 'Your comment has been added successfully!')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):

    def post(sefl, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def search(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query))
        if not results:
            # No results found
            message = "Sorry, no results were found for your search."
            return render(request, 'search_results.html', {'message': message})
    else:
        results = Post.objects.all()
    return render(request, 'search_results.html', {'results': results})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.user:
        comment.delete()
        messages.warning(request,
                         'Your comment has been deleted successfully!')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseForbidden()