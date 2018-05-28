import datetime
import sys
import json
from time_key import Time_key

def	check_adjs(nlu, i, adjs):
	if (i > 0):
		if (nlu[i - 1]["source"] == adjs[0]):
			return (False)
	if (i < len(nlu) - 1):
		if (nlu[i + 1]["source"] == adjs[1]):
			return (False)
		if (nlu[i + 1]["source"] == adjs[2]
			or nlu[i + 1]["source"] == adjs[3]):
			return (True)
	return (None)
		

def	check_wday(nlu, i, future, time_keys, today):
	days = time_keys["days"]
	if (not nlu[i]["meaning"] or not nlu[i]["meaning"][0] == days["meaning"]):
		return (None)
	day = nlu[i]["source"]
	sday = None
	for j in range(len(days["lemma"])):
		if (day == days["lemma"][j]):
			sday = j
			break
	if (not sday):
		return (None)
	f = check_adjs(nlu, i, time_keys["adjs"])
	if (not f is None):
		future = f
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
	return (daydiff)

def	check_RB(nlu, rb):
	for i in range(len(rb)):
		if (nlu["source"] == rb[i]):
			return (i - 2)
	return (None)

def	nn_date(phrase):
	time_keys = Time_key.table
	today = datetime.date.today()
	date = None
	future = None
	nlu = phrase["NLU"]
	for i in range(len(nlu)):
		a_date = check_RB(nlu[i], time_keys["RB"]["lemma"])
		if (a_date is None):
			a_date = check_wday(nlu, i, future, time_keys, today)
		if (a_date):
			a_date = today + datetime.timedelta(days = a_date)
			if (date is None):
				date = a_date
			elif (not date == a_date):
				return (None)
	return (date)
		

with open(sys.argv[1]) as file:
	print(nn_date(json.load(file)))
