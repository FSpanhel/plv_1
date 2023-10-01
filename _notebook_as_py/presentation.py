# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% slideshow={"slide_type": "skip"}
from IPython.display import display, HTML
display(HTML("<style>.container { width:95% !important; }</style>"))

# %% [markdown] slideshow={"slide_type": "slide"}
# [TODO] 
# - QR Code zu Binder Präsentation, Tiny URL verwenden?
# - Es kann bis zu 30 Sekunden dauern, bis die Präsentation gestartet wird.
# - Kurzes Intro zu Bedienung:
#     - Space
#     - Shift + Tab
#     - Zommen der Website

# %% [markdown] slideshow={"slide_type": "slide"}
# <div align="center" style="font-size:70px;">
# Probelehrveranstaltung für die Professur für Angewandte Mathematik mit Schwerpunkt Statistical Learning
# <br><br>
# Stationarität von Zeitreihen mit Anwendung an einem praktischen Beispiel
# <div/>
#     
# <div align="left" style="font-size:16px;">
# <div/>
#
#

# %% [markdown] slideshow={"slide_type": "notes"}
# [TODO] Evtl. TOC?
# - About me
# - Einführung und Motivation [5 Min]
# - Stationarität
#     - Definition [4 Min]
#     - Illustration anhand AR(1) [6 Min]
#     - Testen von Stationarität [4 Min]
# - Praktische Anwendung auf X Daten [10 Min]

# %% [markdown] slideshow={"slide_type": "slide"}
# # About me [TODO: Auf Deutsch]
# <br>
# <br>
# <div style="font-size:40px;">
# Dr. rer. nat. Fabian Spanhel
# <div/>
#     
# <div align="left" style="font-size:32px;">
# <div/>
# <br>
#
# - Studies in economics with a focus on econometrics & statistics
# - PhD in statistics
# - Since November 2016 working as a Data Scientist at ProSiebenSat.1

# %% [markdown] slideshow={"slide_type": "slide"}
# # Einführung und Motivation
# Wenn wir von einer (diskreten) Zeitreihe sprechen, können damit zwei verschiedene Begriffe gemeint sein:
# 1. Eine Zeitreihe ist eine Abfolge von Daten, die in zeitlicher Reihenfolge angeordnet sind -> Beispiele.
# 2. Eine Zeitreihe ist ein stochastischer Prozess, d.h., ein Folge von Zufallsvariablen mit einem Index der für Zeitpunkte steht.
#
# **Die Verbindung zwischen 1. und 2. ergibt sich dadruch, dass (in der Statistik) Daten in 1. als eine Stichprobe oder Realisierung eines zugrunde liegenden stochastischen Prozess in 2. aufgefasst werden.**
#
#
# Eine (diskrete) Zeitreihe ist eine zeitlich geordnete Folge statistischer Maßzahlen.
#
#
# äquidistant
#
# Warum Zeitreihen modellieren sinnvoll ist

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Illustration des Zusammenhangs zwischen Zeitreihendaten und -prozess

# %% [markdown]
# ## Annahmen an einen Zeitreihenprozess für die statistische Inferenz und Modellierung

# %%
Für die statistische Inferenz mit Zeitreihen müssen Annahmen getroffen werden, da in der Praxis meist nur eine Realisierung des die Zeitreihe generierenden Prozesses vorliegt. Die Annahme der Ergodizität bedeutet, dass Stichprobenmomente, die aus einer endlichen Zeitreihe gewonnen werden, für 
�
→
∞T\rightarrow \infty  quasi gegen die Momente der Grundgesamtheit konvergieren.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Stationarität

# %% [markdown] slideshow={"slide_type": "slide"}
# ## (Strikte Stationarität) und Kovarianzstationarität 
# Frage hier an die Studierenden: Welche Definition ist stärker?
# Evtl. hier auch wieder Grafik mit 4 Punkten und daran sichtbar machen (auf ZVs Ebene)
#     Mittelwert der Trajektorien sollte gleich sein

# %% [markdown] slideshow={"slide_type": "notes"}
# Evtl. Beispiel für Zeitreihenprozesse, sind die stationär? Darüber abstimmen, mit ja/nein/weiß nicht/kommt drauf an (Es reicht wenn sie die Erwartungs- und Varianzstationarität überprüfen)
# 1. iid Exponential
# 2. MA(1)
# 3. AR(1)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Illustration anhand der Simulation eines (linearen) AR(1) Prozesses

# %% [markdown] slideshow={"slide_type": "notes"}
# 1. Modellgleichung
#     1. Autoregressive weil auf sich selbst regressiert, der Ordnung 1 weil ein Lag
#     1. Was bedeutet das? Was ist a?
#     1. Was ist wenn a negativ ist? Interessant weil ich sehr gut schätzen kann (Bild mit Normalverteilung)
# 1. Simulationsbilder in Abhängigkeit von a
#     1. Simulation nicht stationär weil wir immer mit gleichen Wert starten, aber schauen wir mal was passiert
# 1.	Theoretischen Beweis skizzieren (schon sophisticated, bei Copulas einfacher)
#     1. Nur mean stationarität zeigen
#     1.	Beweis für Kovarianzstationarität analog (Kovarianz auch nur Erwartungswert), oder E[Y_tY_{t-h}^k], k = 0, 1
#     1.	Beweis für strikt stationär schwierig, aber auch |a| <=1
#         1.	Stärkere Annahmen and die Abhängigkeit der Störterme
#         2.	Keine geschlossene Form für die Multivariate Verteilung im allgemeinen (nur durch Simulationen möglich)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Testen auf Stationarität

# %% [markdown] slideshow={"slide_type": "slide"}
# Angenommen unsere Daten werden durch den vorher beschriebenen AR(1) Prozess generiert, wie könnte somit ein Test auf (schwache) Stationarität aussehen?
#
# Wie könnte die Null- und Alternativhypothese aussehen?

# %% [markdown] slideshow={"slide_type": "fragment"}
# 1. Die vorherigen Simulationen vorhin haben illustriert und der Beweis gezeigt, dass ein AR(1) Prozess (schwach) stationär ist solange |a| < 1 ist.
# 2. Man könnte also H_0: |a| >= 1 vs. H_1: |a| < 1.
# 3. Da in der Praxis in der Regel a >= 0, Vereinfachung zu H_0: a >= 1 vs. H_1: a < 1

# %% [markdown] slideshow={"slide_type": "slide"}
# ## The (augmented) Dickey-Fuller Test
# 5. Der Dickey-Fuller Test macht das im Prinzip (verwendet aber die Differenzen)
# 5. Erweiterung zum Augmented Dickey-Fuller Test
#
# Der (A)DF Test ist vermutlich der populärste Test für die (schwache) Stationarität einer Zeitreihen.
# Allerdings ist der damit auch vermutlich einer der Tests dessen Annahmen nicht erfüllt sind.
# - Die Zeitreihendaten werden durch einen (linearen) autoregressiven Prozess generiert.
# - Die Störterme/Innovationen des Process sind iid N(0, \sigma^2)
#

# %% [markdown] slideshow={"slide_type": "notes"}
# Diskussion: 1. Annahme approximation okay, 2. aber eigentlich nie erfüllt.
#
# Evtl. Simulation zeigen, dass ADF Test nicht covered wenn Störterme N(0, \sigma^2)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Wie teste ich auf Stationarität in der Praxis?
# 1.	Theoretisches Resultat dass es keinen Test gibt der das asymptotische immer zeigen kann
#     1.	Vll. davor: Zeitreihen simulieren von statistischen Prozessen (u.a. Copula) und Frage ob schwach stationär (evtl. hierzu abstimmen)
# 1.	In der Praxis: Eher inhaltliche Überlegungen
#     1.	Deterministische Trends: Saisonalität 
# 1.	Davon abgesehen: Man kann nicht stationäre Prozess auch mit stationären approximieren (in der next step vorhersage), klappt ganz okay soweit nicht zu weit weg von 
#

# %% [markdown] slideshow={"slide_type": "slide"}
# # Praktische Anwendung

# %% [markdown] slideshow={"slide_type": "slide"}
# # Literatur
