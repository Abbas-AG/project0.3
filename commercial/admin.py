from django.contrib import admin
from .models import Contact, SpecialOffer, Room, Style, CoffeeBreak, Reservation, UserFavorite





admin.site.register(SpecialOffer)
admin.site.register(Room)
admin.site.register(Style)
admin.site.register(CoffeeBreak)
admin.site.register(Reservation)
admin.site.register(UserFavorite)
admin.site.register(Contact)
