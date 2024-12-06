import requests
from django.shortcuts import render, redirect
from cityapp.models import Contact,Member,Bookings
from cityapp.forms import BookingsForm,ContactForm,FeedbackForm
from cityapp.models import Feedback
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.
def index(request):
    if request.method == 'POST':
        # Filter for members with matching username and password
        members = Member.objects.filter(
            username=request.POST['username'],
            password=request.POST['password']
        )
        # Check if any matching members exist
        if members.exists():
            # Safely retrieve the first matching member
            member = members.first()
            return render(request, 'index.html', {'members': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        mycontact=Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('/contactshow')
    else:
         return render(request,'contact.html')

def contactshow(request):
    allcontacts = Contact.objects.all()
    return render(request,'contactshow.html',{'allcontacts': allcontacts})

def deleteContact(request,id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('/contactshow')

def editContact(request,id):
    editcontact = Contact.objects.get(id=id)
    return render(request, 'editcontact.html',{'contact':editcontact})

def updateContact(request,id):
    updateinfo = Contact.objects.get(id=id)
    form = ContactForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/contactshow')
    else:
        return render (request,'editcontact.html')



def menu(request):
    return render(request,'menu.html')




def book(request):
    if request.method == "POST":
        mybookings  = Bookings(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            time=request.POST['time'],
            people=request.POST['people'],
            message=request.POST['message'],
        )
        mybookings.save()
        return redirect('/show')
    else:
        return render(request,'bookatable.html')

def show(request):
    allbookings = Bookings.objects.all()
    return render(request, 'show.html', {'allbookings': allbookings})

def deleteBookings(request,id):
    book = Bookings.objects.get(id=id)
    book.delete()
    return redirect('/show')

def editBookings(request,id):
    editbook = Bookings.objects.get(id=id)
    return render(request, 'editbooking.html',{'book':editbook})

def updateBookings(request,id):
    updateinfo = Bookings.objects.get(id=id)
    form = BookingsForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render (request,'editbooking.html')


def register(request):
    if request.method == "POST":
       members = Member(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password']
       )
       members.save()
       return redirect('/login')
    else:
        return render (request,'register.html')

def login(request):
    return render(request,'login.html')



def rate_us(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_ratings')
    else:
        form = FeedbackForm()
    return render(request, 'rateus.html', {'form': form})

def show_ratings(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'showratings.html', {'feedbacks': feedbacks})

def specials(request):
    return render(request,'specials.html')

def events(request):
    return render(request,'events.html')

def chefs(request):
    return render(request,'chefs.html')

def testimonials(request):
    return render(request,'testimonials.html')

def gallery(request):
    return render(request,'gallery.html')

def terms(request):
    return render(request, 'terms_of_service.html')



def passwordreset(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']

        # Logic to verify user details and send password reset email
        # For demonstration, we'll assume the details are correct and send an email

        send_mail(
            'Password Reset Request',
            'Click the link below to reset your password:\n\nhttp://example.com/reset-password/',
            'from@example.com',
            [email],
            fail_silently=False,
        )

        messages.success(request,
                         'A password reset link has been sent to your email. Check your email to reset your password.')
        return redirect('login')

    return render(request, 'password_reset_request.html')
