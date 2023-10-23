from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Contact, Room, Style, CoffeeBreak, Reservation
from django.core.mail import send_mail
from .models import SpecialOffer, Room, Style, CoffeeBreak, Reservation
from django.template.loader import render_to_string


# Create your views here.

def index(request):
    rooms = Room.objects.all()
    print(rooms[0])
    styles = Style.objects.all()
    return render(request, 'index.html', {
        'rooms': rooms,
        'styles': styles
    })

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

# def home(request):
#     rooms = Room.objects.all()

#     styles = Style.objects.all()
#     return render(request, 'home.html', {
#         'rooms': rooms,
#         'styles': styles
#     })


def coffee(request):
    special_offers = CoffeeBreak.objects.all()
    return render(request, 'coffee.html', {
        'special_offers': special_offers
    })

def contact(request):

    if request.method == 'POST':
        full_name = request.POST.get('full_name')  
        message = request.POST.get('message')  
        subject = request.POST.get('subject')
        email = request.POST.get('email')

        contact = Contact(
            full_name= full_name,
            message = message,
            email = email,
            subject = subject
        )
        contact.save()
        return redirect("home")
    
    else:
        return render(request, 'contact.html')


def reservation(request):
    rooms = Room.objects.all()
    styles = Style.objects.all()
    coffee_offers = CoffeeBreak.objects.all()

    if request.method == 'POST':
        event_room_id = request.POST['event_room']
        event_style_id = request.POST['event_style']
        coffee_break_id = request.POST['coffee_offer']
        event_room = request.POST.get('event_room')
        date_and_time = request.POST.get('date_and_time')
        number_of_attendees = request.POST.get('number_of_attendees')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        notes = request.POST.get('notes')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        event_room = Room.objects.get(pk=event_room_id)
        event_style = Style.objects.get(pk=event_style_id)
        coffee_break = CoffeeBreak.objects.get(pk=coffee_break_id)
        reservation = Reservation(
            event_room=event_room,
            event_style=event_style,
            coffee_break=coffee_break,
            date_and_time=date_and_time,
            number_of_attendees=number_of_attendees,
            notes=notes,
            email=email,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
        )
        reservation.save()

        send_mail(
            'Reservation Confirmation',
            render_to_string ('email.html', {'reservation': reservation}),
            "abbasgamer9999@gmail.com",
            [email],
            fail_silently=False)

    context = {
        'rooms': rooms,
        'styles': styles,
        'coffee_offers': coffee_offers,
    }
    
    return render(request, 'reservation.html', context)


def error(request, exception=None):
    return render(request, 'error.html', status=404)


