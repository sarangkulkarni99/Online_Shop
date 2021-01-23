from django.shortcuts import render, get_object_or_404
from .models import Category, Shop, Product
from django.views import generic
from cart.forms import CartAddProductForm

# Create your views here.

class CategoryList(generic.ListView):
    queryset = Category.objects.order_by('name')
    template_name = 'shop/product/category.html'
    paginate_by = 8


def shop_list(request, category_id):
    category = Category.objects.get(id=category_id)
    shops = category.shop_set.order_by('name')
    context = {'category': category, 'shops': shops}
    return render(request, 'shop/product/shop_list.html', context)

def product_list(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    products = shop.product_set.all()
    cart_product_form = CartAddProductForm()
    context = {'shop': shop, 'products': products, 'cart_product_form': cart_product_form}
    return render(request, 'shop/product/product_list.html', context)