from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from article_module.models import Article, ArticleCategory, ArticleComment

class ArticleListView(ListView):
    model = Article
    paginate_by = 4
    template_name = 'article_module/article_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticleListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article: Article = kwargs.get('object')
        context['comments'] = ArticleComment.objects.filter(Article_id=article.id, parent=None).order_by(
            '-create_date').prefetch_related('articlecomment_set')
        context['comments_count'] = ArticleComment.objects.filter(Article_id=article.id).count()
        return context

def article_categories_component(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.prefetch_related('articlecategory_set').filter(is_active=True, parent_id=None)

    context = {
        'main_categories': article_main_categories
    }
    return render(request, 'article_module/component/article_categories_component.html', context)

def add_article_comment(request: HttpRequest):
    if request.user.is_authenticated:
        Article_id = request.GET.get('article_id')
        Article_comment = request.GET.get('article_comment')
        Article_parent = request.GET.get('parent_id')
        print(Article_id, Article_comment, Article_parent)
        New_commen = ArticleComment(Article_id=Article_id, user_id=request.user.id, text=Article_comment,
                                    parent_id=Article_parent)
        New_commen.save()
        context = {
            'comments': ArticleComment.objects.filter(Article_id=Article_id, parent=None).order_by(
                '-create_date').prefetch_related('articlecomment_set'),
            'comment_count': ArticleComment.objects.filter(Article_id=Article_id).count(),
        }

        return HttpResponse(render(request, 'article_module/includes/article_comment_partial.html', context))
    return HttpResponse('response')
