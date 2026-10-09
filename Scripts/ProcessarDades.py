import pandas as pd
import numpy as np
import os

# Obtenim la ruta absoluta del directori on es troba l'script (Scripts/)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Definim les rutes cap a Dades i Resultats (carpeta Codi/)
base_dir = os.path.dirname(script_dir)
input_path = os.path.join(base_dir, 'Dades', 'dataset.csv')
output_dir = os.path.join(base_dir, 'Resultats')
output_path = os.path.join(output_dir, 'dataset_preprocesat.csv')

# Creem la carpeta Resultats automàticament si no existeix
os.makedirs(output_dir, exist_ok=True)

# 1. Carregar les dades des de la carpeta Dades
df = pd.read_csv(input_path)

# 2. OPERACIÓ 1: Normalització a dades relatives (Càlcul d'anomalia climàtica)
# Calculem la temperatura de referència del període estàndard 1991-2020
t_ref = df[(df['year'] >= 1991) & (df['year'] <= 2020)]['temp_media'].mean()
df['anomalia_oficial'] = (df['temp_media'] - t_ref).round(2)

# 3. OPERACIÓ 2: Reconfiguració i ordenació temporal (Mitjana mòbil) 
# Ordenem cronològicament i apliquem una mitjana mòbil a 10 anys
df = df.sort_values('year').reset_index(drop=True)
df['tendencia_10_anys'] = df['temp_media'].rolling(window=10, min_periods=1).mean().round(2)

# 4. OPERACIÓ 3: Agrupament lògic de variables (Categorització per percentils)
p20, p40, p60, p80 = df['temp_media'].quantile([0.2, 0.4, 0.6, 0.8])

condicions = [
    df['temp_media'] <= p20,
    (df['temp_media'] > p20) & (df['temp_media'] <= p40),
    (df['temp_media'] > p40) & (df['temp_media'] <= p60),
    (df['temp_media'] > p60) & (df['temp_media'] <= p80),
    df['temp_media'] > p80
]

etiquetes = ['Molt fred', 'Fred', 'Normal', 'Càlid', 'Molt càlid']
df['categoria_objectiva'] = np.select(condicions, etiquetes, default='Normal')

# 5. Guardar el nou fitxer netejat a la carpeta Resultats
df.to_csv(output_path, index=False)
print(f"Fitxer processat creat amb èxit a:\n{output_path}")