from django.urls import path
from . import views
urlpatterns = [
    #change this view with the main index rather page view
    path('', views.test),
]
