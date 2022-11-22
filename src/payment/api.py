import stripe
import os
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render

from payment.models import Item

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
DOMAIN = 'http://127.0.0.1:8000'


def get_item(request: HttpRequest, item_id: int) -> HttpResponse:
    try:
        item = Item.objects.get(pk=item_id)
    except Exception as ex:
        return HttpResponse(ex)
    item_template_context = {
        'item_id': item.pk,
        'item_name': item.name,
        'item_description': item.description,
        'item_price': item.price,
        'publishable_key': PUBLISHABLE_KEY,
    }
    return render(request,
                  template_name='item.html',
                  content_type='text/html',
                  context=item_template_context)


def buy_item(request: HttpRequest, item_id: int) -> JsonResponse:
    try:
        item = Item.objects.get(pk=item_id)
    except Exception:
        return JsonResponse(
            {'error': 'Item with given id doesn\'t exist'}
        )
    session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount_decimal': item.price * 100,
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=DOMAIN + '/success/',
        cancel_url=DOMAIN + '/cancel/',
    )
    return JsonResponse(
        {'id': session.id}
    )


def success_resp(request: HttpRequest) -> HttpResponse:
    return render(request,
                  template_name='success.html',
                  content_type='text/html')


def cancel_resp(request: HttpRequest) -> HttpResponse:
    return render(request,
                  template_name='cancel.html',
                  content_type='text/html')
