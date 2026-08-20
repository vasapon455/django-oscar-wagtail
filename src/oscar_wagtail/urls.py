from django.urls import path

from oscar_wagtail import views

app_name = 'oscar_wagtail'

urlpatterns = [
    path('product-choose/',
        views.product_choose, name='product_choose'),

    path('product-choose/<int:pk>/',
        views.product_chosen, name='product_chosen'),
]
