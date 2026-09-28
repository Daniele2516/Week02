# Creazione di una lista vuota
lista = []

# Creazione di una lista contentente elementi
lista = [45, 19, 25, 67, 78, 19, 900]

# Accesso agli elementi per indice
elemento = lista[0] # Indici da 0 a len(lista)-1
print(len(lista)) # Stampa della dimensione

# Aggiunta di un elemento in coda
lista.append(1500)

# Aggiunta di un altro elemento (in questo caso str)
#lista.insert(2, "Valore")
# Sconsigliato creare liste con elementi di tipo diverso

# Ordinamento di liste
print("Lista prima dell'ordinamento")
print(lista)
lista.sort() # Ordina la lista, dopo averla chiamata lista è ordinata
print("Lista dopo l'ordinamento")
print(lista)

ordinata = lista.sorted() # Altra funzone, restituisce una nuova lista, ordinata

# Estrazione sotto-liste, come per le stringhe

stringa = "La mia stringa"
sottostringa = stringa[0 : 4]

sottolista = lista[0 : 4]

# Verifica della presenza di elementi

if 78 in lista:
    print("Valore presente")
else:
    print("Valore assente")

# Posizione/indice della prima occorrenza dell'elemento 19

indice = lista.index(19)
print(f"Posizione: {indice}")

# Funzioni aritmetiche sugli elementi della lista, es. somma di tutti gli elementi
somma = sum(lista)
print(somma)
