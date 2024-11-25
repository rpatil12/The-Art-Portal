from django.urls import path
from tap_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('ib-portfolios/', views.ib_portfolios, name='ib_portfolios'),
    path('other-portfolios/', views.other_portfolios, name='other_portfolios'),
    path('ib-portfolios/<str:category>/', views.artwork_form, name='artwork_form'),
    path('artwork_form/<str:category>/', views.artwork_form, name='artwork_form'),
]
