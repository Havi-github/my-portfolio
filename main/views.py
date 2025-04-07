from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    return render(request, 'main/contact.html')


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             send_mail(
#                 form.cleaned_data['subject'],
#                 form.cleaned_data['message'],
#                 form.cleaned_data['email'],
#                 ['habetayilekal10@gmail.com'],  # Replace with your email
#             )
#             messages.success(request, 'Message sent!')
#             return redirect('contact')
#     else:
#         form = ContactForm()
#     return render(request, 'main/contact.html', {'form': form})
