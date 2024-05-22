from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Cards, Deck
from .forms import CardsForm, DeckForm


class CardsList(ListView):
    model = Cards

    template_name = 'cards/card_list.html'
    context_object_name = 'Cards'
    paginate_by = 10

    def get_queryset(self):
        queryset = Cards.objects.filter(author=self.request.user.id)
        return queryset


class CardsDetail(LoginRequiredMixin, DetailView):
    model = Cards
    template_name = 'cards/card.html'
    context_object_name = 'Card'

    def get_object(self, *args, **kwargs):
        obj = super().get_object(queryset=self.queryset)
        return obj


@login_required
def image_upload_view(request):

    if request.method == 'POST':
        form = CardsForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.author_id = request.user.id
            form.save()
            img_obj = form.instance
            return render(request, r'/Users/nikitamacbookair/Desktop/python project/LearnEnglish/anki/templates/cards/card_edit.html', {'form': form, 'img_obj': img_obj})
    else:
        form = CardsForm()
    return render(request, r'/Users/nikitamacbookair/Desktop/python project/LearnEnglish/anki/templates/cards/card_edit.html', {'form': form})


class CardsDelete(LoginRequiredMixin, DeleteView):
    model = Cards
    template_name = 'cards/card_delete.html'
    success_url = reverse_lazy('card_list')


class DeckList(LoginRequiredMixin, ListView):
    model = Deck

    template_name = 'Deck/deck_list.html'
    context_object_name = 'Decks'
    paginate_by = 10

    def get_queryset(self):
        queryset = Deck.objects.filter(user=self.request.user.id)
        return queryset


class DeckCreate(LoginRequiredMixin, CreateView):
    form_class = DeckForm
    model = Deck
    template_name = 'cards/deck_edit.html'
    success_url = reverse_lazy('card_list')

    def form_valid(self, form):
        deck = form.save(commit=False)
        deck.user = self.request.user

        deck.save()
        print('Пост сохранен')
        return redirect('/cards/')
