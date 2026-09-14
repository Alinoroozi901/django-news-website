from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from . import models, mixins,forms
from django.db.models import Q


class ArticleList(mixins.CustomLoginNeededMixin, ListView):
    model = models.Article
    template_name = "article_list.html"
    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()  # fix spaces
        if query:
            words = query.split()  # split into individual words
            filters = Q()
            for word in words:
                filters &= Q(title__icontains=word) | Q(body__icontains=word)
            return models.Article.objects.filter(filters)
        return models.Article.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class CommentGet(DetailView):
    model = models.Article
    template_name = "article_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.CommentForm
        return context

class CommentPost(FormView,SingleObjectMixin): # new
    model = models.Article
    form_class = forms.CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, ** kwargs):
        self.object = self.get_object()
        return super().post(request, *args, ** kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})
    

class ArticleDetail(mixins.CustomLoginNeededMixin,View):
    def get(self, request, *args, ** kwargs):
        view = CommentGet.as_view()
        return view(request, *args, ** kwargs)

    def post(self, request, *args, ** kwargs):
        view = CommentPost.as_view()
        return view(request, *args, ** kwargs)
class ArticleUpdate(mixins.CustomLoginNeededMixin, mixins.UserPassesTestMixin, UpdateView):
    model = models.Article
    fields = ['title','body']
    template_name = "article_edit.html"
    success_url = reverse_lazy('article_list')
    
    def handle_no_permission(self):
        return redirect('article_list')
    
    def test_func(self):
        article = self.get_object()
        return(self.request.user.is_staff or article.author == self.request.user)
    
class ArticleDelete(mixins.CustomLoginNeededMixin, mixins.UserPassesTestMixin, DeleteView):
    model = models.Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('article_list')
    
    def handle_no_permission(self):
        return redirect('article_list')
    
    def test_func(self):
        article = self.get_object()
        return(self.request.user.is_staff or article.author == self.request.user)
class ArticleCreate(mixins.CustomLoginNeededMixin, CreateView):
    model = models.Article
    template_name = 'article_create.html'
    fields = ('title', 'body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)