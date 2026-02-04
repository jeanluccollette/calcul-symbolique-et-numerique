# Calcul symbolique et numérique

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
