card_deck = input().split()
count_of_faro_shuffles = int(input())
for shuffle in range(count_of_faro_shuffles):
    final_deck = []
    middle_deck = len(card_deck) // 2
    left_deck = card_deck[0:middle_deck]
    right_deck = card_deck[middle_deck:]
    for index_of_the_card in range(len(left_deck)):
        final_deck.append(left_deck[index_of_the_card])
        final_deck.append(right_deck[index_of_the_card])
    card_deck = final_deck
print(card_deck)
