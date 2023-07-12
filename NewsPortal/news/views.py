from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import FormPost
from .filters import FilterPost


class PostList(ListView):
    model = Post
    ordering = '-dateCreate'
    template_name = 'news.html'
    context_object_name = 'post'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = FilterPost(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'onepost'


class PostCreate(CreateView):
    form_class = FormPost
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_posts = 'NS'
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = FormPost
    model = Post
    template_name = 'news_create.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_detail')


class ArticleCreate(CreateView):
    form_class = FormPost
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_posts = 'PT'
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    form_class = FormPost
    model = Post
    template_name = 'news_create.html'


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_detail')