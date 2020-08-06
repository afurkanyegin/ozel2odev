from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from Home.models import Setting
from Hotel.models import Hotel, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Hotel.objects.all()[:4]
    category=Category.objects.all()
    featureshotel = Hotel.objects.all().order_by('-id')[:6]
    recommendedhotels = Hotel.objects.all().order_by('?')[:3]
    context = {'setting': setting,
               'category':category,
               'sliderdata': sliderdata,
               'featureshotel': featureshotel,
               'recommendedhotels': recommendedhotels, }

    return render(request, 'index.html', context)


def hotel_detail(request, id, slug):
    mesaj = "hotel", id, "/", slug
    #return HttpResponse(mesaj)
    return render(request,'hotel_detail.html')
