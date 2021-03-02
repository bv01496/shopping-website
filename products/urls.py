from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('catagory/<pk>',views.catlist,name='catagory'),
    path('search-query',views.Search.as_view(),name='search'),
    path('order',views.ordercheckout ,name='placeorder'),
    path('add_address',views.add_address ,name='add_address'),
    path('cart',views.add_cart ,name='cart'),
    path('usercart',views.usercart,name='usercart'),
    path('alter-cart-prod',views.alter_cart_prod,name='alter-cart-prod'),
    path('prod_detail/<pk>',views.ProdDetail.as_view(),name='prod-detail'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
