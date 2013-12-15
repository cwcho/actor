from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt

from ymb.models import Customer

def index(request):
    latest_customer_list = Customer.objects.order_by('-id')[:5]
    context = {'latest_customer_list': latest_customer_list}
    return render(request, 'ymb/index.html', context)

def sign_up(request):
    latest_customer_list = Customer.objects.order_by('-id')[:5]
    context = {'latest_customer_list': latest_customer_list}
    return render(request, 'ymb/sign_up.html', context)

@csrf_exempt
def proc_sign_up(request):
    print request.POST['name']
    print request.POST['password']
    print request.POST['email']
    print request.POST['address']
    print request.POST['sex']
    return HttpResponseRedirect("/")

def menu(request):
    latest_customer_list = Customer.objects.order_by('-id')[:5]
    context = {'latest_customer_list': latest_customer_list}
    return render(request, 'ymb/menu.html', context)

def check_email(request):
    from ymb.models import Customer
    try:
        Customer.objects.get(email__exact=request.GET['email'])
    except Customer.DoesNotExist:
        return HttpResponse("false")
    else:
        return HttpResponse("true")

def check_address(request):
    from ymb.models import zipcode
    try:
        zipcode.objects.get(dong__exact=request.GET['dong'])
    except zipcode.DoesNotExist:
        return HttpResponse("false")
    except zipcode.MultipleObjectsReturned:
        return HttpResponse("true")
    else:
        return HttpResponse("true")

#def sign_up_result(request):
#    
