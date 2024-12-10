persona = dict()
persona = dict() # dizionario vuoto
persona['nome'] = 'Giovanni'
persona['cognome'] = 'Bianchi'
persona['matricola'] = 256
persona
{'nome': 'Giovanni', 'cognome': 'Bianchi', 'matricola': 256}
persona['matricola'] = 3256
persona['nascita'] = 2000
persona
{'nome': 'Giovanni', 'cognome': 'Bianchi', 'matricola': 3256, 
'nascita': 2000}
persona.pop('nascita')
2000
'nascita' in persona
False