class Time_key:
	table = {
		'days' :{
			'meaning' : 'Jourssemaines',
		 	'lemma' :['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
			},

		'RB' :{
			'tag' : 'RB',
			'lemma' : ['avant-hier', 'hier', "aujourd'hui",
						'demain', u'après-demain']
			},

		'ordinals' :{
			'meaning' : 'Ordinaux',
			'lemma' : [u'précédent', 'dernier', 'suivant', 'prochain']
			},

		'months' :{
			'meaning' : 'Mois',
			'lemma' : ['semaine', 'mois']
			}
		}
