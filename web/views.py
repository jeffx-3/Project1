from django.shortcuts import render


'''You can actualy rename the views according to the templates you'll create '''

# Create your views here.
def index(request):
    return render(request, 'index.html')

#about view
def about(request):
    return render(request, 'about.html')

#contact view
def contact(request):
    return render(request, 'contact.html')

#stories view
def service(request):
    return render(request, 'services.html')

#products view
def team(request):
    return render(request, 'team.html')


    