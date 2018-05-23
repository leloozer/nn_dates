import datetime

def nn_date_from_adv(words, token_index):
    """
    token_index nous donne la valeur du jour
    0 : avant-hier
    1 : hier
    2 : aujourd'hui
    3 : demain
    4 : après-demain
    """

    today = datetime.date.today()
    date = today + datetime.timedelta(days = (token_index - 2))
    return(str(date))
