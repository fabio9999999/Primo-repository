"""
testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.
'''

file_testo = open('testo.txt', 'w')

# Loop sulle righe che compongono la stringa multilinea
for riga in testo.split('\n'):     
    # Scrivo la riga nel file (ricordandomi di andare a capo con \n)
    file_testo.write(f'{riga}\n')   

# chiudo il file a fine operazioni
file_testo.close()

# Apro file in lettura
file_testo = open('testo.txt', 'r')   

# Leggo l'intero contenuto del file
contenuto = file_testo.readlines()                   

# Chiudo il file
file_testo.close()                              

# visualizzo il contenuto letto dal file
print(contenuto)

# visualizzo il tipo del contenuto letto
print(type(contenuto))
"""

"""
# oggetto da scrvere, ad esempio le soluzioni del problema regine
lista_numeri = [3, 6, 2, 7, 1, 4, 0]

# Apro un file binario in scrittura
binary_file = open('lista_numeri.bin', 'w') 

# Converto l'oggetto da scrivere in un gruppo di bytes
lista_numeri_bytes = bytearray(lista_numeri)

# Scrivo il gruppo di bytes nel file
binary_file.write(lista_numeri_bytes)           

# Chiudo il file
binary_file.close()
"""
"""
import json

data = {
  "Paolino Paperino": {
      "giorno": 9,
      "mese": "giugno",
      "anno": 1934,
      "età": 89,
      "sesso": "M",
      "mail": "paolino.paperin0@disney.org"}
  }

with open("data_file.json", "w") as write_file:
    # scrive il contenuto serializzato del dizionario nel file object
    json.dump(data, write_file)

with open('data_file.json', 'r') as in_file:
    # legge il contenuto del file in un dizionario
    data = json.load(in_file)

print(data2)
"""

"""
testo = Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.
Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.
The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.
About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
"""
"""
nome = 'nome'
anni = 42
altezza = 1.75

out = 'Mi chiamo ' + nome + ', ho ' + str(anni) + ' anni e sono alto ' + str(altezza) + \
'. Tra 145 anni avrò ' + str (anni+145) +' anni'

print(out)
"""


lista_lettere = ['M','A', 'T', 'T', 'A']

lista_lettere[4:4] = ['I','N']