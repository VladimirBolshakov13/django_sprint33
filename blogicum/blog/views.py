from django.shortcuts import get_object_or_404, render

from .models import Category, get_queryset


AMOUNT_OF_POSTS = 5


def index(request):
    template = 'blog/index.html'
    post_list = get_queryset()[:AMOUNT_OF_POSTS]
    context = {
        'post_list': post_list
    }
    return render(request, template, context)


def post_detail(request, id):
    temlpate = 'blog/detail.html'
    post = get_object_or_404(
        get_queryset(),
        pk=id
    )
    context = {
        'post': post
    }
    return render(request, temlpate, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_queryset().filter(
        category=category
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
