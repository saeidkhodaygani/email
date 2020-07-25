from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post,UserProfile,Contacts
import operator
from django.urls import reverse_lazy
from django.contrib.staticfiles.views import serve

from blog.forms import createPost
from django.db.models import Q

@login_required
def home(request):
    current_user = request.user.username
    
    context = {
        'posts': Post.objects.filter(manager=current_user.username)
    }
    return render(request, 'blog/home.html', context)

@login_required
def search(request):
    template='blog/home.html'

    query=request.GET.get('q')

    result=Post.objects.filter(Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query))
    paginate_by=2
    context={ 'posts':result }
    return render(request,template,context)
   

@login_required
def getfile(request):
   return serve(request, 'File')


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        #user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(manager__user__username=self.request.user.username).order_by('-date_posted')



class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    # model = Post
    # template_name = 'blog/post_form.html'
    # fields = ['title', 'content', 'file','manager']

    form_class = createPost
    template_name = 'blog/post_form.html'
    def get_form_kwargs(self):
        kwargs = super(PostCreateView,self).get_form_kwargs()
        kwargs['userss'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        #form.instance.manager = UserProfile.objects.filter(user__username=self.request.user.username).values_list('contact', flat=True)
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'file','manager']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
