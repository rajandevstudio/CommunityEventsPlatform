from django.shortcuts import render

def login_page(request):
    return render(request, "frontend/login.html")

def register_page(request):
    return render(request, "frontend/register.html")

def events_page(request):
    return render(request, "frontend/event_list.html")

def event_create_page(request):
    return render(request, "frontend/event_create.html")

def profile_page(request):
    return render(request, "frontend/profile.html")
