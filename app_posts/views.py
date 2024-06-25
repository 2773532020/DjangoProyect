from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import CreateView

def index(request):
    posts = Post.objects.all()  # Cambié 'post' a 'posts' para que el nombre sea más representativo
    return render(request, 'index.html', {'posts': posts})

# imágenes
class CommentCreateView(CreateView):
    form_class = CommentForm
    model = Comment

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'post_id': self.kwargs['post_id']})

# detalles del post
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.save()
            return redirect('post_detail', post_id=post_id)
        else:
            errors = form.errors
    else:
        form = CommentForm()
        errors = None

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form, 'errors': errors})

