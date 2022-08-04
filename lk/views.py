from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'lk/index.html')


def user_personal_page(request):
    return render(request, 'lk/user_page.html')