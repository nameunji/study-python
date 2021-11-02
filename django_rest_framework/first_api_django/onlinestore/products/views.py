from django.http import JsonResponse

from .models import Product, Manufacturer

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
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

# from .models import Product, Manufacturer

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"


# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"