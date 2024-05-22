from django.contrib import admin
from django import forms

from .models import Cards, Deck


admin.site.register(Cards)
admin.site.register(Deck)
