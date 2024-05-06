from django.urls import path
from .views import VendorListCreate, VendorRetrieveUpdateDestroy, PurcahseOrderListCreate, PurchaseOrderRetrieveUpdateDestroy

urlpattern = [
    path('vendor/', VendorListCreate.as_view(), name='vendor-list-create'),
    path('vendor/<int:pk>/', VendorRetrieveUpdateDestroy.as_view(), name='vendor-retrieve-update-destroy'),
    path('purchase_orders/', PurcahseOrderListCreate.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroy.as_view(), name='purchase-order-retrieve-update-destroy'),
]

