from random import shuffle

cardSuits = ["♥", "♦", "♣", "♠"]
varDeck = []
for suits in cardSuits:
    for varCards in range(1,14):
        if varCards == 11:
            varDeck.append("J" + suits )
        elif varCards == 12:
            varDeck.append("Q" + suits )
        elif varCards == 13:
            varDeck.append("K" + suits )
        elif varCards == 1:
            varDeck.append("A" + suits )
        else:
            varDeck.append(str(varCards) + suits)
print(varDeck)
