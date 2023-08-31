from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib.auth import get_user_model
from django.urls import reverse
from .forms import AdvertisementForm
from .models import Advertisement

User = get_user_model()

def index(request):
    title = request.GET.get('query')
    if title:
        advertisement = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisement = Advertisement.objects.all()
    context = {'advertisement' : advertisement, 'title' : title}
    return render(request, 'adverts_app/index.html', context)

def topSellers(request):
    users = User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
    context = {'users' : users}
    return render(request, 'adverts_app/top-sellers.html', context)

def advertisementPost(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            if title.startswith('?'):
                form.add_error('title', "Заголовок не может начинаться с символа '?'.")
            else:
                advertisement = Advertisement(**form.cleaned_data)
                advertisement.user = request.user
                advertisement.save()
                return redirect(reverse('main_page'))
    else:
        form = AdvertisementForm()
    context = {'form' : form}
    return render(request, 'adverts_app/advertisement-post.html', context)

def advertisementDetails(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {'advertisement' : advertisement}
    return render(request, 'adverts_app/advertisement.html', context)