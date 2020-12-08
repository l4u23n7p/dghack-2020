# Involucrypt 1

## Description

Pendant une investigation numérique sur un disque dur, vous trouvez un fichier chiffré en utilisant un algorithme propriétaire.

Heureusement, le script utilisé pour chiffrer et déchiffrer se trouve dans le même dossier, mais vous ne disposez pas de la clé. Bon courage !

## Solution

En analysant la fonction utilisée pour chiffrer, on remarque que chaque caractère de la clé est utilisé pour chiffrer 150 caractères.

En partant de ce principe et du nombre totale de caractère du fichier chiffré, on sait que la clé utile pour déchiffrer à une longueur de 3 caractères.

On fait donc un simple brute-force sur la clé avec le script `flag.py`.

On obtient le flag `TheKeyIsTooDamnWeak!`.

## Write-up

- [Nicolas Bourras](https://nicolasb.fr/blog/writeup-dghack-involucrypt-1/)
