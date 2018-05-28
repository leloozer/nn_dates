import datetime
import sys
import re
from time_word import Time_word
from time_key import Time_key

def wday_date(today, sentence, i):
    slen = len(sentence)
    future = None
    if (i > 0 and sentence[i - 1].get_adj() == 0):
        future = False
    elif (i < slen - 1 and sentence[i + 1].get_adj() == 1):
        future = False
    elif (i < slen - 1 and sentence[i + 1].get_adj() > 1):
        future = True
    sday = sentence[i].get_day()
    if (future == True or future == None):
        if (today.weekday() >= sday and future == True or today.weekday() > sday):
                daydiff = sday + 7 - today.weekday()
        else:
            daydiff = sday - today.weekday()
    else:
        if (today.weekday() <= sday):
            daydiff = -(today.weekday() + 7 - sday)
        else:
            daydiff = -(today.weekday() - sday)
    return (today + datetime.timedelta(days = daydiff))


def adv_date(today, sentence, i):
    return (today + datetime.timedelta(days = sentence[i].get_adv() - 2))

def nn_date(phrase):
    time_keys = Time_key.table
    today = datetime.date.today()
    sentence = []
    delimiters = [' ', ', ', '; ', ': ', '.']
    regexPattern = '|'.join(map(re.escape, delimiters))
    for word in re.split(regexPattern, phrase):
        sentence.append(Time_word(word, time_keys))
    for i in range(len(sentence)):
        if (not sentence[i].get_day() == -1):
            sentence[i].set_date(wday_date(today, sentence, i))
        elif (not sentence[i].get_adv() == -1):
            sentence[i].set_date(adv_date(today, sentence, i))
        print(sentence[i].get_date())

nn_date(sys.argv[1])
