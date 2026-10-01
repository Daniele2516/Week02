
# Definizione della classe Studente
class Studente:
    # Attributi
    # matricola = 0
    # nome = ""
    # cognome = ""

    # Costruttore, funzione standard per inizializzare l'oggetto
    def __init__(self, matricola, nome, cognome):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome

    # Altre funzioni della classe Studente
    def sostiene_esame(self):
        print("Sostiene esame")

    def si_unisce_a_gruppo_studentesco(self):
        print("Si unisce a gruppo studentesco")



# Creo un oggetto/istanza della classe Studente

s = Studente(123456, "Mario", "Rossi")
               # Sto creando uno studente ed inizializzandolo
               # Python chiama la funzione __init__()
#print(s)

# Accedo alla "pancia" dell'oggetto per leggere o scrivere i suoi attributi
print(f"{s.matricola} - {s.nome} - {s.cognome}")

s.sostiene_esame() # Posso invocare su QUELLO studente Mario Rossi
                   # la funzione che serve per fargli sostenere
                   # l'esame: DATI E OP. SUI DATI SONO INCAPSULATE NELL'OGGETTO

# Collezione di studenti come lista

lista_studenti = []
lista_studenti.append(s)
lista_studenti.append(Studente(67890,
                               "Gianni",
                               "Verdi"))

# Stampo la lista di studenti con for in
for studente in lista_studenti:
    print(studente.matricola, studente.nome, studente.cognome)