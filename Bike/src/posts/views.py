from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import UpdateView, DeleteView
from django.template.defaultfilters import slugify

from bike.models import Type
from posts.models import Post
from posts.forms import PostForm
from django.urls import reverse_lazy


def homepostview(request):
    posts = Post.objects.all()
    types = Type.objects.all()
    class Meta:
        ordering = ['-post_date']

    return render(request, 'core/post/posts.html', {'posts': posts, 'types': types})


@staff_member_required
def adminpostview(request):
    posts = Post.objects.all()

    class Meta:
        ordering = ['-post_date']

    return render(request, 'core/post/posts_admin.html', {'posts': posts})


def postdetailview(request, slug):
    post = get_object_or_404(Post, slug=slug)
    types = Type.objects.all()
    return render(request, 'core/post/postdetail.html', {'post': post, 'types': types})


class CreatePost(PermissionRequiredMixin, View):
    permission_required = 'login.login'

    @staff_member_required
    def get(self, request):
        form = PostForm()
        return render(request, 'core/post/add_post.html', {'form': form})

    @staff_member_required
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                title=form.cleaned_data['title'],
                slug=slugify(form.cleaned_data['title']),
                content=form.cleaned_data['content'],
            )
            post.save()
        posts = Post.objects.all()
        return render(request, 'core/post/posts_admin.html', {'posts': posts})


class EditPost(PermissionRequiredMixin, UpdateView):
    permission_required = 'login.login'
    model = Post
    form_class = PostForm
    template_name = 'core/post/edit_post.html'


class DeletePost(PermissionRequiredMixin, DeleteView):
    permission_required = 'login.login'
    model = Post
    template_name = 'core/post/delete_post.html'
    success_url = reverse_lazy('post_admin')
