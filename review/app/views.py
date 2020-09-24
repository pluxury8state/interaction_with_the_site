from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        comment = ReviewForm(request.POST)
        if request.session.get(product.name, True):
            if comment.is_valid():
                Review.objects.create(**comment.cleaned_data, product=product)
                request.session[product.name] = False
                return redirect('product_detail', pk=pk)

    template = 'app/product_detail.html'

    form = ReviewForm()

    comments = Review.objects.filter(product=product)

    allow_comment = request.session.get(product.name, True)


    context = {
        'form': form,
        'product': product,
        'reviews': comments,
        'allow_comment': allow_comment
    }

    return render(request, template, context)
