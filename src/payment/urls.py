from django.urls import path
from payment.api import get_item, buy_item, success_resp, cancel_resp

urlpatterns = [
    path('buy/<int:item_id>/', buy_item),
    path('item/<int:item_id>/', get_item),
    path('success/', success_resp),
    path('cancel/', cancel_resp)
]
