import sys
from nn_date_from_day import nn_date_from_day
from nn_date_from_adv import nn_date_from_adv

def nn_dates(phrase):
    import datetime
    import calendar

    days = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    adv = ["avant-hier", "hier", "aujourd'hui", "demain", u"après-demain"]
    words = phrase.split(' ')
    token = None
    for i in range(len(words)):
        words[i] = words[i].lower()
        for t in days:
            if t == words[i]:
                return (nn_date_from_day(words, day_index=i, future=True))
        for j in range(len(adv)):
            if (adv[j] == words[i] and token is None):
                token = j
    if token is None:
        return None
    else:
        return (nn_date_from_adv(words, token_index=token))

print(nn_dates(sys.argv[1]))
