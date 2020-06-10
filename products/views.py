from django.shortcuts import render,get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm, RowProductForm


def render_initial_data(requst):
    initial_data = {
        'title': "My awesome title"
    }
    obj = Product.objects.get(id=1)
    form = RowProductForm(requst.POST or None)
    context = {
        'form': form
    }
    return render(requst, "product/product_create.html", context)


def dynamic_lookup_view(requst, id):
    #obj = Product.objects.get(id=id)
    #obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }
    return render(requst, "product/product_det.html", context)


def product_list_view(requst):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(requst, "product/product_list.html", context)


def product_delete_view(requst, id):
    obj = get_object_or_404(Product, id=id)
    if requst.method == "POST":
        # conirming delete
        obj.delete()
        return redirect('../')
    context = {
        'object': obj
    }
    return render(requst, "product/product_create.html", context)



# def product_create_view(requst):
#     my_form = RowProductForm()
#     if requst.method == "POST":
#         my_form = RowProductForm(requst.POST)  #instance of a class
#         if my_form.is_valid():
#             #now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(requst, "product/product_create.html", context)

#hereeeeeeeeeeeeeeeeeeee
# def product_create_view(requst):
#     if requst.method == 'POST':
#         my_title = requst.POST.get('title')
#         print(my_title)
#     context = {}
#     return render(requst, "product/product_create.html", context)

# def product_create_view(requst):
#     context = {}
#     return render(requst, "product/product_create.html", context)


#shortcut method for here
def product_create_view(requst):
    form = ProductForm(requst.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(requst, "product/product_create.html", context)


# Create your views here.
def product_detail_view(requst):
    obj = Product.objects.get(id=1)
    # context = {
    #    "title":  obj.title,
    #    "description":  obj.description
    # }
    context = {
        'object': obj
    }
    return render(requst, "product/product_det.html", context)
