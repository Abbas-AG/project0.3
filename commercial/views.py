from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import SpecialOffer, Room, Style, CoffeeBreak, Reservation

# Create your views here.

def index(request):
    return render(request, 'index.html')

def specialoffer(request):
    special_offers = SpecialOffer.objects.all()
    return render(request, 'specialoffer.html', {
        'special_offers': special_offers
    })

def room(request):
    rooms = Room.objects.all()
    return render(request, 'room.html', {
        'rooms': rooms
    })

def style(request):
    styles = Style.objects.all()
    return render(request, 'style.html', {
        'styles': styles
    })

def coffeebreak(request):
    coffeebreaks = CoffeeBreak.objects.all()
    return render(request, 'coffeebreak.html', {
        'coffeebreaks': coffeebreaks
    })

def home(request):
    rooms = Room.objects.all()
    styles = Style.objects.all()
    return render(request, 'home.html', {
        'rooms': rooms,
        'styles': styles
    })


def coffee(request):
    special_offers = SpecialOffer.objects.all()
    return render(request, 'coffee.html', {
        'special_offers': special_offers
    })

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render
from .models import Room, Style, CoffeeBreak, Reservation
from django.core.mail import send_mail

def reservation(request):
    rooms = Room.objects.all()
    styles = Style.objects.all()
    coffee_offers = CoffeeBreak.objects.all()

    if request.method == 'POST':
        # Get form data from POST request
        event_space_1_id = request.POST.get('event_space_1')  
        event_space_2_id = request.POST.get('event_space_2')  
        date_and_time = request.POST.get('date_and_time')
        number_of_attendees = request.POST.get('number_of_attendees')
        firstName = request.POST.get('first_name')  
        lastName = request.POST.get('last_name')  
        notes = request.POST.get('notes')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phone_number')  

        # Create a new reservation instance and save it
        reservation_instance = Reservation(
            event_space_1=event_space_1_id,
            event_space_2=event_space_2_id,
            date_and_time=date_and_time,
            number_of_attendees=number_of_attendees,
            first_name=firstName,
            last_name=lastName,
            notes=notes,
            email=email,
            phone_number=phoneNumber,
        )
        reservation_instance.save()

        # Placeholder: Send confirmation email
        send_reservation_email(email, "Your reservation details...")

    context = {
        'rooms': rooms,
        'styles': styles,
        'coffee_offers': coffee_offers,
    }
    
    return render(request, 'reservation.html', context)

def send_reservation_email(user_email, reservation_data):
    subject = 'Reservation Confirmation'
    message = f'Thank you for your reservation. Here are the details:\n\n{reservation_data}'
    from_email = 'settings.EMAIL_HOST_USER'  # Replace with your email
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
    
    return render('reservation.html')

def error(request, exception=None):
    return render(request, 'error.html', status=404)
