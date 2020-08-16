from django.urls import path
#from .import views

from .views import (
    
    ItemDetailView,
    CheckoutView,
    HomeView,
    products,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    #checkout,
    remove_single_item_from_cart,
    PaymentView,
    #add_coupon,
    AddCouponView,
    RequestRefundView
)

app_name = 'core'
urlpatterns =[
    #path('' , views.Home, name='Home'),
    path('' , HomeView.as_view(), name='HomeView'),
    path('checkout/' ,CheckoutView.as_view() ,name='checkout'),
    path('product/<slug>/' ,ItemDetailView.as_view(),name='product'),
   # path('' ,views.HomeView ,name='Home'),
    path('add-to-cart/<slug>/' ,add_to_cart ,name="add-to-cart"),
    path('remove-from-cart/<slug>/' ,remove_from_cart ,name="remove-from-cart"),
    path('order-summary/' ,OrderSummaryView.as_view() ,name="order-summary"),
    path('add-coupon/' , AddCouponView.as_view(),name="add-coupon"),
  
    path('payment/<payment_option>/' ,PaymentView.as_view() ,name='payment'),
    path('remove-single-item-from-cart/<slug>/' ,remove_single_item_from_cart ,name="remove-single-item-from-cart"),
    path('request-refund/' ,RequestRefundView.as_view() ,name="request-refund")


]