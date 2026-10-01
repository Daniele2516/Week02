
lista = [4, 6]

tupla = (4, 6, -5) # Es. un punto nello spazio 3D

# Dizionario di studenti con chiave la matricola e valore il nome/cognome
diz_studenti = { "015675": "Mario Rossi", "123456" : "Gianni Verdi" }

#Con una lista di liste (ovvero una tabella)
lista_studenti = [ ["015675", "Mario Rossi" ],
                   ["123456", "Gianni Verdi" ]
                 ]
# Liste separate
lista_matricole = ["015675", "123456"]
lista_nomi_cognomi= ["Mario Rossi", "Gianni Verdi"]

nuova_lista = lista_studenti # Non copia la lista
# Crea solamente un "alias", in memoria i dati non sono stati duplicati

copia_della_lista=list(nuova_lista) # Per una vera copia uso la funzione list()