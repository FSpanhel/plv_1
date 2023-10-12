# %% [markdown] slideshow={"slide_type": "slide"}
# # Appendix

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Ausführliche Skizze des Beweis für die schwache Stationarität des AR(1) Prozesses

# %% [markdown] slideshow={"slide_type": "slide"}
# <blockquote style="width: auto; background-color: 
#                    lightyellow; color: black; 
#                    margin: 70px; 
#                    padding: 5px; 
#                    border: 3px solid #ccc;
#                    margin-bottom: -0px;
#                    margin-top: 40px
#                    ">
# Theorem: (<strong>Hinreichende Bedingungen für die Stationarität eines AR(1) Prozesses</strong>)<br>
# Sei $Y_t = aY_{t-1} + U_t$, wobei $(U_t)_{t \in \mathbb{Z}}$ Weißes Rauschen ist und $\sup_{t \in \mathbb{Z}} E[Y_t^2] < \infty$. <br><br>
# Falls $|a| < 1$,  dann ist $(Y_t)_{t \in \mathbb{Z}}$ schwach stationär.
# </blockquote>
#
# - Der Beweis dieses Theorems ist nicht trivial.
# - Im Folgenden werden die zwei Schritte deshalb nur skizziert.
#     1. Limes Repräsentation von $Y_t$ als eine Funktion von $(U_t)_{t \in \mathbb{Z}}$.
#     2. Berechung des Erwartungswerts und Kovarianzfunktion von $(Y_t)_{t \in \mathbb{Z}}$.

# %% [markdown] slideshow={"slide_type": "notes"}
# In der Literatur so nicht so einfach zu finden und nicht exakt
#
# Hier keine Konstante $c$ betrachtet.

# %% [markdown] slideshow={"slide_type": "slide"}
# **Schritt 1: Limes Repräsentation von $Y_t$ als eine Funktion von $(U_t)_{t \in \mathbb{Z}}$.**
#
# Rekursive Substituierung führt zu
#
# $$
# \begin{align}
# Y_t & = aY_{t-1} + U_t = a(aY_{t-2} + U_{t-1}) + U_t = \ldots = 
# \\ & = \underbrace{a^h Y_{t-h}}_{=:A_h} + \underbrace{\sum_{i=0}^{h-1}a^{i}U_{t-i}}_{=:B_h} =: X_h
# \end{align}
# $$
#
# Was passiert mit $X_h$, wenn $h\to\infty$?

# %% [markdown] slideshow={"slide_type": "slide"}
# &#9888;&#65039; Da $X_h:=A_h + B_h$ eine Zufallsvariable ist, müssen wir zunächst eine Konvergenzart wählen.
# <blockquote style="width: auto; background-color: 
#                    lightyellow; color: black; 
#                    margin: 70px; 
#                    padding: 5px; 
#                    border: 3px solid #ccc;
#                    margin-bottom: -8px
#                    ">
# Definition: (<strong>Konvergenz im quadratischen Mittel</strong>)<br>
# Eine Folge von Zufallsvariable $(X_t)_{t\in\mathbb{Z}}$ konvergiert im quadratischen Mittel gegen eine Zufallsvariable $X$ $:\!\!\iff$
# $\lim_{t\to\infty} E[(X_t-X)^2] = 0$. In diesem Fall schreiben wir $X_t \stackrel{2}{\to} X$.
# </blockquote>

# %% [markdown] slideshow={"slide_type": "fragment"}
# <div style="margin-bottom: -2040px, margin-top: 0px">
#
# - Falls $A_t \stackrel{2}{\to} A$ und $B_t \stackrel{2}{\to} B$ dann gilt $A_t + B_t \stackrel{2}{\to} A + B$.
# - Wir können also die Konvergenz von $A_h$ und $B_h$ separat betrachten.
#
# </div>

# %% [markdown] slideshow={"slide_type": "fragment"}
# <div style="margin-bottom: -440px, margin-top: -100px">
#
# - Dass $A_h \stackrel{2}{\to} 0$, wenn $|a|<1$ und $\sup_{t \in \mathbb{Z}} E[Y_t^2] < \infty$, lässt sich leicht zeigen.
# - Dass eine Zufallsvariable $B \in L^2$ existiert, gegen die $B_h$ im quadratischen Mittel konvergiert, folgt daraus, dass der $L^2$ Raum vollständig ist und man zeigen kann, dass $B_h$ eine Cauchy Folge ist falls $|a| < 1$ und $(U_t)_{t\in\mathbb{Z}}$ weißes Rauschen ist.
# - Insgesamt folgt also $\exists X \in L^2\colon X_h \stackrel{2}{\to} X$.
# </div>
#     
#     

# %% [markdown] slideshow={"slide_type": "notes"}
# - One way to define the distance between X_t and X is the expectation of the squared difference.
# - Das ist für uns hilfreich da wir ja später an dem Erwartungswert und der Varianz des Limes interessiert sind.
# - [Dreiecksungleichung](https://math.stackexchange.com/questions/4281919/convergence-of-a-linear-combination-of-random-variables), diese kann ich nutzen weil E[(X_t-X)^2] = L2_Norm^2 und die Dreiecksungleichung für die L2_Norm gilt.
# - Frage: Wer weiß noch alles was eine Cauchy Folge ist?
# - Wieso ist $B_h$ eine Cauchy Folge
# $B_h \text{ is Cauchy } \rightarrow E[(B_m-B_n)^2] < \epsilon$
# $E[(\sum_{i=N+1}^Ma_iU_{t-i})^2] \stackrel{U is WN}{=} \sum_{i=N+1}^M a^{2i}E[U_{t-i}^2] = E[U_{t-i}^2]\underbrace{\sum_{i=N+1}^M a^{2i}}_{Cauchy}$

# %% [markdown] slideshow={"slide_type": "slide"}
# **Schritt 2: Berechung des Erwartungswerts und Kovarianzfunktion von $(Y_t)_{t \in \mathbb{Z}}$.**
#
# Setzen wir $\displaystyle{X:= \sum_{i=0}^{\infty}a^{i}U_{t_i}}$ dann gilt $\displaystyle{Y_t \stackrel{2}{\to} \sum_{i=0}^{\infty}a^{i}U_{t_i}}$ und es folgt
# <!--
# Falls $|a|<1$, folgt dass $\sum_{i=0}^{\infty}|a^{i}|\in \mathbb{R}$, und wenn  $(U_t)_{t\in\mathbb{Z}}$ Weißes Rauschen ist folgt aus [Fubini-Tonelli Theorems](https://en.wikipedia.org/wiki/Fubini's_theorem#Fubini-Tonelli) 
#
# Durch die Anwendung des [Fubini-Tonelli Theorems](https://en.wikipedia.org/wiki/Fubini's_theorem#Fubini-Tonelli) und der Tatsache, dass $\sum_{i=0}^{\infty}|a^{i}|\in \mathbb{R}$, falls $|a|<1$, und $(U_t)_{t\in\mathbb{Z}}$ Weißes Rauschen ist, folgt
# -->
#
# $$
# \begin{align*}
# E[Y_t] & = E[\sum_{i=0}^{\infty}a^{i}U_{t-i}] \stackrel{|a|<1,\ (U_t)_{t\in\mathbb{Z}} \text{Weißes Rauschen}}{=} \sum_{i=0}^{\infty}a^{i}\underbrace{E[U_{t-i}]}_{=\ 0} = 0
# \end{align*}
# $$
#
#
# $$
# \gamma(t, h) = Cov[Y_t, Y_{t-h}] 
# %= E[\sum_{i=0}^{\infty}a^{i}U_{t-i} \sum_{j=0}^{\infty}a^{j}U_{t-h-j}] 
# \stackrel{|a|<1,\ (U_t)_{t\in\mathbb{Z}} \text{Weißes Rauschen}}{=}
# %\ldots
# %\sum_{i=0}^{\infty}\sum_{j=0}^{\infty}a^{i}a^{j}\underbrace{E[U_{t-i}U_{t-h-j}}_{\sigma_U^2 \text{ if } i = h + j, \text{ else } 0}]
# %\\
# %\stackrel{i:=h+j}{=} \sum_{j=0}^{\infty}a^{h+j}a^{j}\sigma_U^2 = a^h\sum_{j=0}^{\infty}a^{2j}\sigma_U^2
# a^h\frac{\sigma_U^2}{1-a^2} \in \mathbb{R}
# $$
#
# Somit ist $E[Y_t]=0$ und $\gamma(t, h) \in \mathbb{R}$ hängt nicht von $t$ ab. Folglich ist $(Y_t)_{t \in \mathbb{Z}}$ stationär. &#11035;

# %% [markdown] slideshow={"slide_type": "notes"}
# - Noch offener Punkt, wenn X_h to X, wieso ist dann E[Y_t] = E[X]? Also warum passt das alles?
# - [Fubini-Tonelli Theorems](https://en.wikipedia.org/wiki/Fubini's_theorem#Fubini-Tonelli)
# https://math.stackexchange.com/questions/1166994/linearity-of-expectation-for-infinite-sums
# - Fubini-Tonelli oder Dominated Convergence Theorem erlaubt vertauschen
