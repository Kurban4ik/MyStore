from django.urls import path
from store.views import *

urlpatterns = [
    path('', main, name='home'),
    path('about/', about, name='about'),
    path('base/', base, name='base'),
    path('shop_signle/<slug:name>/', shop_single, name='shop_single'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
]