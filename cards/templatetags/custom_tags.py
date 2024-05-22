from django import template

from cards.models import Cards


register = template.Library()


@register.simple_tag()
def get_deck_cards(deck_id, current_card_id):
    cnt = 0
    flag = 0
    while flag != 2:
        if Cards.objects.filter(deck=deck_id)[cnt].id == current_card_id:
            cnt += 1
            print('совпадение найдено', cnt)
            if cnt != len(Cards.objects.filter(deck=deck_id)):
                print("кверисет переполнен, обнуление")
                print(Cards.objects.filter(deck=deck_id)[cnt].id)
                return Cards.objects.filter(deck=deck_id)[cnt].id
            else:
                print("кверисет закончен, обнуление")
                return Cards.objects.filter(deck=deck_id)[0].id
        elif Cards.objects.filter(deck=deck_id)[cnt].id == len(Cards.objects.filter(deck=deck_id)):
            print('совпадение не найдено, прибавляем счетчик')
            cnt = 0
            flag += 1
        else:
            cnt += 1


