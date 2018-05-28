import datetime

class Time_word:
    def weekday(self, time_keys):
        wdays = time_keys['wdays']
        for i in range(len(wdays)):
            if (wdays[i] == self._lemma):
                return (i)
        return (-1)

    def adverb(self, time_keys):
        advs = time_keys['advs']
        if (self._day == -1):
            for i in range(len(advs)):
                if (advs[i] == self._lemma):
                    return (i)
        return (-1)

    def adjective(self, time_keys):
        adjs = time_keys['adjs']
        if (self._day is -1 and self._adv is -1):
            for i in range(len(adjs)):
                if (adjs[i] == self._lemma):
                    return (i)
        return (-1)

    def nouns(self, time_keys):
        nouns = time_keys['nouns']
        if (self._day is -1 and self._adv is -1 and self._adj is -1):
            for i in range(len(nouns)):
                if (nouns[i] == self._lemma):
                    return (i)
        return (-1)

    def number(self, time_keys):
        return (-1)

    def __init__(self, word, time_keys):
        self._lemma = word.lower()
        self._day = self.weekday(time_keys)
        self._adv = self.adverb(time_keys)
        self._adj = self.adjective(time_keys)
        self._noun = self.nouns(time_keys)
        self._num = self.number(time_keys)
        self._date = None

    def get_attributes(self):
        attr = [self._lemma, self._day, self._adv, self._adj, self._noun,
                self._num, self._time]
        return (attr)

    def get_day(self):
        return (self._day)

    def get_adv(self):
        return (self._adv)

    def get_adj(self):
        return (self._adj)

    def get_num(self):
        return (self._num)

    def get_date(self):
        return (self._date)

    def set_date(self, date):
        self._date = date
