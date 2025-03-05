from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contact.html')

def product(request):
    return render(request, 'Products.html')

def service(request):
    return render(request, 'services.html')

def outcome(request):
    return render(request, 'Outcomes.html')

def innovation(request):
    return render(request, 'innovation.html')





def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'karry' and password == '2310':
            # Initialize or clear session data
            request.session['responses'] = {}
            return redirect('raslo')  # Redirect to raslo view
        else:
            context={'message':"The username or password you entered is incorrect."}
            return render(request, 'login.html',context)

    return render(request, 'login.html')
