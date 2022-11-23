# Django + Stripe API backend 

### Installation, configure requirements and local launch:
1) git clone https://github.com/imarenf/payment-api.git
2) cd payment-api
3) docker-compose up

### API Usage:
 - GET /buy/{item_id}/ - returns Stripe session id for item with given item_id
 - GET /item/{item_id}/ - returns Simple HTML document with information about item and 'Buy' button.
By click on the button, you will be redirected to Stripe Checkout session

By default, there are 10 example items in the database with ids from 1 to 10. 
There is also admin panel (route /admin/), where you can manipulate with test items and create your own.
Admin username and password are stored at env_files/python/.env as DJANGO_SUPERUSER_USERNAME and DJANGO_SUPERUSER_PASSWORD 