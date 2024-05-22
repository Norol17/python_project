from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (CardsList, CardsDetail, CardsDelete, DeckCreate, DeckList, image_upload_view)


urlpatterns = [
   path('', CardsList.as_view()),

   path('cards/', CardsList.as_view(), name='card_list'),
   path('card/<int:pk>', CardsDetail.as_view(), name='card'),
   path('cards/create/', image_upload_view, name='card_create'),
   path('card/<int:pk>/delete/', CardsDelete.as_view(), name='card_delete'),

   path('deck_create/', DeckCreate.as_view(), name='deck_create'),
   path('decks/', DeckList.as_view(), name='deck_list'),
]
