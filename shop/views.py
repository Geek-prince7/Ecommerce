from django.shortcuts import render
from .models import Products,Order
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    products=Products.objects.all()
    # SEARCH 
    item_name=request.GET.get('item_name')
    if item_name is not None and item_name!='':
        products=products.filter(title__icontains=item_name)
    # PAGINATION
    no_item=request.GET.get('items')
    page=request.GET.get('page')
    if no_item is None or no_item=='':
        no_item=2
    paginator=Paginator(products,no_item)
    product_page=paginator.get_page(page)
    return render(request,'shop/index.html',{'products':product_page})


def detail(request,id):
    product=Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product':product})



def checkout(request):
    if request.method=='POST':
        items=request.POST.get('items')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip=request.POST.get('zip','')
        total=request.POST.get('total',0)
        order=Order(total=total,name=name,address=address,zip=zip,email=email,state=state,city=city,items=items)
        order.save()

    return render(request,'shop/checkout.html',{})