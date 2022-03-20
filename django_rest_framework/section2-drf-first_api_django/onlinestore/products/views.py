from django.http import JsonResponse

from .models import Product, Manufacturer

# Competency Assessment 1 - section 2-10
"""
1. given a primary key, the first endpoint will allow users to retrieve
all the detailsabout the specific manufacturer (products included)
2. The second endpoint will allow users to retrieve a list 
of all the available active manufacturers in our online store
"""
def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = manufacturer.products.all()
        data = {"manufacturer": {
            "name": manufacturer.name,
            "city": manufacturer.location,
            "active": manufacturer.active,
            "products": list(manufacturer_products.values())
        }}
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "manufacturer not found!"
            }
        }, status=404)
    return response


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.filter(active=True)
    data = {"manufacturers": list(manufacturers.values())}
    response = JsonResponse(data)
    return response


# 2. Use JsonResponse
def product_list(request):
    products = Product.objects.all()  # [:30]
    data = {"products": list(products.values())} # "pk", "name"
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "photo": product.image.url,
            "price": product.price,
            "shipping_cost": product.shipping_cost,
            "quantity": product.quantity
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "product not found!"
            }
        }, status=404)
    return response


### 1. pure Django view
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Product, Manufacturer

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"