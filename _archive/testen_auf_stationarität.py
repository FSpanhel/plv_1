# %% [markdown] slideshow={"slide_type": "skip"}
# ## Testen auf Stationarität -> Am ende machen, low Priority

# %% [markdown] slideshow={"slide_type": "skip"}
# Angenommen unsere Daten werden durch den vorher beschriebenen AR(1) Prozess generiert, wie könnte somit ein Test auf (schwache) Stationarität aussehen?
#
# Wie könnte die Null- und Alternativhypothese aussehen?

# %% [markdown] slideshow={"slide_type": "skip"}
# 1. Die vorherigen Simulationen vorhin haben illustriert und der Beweis gezeigt, dass ein AR(1) Prozess (schwach) stationär ist solange |a| < 1 ist.
# 2. Man könnte also H_0: |a| >= 1 vs. H_1: |a| < 1.
# 3. Da in der Praxis in der Regel a >= 0, Vereinfachung zu H_0: a >= 1 vs. H_1: a < 1

# %% [markdown] slideshow={"slide_type": "skip"}
# ## Der (Augmented) Dickey-Fuller Test
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

# %% [markdown] slideshow={"slide_type": "skip"}
# ## Wie teste ich auf Stationarität in der Praxis?
# 1.	Theoretisches Resultat dass es keinen Test gibt der das asymptotische immer zeigen kann
#     1.	Vll. davor: Zeitreihen simulieren von statistischen Prozessen (u.a. Copula) und Frage ob schwach stationär (evtl. hierzu abstimmen)
# 1.	In der Praxis: Eher inhaltliche Überlegungen
#     1.	Deterministische Trends: Saisonalität 
# 1.	Davon abgesehen: Man kann nicht stationäre Prozess auch mit stationären approximieren (in der next step vorhersage), klappt ganz okay soweit nicht zu weit weg von 
#