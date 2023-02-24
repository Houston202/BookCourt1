from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='news_home'),
    path('create', views.import_data_to_db, name='create')
]