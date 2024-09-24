from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import servicelist, serviceform

# Redirect home view to customer portal
def home(request):
    # Redirect to the customer portal's main page
    return redirect('customer')  # Ensure 'customer' matches the name in customer_portal.urls

def customer(request):
    return HttpResponse("This is the customer page.")

def servicerequest(request):
    if request.method == 'POST':
        # Collecting form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        service_request_type = request.POST.get('service')  # Updated to 'service' to match the form
        subject = request.POST.get('subject')  # Ensure subject field is captured
        message = request.POST.get('message')

        # Check if all required fields are present
        if name and email and subject and service_request_type:
            # Save the form data to the serviceform model
            serviceformdata = serviceform(
                name=name, 
                email=email, 
                subject=subject,
                service_request_type=service_request_type, 
                message=message
            )
            serviceformdata.save()
            return HttpResponse("Service request submitted successfully!")
        else:
            return HttpResponse("Missing required fields.")

    # Fetch service list data
    servicelistdata = servicelist.objects.all()
    if servicelistdata.exists():
        first_servicelist = servicelistdata[0]
    else:
        first_servicelist = None
    
    # Send data to the template
    context = {
        'servicelist': first_servicelist
    }

    return render(request, 'customer_portal/Service_Request.html', context)

def trackrequest(request):
    service_requests = serviceform.objects.all()

    if str(request.user) == 'admin':
        return render(request, 'customer_portal/Track_Request.html', {
            'service_requests': service_requests,
            "user": 'admin'
        })
    
    # Filter requests by user email to improve accuracy
    curr_user_service = serviceform.objects.filter(email=request.user.email)

    # Check if the user has any service requests
    if not curr_user_service.exists():
        return render(request, 'customer_portal/Track_Request.html', {
            'service_requests': curr_user_service,
            'message': 'No service requests found for this user.'
        })

    return render(request, 'customer_portal/Track_Request.html', {
        'service_requests': curr_user_service
    })

def chooseoption(request):
    return render(request, 'customer_portal/button.html')

def editservicerequest(request, entry_id):
    # Get the service request by ID
    try:
        service_request = serviceform.objects.get(id=entry_id)
    except serviceform.DoesNotExist:
        return HttpResponse("Service Request not found.")
    
    # If it's a POST request, update the service request
    if request.method == 'POST':
        service_request.name = request.POST.get('name', service_request.name)
        service_request.email = request.POST.get('email', service_request.email)
        service_request.subject = request.POST.get('subject', service_request.subject)
        service_request.service_request_type = request.POST.get('service', service_request.service_request_type)
        service_request.message = request.POST.get('message', service_request.message)
        service_request.save()
        return redirect('TrackRequest')  # Redirect to track request page after updating

    # Render the form with the current data for editing
    return render(request, 'customer_portal/edit_service_request.html', {'service_request': service_request})
