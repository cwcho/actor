from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from ymb.models import Customer

def index(request):
    latest_customer_list = Customer.objects.order_by('-id')[:5]
    context = {'latest_customer_list': latest_customer_list}
    return render(request, 'ymb/index.html', context)


# Create your views here.
