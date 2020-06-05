from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from groups.models import Group, GroupMember
from posts.models import Post

User = get_user_model()
# Create your views here.

class PostList(SelectRelatedMixin,ListView):
    model = Post
    select_related = ('user','group')
    template_name='posts/post_list.html'
    def get_queryset(self): 
        try:      
            self.user_groups = GroupMember.objects.prefetch_related('group','user').filter(user__username__iexact=self.kwargs.get('username')).distinct()
            self.other_groups = GroupMember.objects.prefetch_related('group','user').exclude(user__username__iexact=self.kwargs.get('username')).distinct()

            gnames=[]
            self.my_groups=[]
            for g in self.user_groups:
                if(g.group.name not in gnames):
                    gnames.append(g.group.name)
                    self.my_groups.append(g)
            
            onames=[]
            self.o_groups=[]
            for g in self.other_groups:
                if(g.group.name not in onames):
                    onames.append(g.group.name)
                    self. o_groups.append(g)
        except:
            raise Http404
        else:
            return self.user_groups.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_groups"] = self.my_groups
        context["other_groups"] = self.o_groups

        return context  

class UserPosts(ListView):
    model = Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context
    
class PostDetail(SelectRelatedMixin, DetailView):
    model = Post
    select_related = ('user', 'group')


    def get_queryset(self,**kwargs):
        return super().get_queryset().filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    fields = ('message','group')
    model = Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user.id)

    def delete(self,*args, **kwargs):
        messages.success(self.request, "Post Deleted Successfully")
        return super().delete(*args, **kwargs)
    
    


    

    
    
