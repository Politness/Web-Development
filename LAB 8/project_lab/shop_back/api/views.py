from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

def list_products(request):
    products = Product.objects.all()
    products_json = [p.to_json() for p in products]
    return JsonResponse (products_json, safe = False)

def get_product(request, get_id):
    products = Product.objects.all()
    products_json = [p.to_json() for p in products]
    for p in products_json:
            if p['id'] == get_id:
                return JsonResponse(p, safe = False)        
    return JsonResponse("No such product")
    
    
def list_categories(request):
    category = Category.objects.all()
    category_json = [cat.to_json() for cat in category]
    return JsonResponse({category_json})

def get_category(request, get_id):
    category = Category.objects.all()
    category_json = [cat.to_json() for cat in category]
    for cat in category_json:
            if cat['id'] == get_id:
                return JsonResponse(cat, safe = False) 
    return JsonResponse("No such category")

def product_category(request, get_id):
    products = Product.objects.all()
    products_json = [p.to_json() for p in products]
    category = Category.objects.all()
    category_json = [cat.to_json() for cat in category]
    for cat in products_json:
        if get_id == cat['id']:
            get_data = Product.objects.filter(category_id=get_id)
            return JsonResponse(get_data, safe= False)
    get_data = product_json.objects.filter(category['id'] == data.id)
    list = []
    for cat in category_json:
        for p in products_json:
            if cat['id'] == get_id:
                if cat == p['category']:
                    list.append(p)
    if list.empty():
        return JsonResponse("No such product or product category")
    return JsonResponse({list})
    





def index(request):
    return HttpResponse("Site view Api")

def categories(request):
    return HttpResponse("Site Api categories")

def index(request):
    posts = Api.objects.all()
    return render(request, 'api/index.html', {'posts': posts, 'categories': category, 'title': 'Home page', 'name': 'This is home page'})

def cat_item(request):
    return render(request, 'api/cat_item.html', {'categories': category, 'title': 'Catalog page', 'name': 'This is catalog page'})