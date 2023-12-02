from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from utils.convertor import get_client_ip, group_list
from site_module.models import site_banner
from .models import Product, ProductCategory, Productbrand, ProductVisit, ProductGallery


class ProductListView(ListView):
    template_name = 'production/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        context['banners'] = site_banner.objects.filter(is_active=True,
                                                        position__iexact=site_banner.SiteBannerPositions.product_list)
        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if start_price is not None:
            query = query.filter(price__gte=start_price)

        if end_price is not None:
            query = query.filter(price__lte=end_price)

        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


class ProductDetailView(DetailView):
    template_name = 'production/detail_list.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        the_product = self.object
        request = self.request
        favorite_product_id = request.session.get('product_favorite')  # request.session['product_favorite']

        context['is_favorite'] = favorite_product_id == str(the_product.id)

        context['related_products'] = group_list(
            list(Product.objects.filter(brand_id=the_product.brand_id).exclude(pk=the_product.id)), 3)

        context['banners'] = site_banner.objects.filter(is_active=True,
                                                        position__iexact=site_banner.SiteBannerPositions.product_detail)

        gallery = list(ProductGallery.objects.filter(product_id=the_product.id).all())
        gallery.insert(0, the_product)
        context['product_galleries_group'] = group_list(gallery, 3)

        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id

        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=the_product.id)

        if not has_been_visited:
            new_visit = ProductVisit(ip=user_ip, user_id=user_id, product_id=the_product.id)
            new_visit.save()
        return context


class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = Product.objects.get(pk=product_id)
        request.session["product_favorite"] = product_id
        return redirect(product.get_absolute_url())


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {'categories': product_categories}
    return render(request, 'components/product_categories.html', context)


def product_brands_component(request: HttpRequest):
    product_brands = Productbrand.objects.annotate(brands_count=Count('product')).filter(is_active=True)
    context = {'brands': product_brands}
    return render(request, 'components/product_brands.html', context)
