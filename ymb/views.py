from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from ymb.models import Customer

def index(request):
    return render(request, 'ymb/index.html')

@csrf_exempt
def sign_in(request):
    from ymb.models import Customer
    print request.POST['email']
    print request.POST['password']
    from ymb.models import Customer
    try:
        Customer.objects.get(Q(email__exact=request.POST['email']) & Q(pwd__exact=request.POST['password']))
    except Customer.DoesNotExist:
        return HttpResponseRedirect("/sign_in_fail")
    else:
        return HttpResponseRedirect("/order")

def sign_up(request):
    return render(request, 'ymb/sign_up.html')

@csrf_exempt
def proc_sign_up(request):
    from ymb.models import Customer
    print request.POST['name']
    print request.POST['password']
    print request.POST['email']
    print request.POST['phone']
    print request.POST['address']
    c = Customer(name = request.POST['name'], pwd = request.POST['password'], email = request.POST['email'], phone = request.POST['phone'], address = request.POST['address'])
    print "c"
    c.save()
    return HttpResponseRedirect("/sign_up_result")

def sign_up_result(request):
    latest_customer_list = Customer.objects.order_by('-id')[:5]
    context = {'latest_customer_list': latest_customer_list}
    return render(request, 'ymb//sign_up_result.html', context)

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

def order(request):
    return render(request, 'ymb/order.html')

def sign_in_fail(request):
    return render(request, 'ymb/sign_in_fail.html')
