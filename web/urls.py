from django.urls import path
from . import views
'''You can as well modify the views her to ensure it corresponds to the changes ou might have made in the views.py file'''
urlpatterns = [
    #change this view with the main index rather page view
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('stories/', views.stories),
    path('products/', views.products),
    
]
