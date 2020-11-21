from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def home(request):
    shop = Shop.objects.all()
    return render(request,'home.html',context={'shop':shop})
@login_required(login_url='/login')
def detail(request,post_id):
    shops = Shop.objects.all()
    shopy = get_object_or_404(Shop,pk=post_id)
    bond = shopy.posts.all()
    totaldis = 0
    totald = 0
    totalp = 0
    for x in bond:
        totaldis += x.discount
    for xx in bond:
        totald += xx.residual
    for xxx in bond:
        totalp += xxx.paid_amount




    context = {'shop': shopy,
                'shops': shops,
                'bond': bond,
               'totaldis':totaldis,
               'totald': totald,
               'totalp': totalp,
               }
    return render(request,'detail.html',context)



