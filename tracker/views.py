from django.shortcuts import render
from .models import Article,Product
from django.utils import timezone
from django.views.generic import DetailView,ListView

class home(ListView):

    model = Article
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ProductListView(ListView):

    model = Product
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['Products'] = Product.objects.filter(articles=self.get_object())
        return context
