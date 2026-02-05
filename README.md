# Calcul symbolique et numérique

## Introduction

En Python, le package **sympy** permet de disposer de méthodes très performantes pour le calcul symbolique. Si, par
ailleurs, elles sont utilisées dans un notebook, l'affichage des résultats s'effectue dans un format comparable
à celui obtenu avec le langage **latex**.

Pour envisager ensuite des applications numériques, la fonction **lambdify** convertit une expression
obtenue avec **sympy** en une fonction qui affecte des valeurs numériques aux symboles.

Pour illustrer ces possibilités par un exemple, la mise en équation d'un système chariot-pendule en calcul symbolique
est détaillée. Elle est ensuite exploitée en numérique dans des environnements tels que **numpy** et **scipy**.

## Exemple choisi

On considère un chariot de masse $M$ se déplaçant sans frottement, guidé par un rail horizontal. Sur ce chariot s'applique
une force horizontale $F$. Sa position est une abscisse $x$, sa vitesse est notée $x^{(1)}$ et son accélération $x^{(2)}$
(dérivée première et seconde par rapport au temps).

Sous ce chariot est suspendu un pendule constitué d'une tige rigide de longueur $l$ de masse négligeable et d'une masse
$m$ à son extrémité. Sa position angulaire par rapport à la verticale (dirigée vers le bas) est notée $\phi$. La vitesse angulaire est notée
$\phi^{(1)}$ et l'accélération $\phi^{(2)}$.

L'accélération de la pesanteur est notée $g$.

## Principe fondamental de la dynamique appliqué au pendule et au chariot

Le principe appliqué au pendule seul, après projection sur un axe normal au pendule, donne une première équation.

$$g \\sin{\\left(\\phi \\right)} + l \\phi^{(2)} + x^{(2)} \\cos{\\left(\\phi \\right)} = 0$$

Le principe appliqué au chariot, prenant en compte la composante horizontale de la force de réaction du pendule sur le chariot, donne
une seconde équation.

$$- F - l m \\left(\\phi^{(1)}\\right)^{2} \\sin{\\left(\\phi \\right)} + l m \\phi^{(2)} \\cos{\\left(\\phi \\right)} + x^{(2)} \\left(M + m\\right) = 0$$

## Equation d'état

L'état du système complet peut être décrit par le vecteur d'état 

$$\vec{y}=\begin{pmatrix}
x\\
\phi\\
x^{(1)}\\
\phi^{(1)}
\end{pmatrix}$$

L'équation d'évolution se présentera sous la forme

$$\dfrac{d\vec{y}}{dt}=f(\vec{y},F)$$

## Utilisation de Python

Le but est maintenant de

- mettre en forme l'équation d'état avec les outils de calcul symbolique du package **sympy**
- exploiter les résultats du calcul symbolique pour simuler numériquement le système, via la fonction **solve_ivp** du package **scipy**

## Calcul symbolique

### Définition des symboles

Dans le [notebook](chariot_pendule_sym.ipynb) fourni, les symboles s'afficheront conformément aux notations initialement choisies.

```python
import sympy as sp
from IPython.display import display, Math
x, phi, dx, dphi, d2x, d2phi, g, l, m, M, F = \
    sp.symbols('x, phi, x^(1}, phi^(1), x^(2), phi^(2), g, l, m, M, F')
```

### Equation du pendule

```python
EQP = d2x*sp.cos(phi)+l*d2phi+g*sp.sin(phi)
display(Math(sp.latex(EQP)+' = 0'))
```

### Equation du chariot

```python
EQC = -F + (m+M)*d2x+m*l*sp.cos(phi)*d2phi-m*l*sp.sin(phi)*dphi**2
display(Math(sp.latex(EQC)+' = 0'))
```

### Principe suivi

L'idée est ensuite d'accéder progressivement aux expressions de $x^{(2)}$ (variable **D2X**) et $\phi^{(2)}$ (variable **D2PHI**) ne faisant intervenir que
les composantes du vecteur d'état $\vec{y}$ et la force $F$, via la fonction **solve** et la méthode **subs** de **sympy**.

### Interface avec les applications numériques

Ces expressions finalement obtenues permettent de construire des fonctions qui affecteront des valeurs numériques aux symboles utilisés.

```python
D2X_NUM = sp.lambdify([phi, dx, dphi, F, g, l, m, M], D2X, 'numpy')
D2PHI_NUM = sp.lambdify([phi, dx, dphi, F, g, l, m, M], D2PHI, 'numpy')
```

Ces fonctions seront utilisées dans la fonction $f$ intervenant dans l'équation d'évolution.

$$\dfrac{d\vec{y}}{dt}=f(\vec{y},F)$$

Cette fonction permettra alors de mettre en oeuvre une méthode numérique de résolution de l'équation d'évolution,
via la fonction **solve_ivp** du package **scipy**.

## Remarques

Le [notebook](chariot_pendule_sym.ipynb) fourni détaille les méthodes, en affichant par ailleurs les résultats
dans un format similaire à celui qui est obtenu avec un code écrit en **latex**.

Le [programme](chariot_pendule_sym.py) fourni reprend juste les étapes essentielles. Pour réaliser
l'interface entre le calcul symbolique et numérique et bien séparer ces calculs, une attention
a été apportée de sorte de n'échanger que les informations strictement nécessaires et
de n'utiliser en aucun cas des variables globales.

```python
D2X_F, D2PHI_F = calcul_symb()
calcul_nume(D2X_F, D2PHI_F)
```




