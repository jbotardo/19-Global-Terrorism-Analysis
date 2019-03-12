from django.urls import path, include
from . import views


app_name = 'front_end'
urlpatterns = [
    path(r'^$', 'views.index', name='home'),
    path(r'^more/', 'views.additional', name='More Views')
]