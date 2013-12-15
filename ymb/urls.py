from django.conf.urls import patterns, url

from ymb import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^sign_up$', views.sign_up, name='sign_up'),
    url(r'^proc_sign_up$', views.proc_sign_up, name='proc_sign_up'),
)
