from django.shortcuts import render


'''You can actualy rename the views according to the templates you'll create '''

# Create your views here.
def home(request):
    return render(request, 'home.html')

#about view
def about(request):
    return render(request, 'about.html')

#contact view
def contact(request):
    return render(request, 'contact.html')

#stories view
def stories(request):
    return render(request, 'stories.html')

#products view
def products(request):
    return render(request, 'products.html')


    