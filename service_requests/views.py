from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ServiceRequestForm

# This is the homepage or landing page
def index(request):
    return HttpResponse("Welcome to the Gas Utility Service!")

# This handles the service request form submission
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)  # Handles form submission with file uploads
        if form.is_valid():
            service_request = form.save(commit=False)
            # Check if the user is authenticated
            if request.user.is_authenticated:
                service_request.customer = request.user.customer  # Associate with the logged-in customer
            else:
                # Handle the case where user is not authenticated
                return redirect('login')  # Redirect to login or an error page

            service_request.save()
            return redirect('request_success')  # Redirect to a success page after submission
    else:
        form = ServiceRequestForm()

    return render(request, 'service_requests/submit_request.html', {'form': form})  # Ensure correct path to template

def request_success(request):
    return render(request, 'service_requests/request_success.html')  # Ensure correct path to template
