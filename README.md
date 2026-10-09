# Pràctica 1: Modelització i Visualització de Dades 

**Autor:** Marius Ionut Ursache    
**Grau en Enginyeria Informàtica** - Universitat Rovira i Virgili (URV)  
**Any acadèmic:** 2026-2027  


## Descripció del Projecte

Aquest projecte analitza críticament una visualització infogràfica publicada per "DadesRTVE" l'estiu de 2026 sobre l'evolució tèrmica estival a l'Espanya peninsular (1961–2026), basada en registres de l'AEMET.

A partir de la detecció d'errors perceptius i metodològics segons les teories d'Edward Tufte, baix ràtio Dades-Tinta, "chartjunk" i distorsió del Lie Factor i les lleis de la Gestalt (vulneració de la continuïtat temporal per diagrames de barres discrets), s'ha implementat:

1. **Preprocessament i normalització matemàtica:** Càlcul d'anomalies tèrmiques relatives respecte a la climatologia estàndard oficial, suavitzat de sèries temporals mitjançant mitjana mòbil a 10 anys, i categorització objectiva basada en percentils estadístics.
2. **Redisseny interactiu:** Desenvolupament d'una visualització web contínua amb Plotly, incorporant exploració sota demanda  i commutació dinàmica de mètriques (Temperatura Mitjana vs. Anomalia Tèrmica).


## Estructura del Repositori

Dades/dataset.csv              # Dades en brut extretes de la visualització de Datawrapper
Resultats/
    dataset_preprocesat.csv  # Sèrie històrica transformada amb noves mètriques
    grafic_interactiu.html   # Visualització interactiva Plotly (obrir al navegador)
    Temperatura Mitjana.png  # Captura de la vista de temperatura i tendència
    Anomalia Termica.png     # Captura de la vista d'anomalia
Scripts/
    ProcessarDades.py        # Script per a la neteja, normalització i càlculs estadístics
    GenerarGrafic.py         # Script per a la generació de la figura interactiva HTML
README.md                    # Documentació tècnica del repositori


## Requisits i Entorn d'Execució

El projecte s'ha desenvolupat amb **Python 3**. Per executar els scripts, cal disposar de les següents dependències:
- pip install pandas numpy plotly

## Guia d'Execució
Per reproduir el pipeline complet des del terminal, situa't al directori arrel del projecte o a la carpeta `Scripts`:

### 1. Processament i modelització de dades 
Llegeix `Dades/dataset.csv`, computa les noves variables climàtiques i desa el resultat a `Resultats/dataset_preprocesat.csv`:
- python Scripts/ProcessarDades.py


### 2. Generació del redisseny interactiu 
Genera la visualització dinàmica autònoma a `Resultats/grafic_interactiu.html`:
- python Scripts/GenerarGrafic.py

## Fonts i Referències
* **Gràfic original de referència:** https://www.rtve.es/noticias/20260831/verano-espana-olas-calor-noches-tropicales-muertes/17206364.shtml o https://datawrapper.dwcdn.net/yNEll/5/
* **Font de dades climàtiques:** Agència Estatal de Meteorologia (AEMET).
