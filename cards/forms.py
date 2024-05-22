from django import forms
from .models import Cards, Deck


class CardsForm(forms.ModelForm):
    class Meta:
        model = Cards
        fields = ['front_text', 'back_text', 'image', 'deck']


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['name']
