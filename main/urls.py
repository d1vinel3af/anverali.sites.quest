from django.urls import path
from . import views

urlpatterns = [
    path('buyer/', views.buyer_page, name='buyer'),
    path('seller/', views.seller_page, name='seller'),
    path('create_order/', views.CreateOrder.as_view(), name='create_order'),
    path('', views.index, name='index'),
    path('order_detail/<int:pk>', views.order_detail, name='order_detail'),
    path('order_edit/<int:pk>', views.OrderEdit.as_view(), name='order_edit'),
    path('order_action/<int:pk>', views.OrderAction.as_view(), name='order_action'),
    path('search_results/', views.search_results, name='search_results'),
]
