"""
Trabalho de Entropia

Gustavo Costa Arakaki 0051352311028
"""
import pandas as pd
from Entropia_funcs import probs, entropia, MAXentropia

cidades = pd.read_excel('cidades.xlsx')
ruralUrban = cidades.RURAL_URBAN.values.tolist()
estados = cidades.STATE.values.tolist()

print(f"Entropia dos estados: {entropia(probs(estados))}")
print(f"Entropia máxima dos estados: {MAXentropia(estados)}")


print(f"Entropia das cidades rurais e urbanas: {entropia(probs(ruralUrban))}")
print(f"Entropia máxima das cidades rurais e urbanas: {MAXentropia(ruralUrban)}")
