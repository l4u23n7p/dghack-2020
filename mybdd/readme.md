# MyBDD

## Description

L'un de nos développeur a développé une nouvelle base de données. Le but : la rendre tellement incompréhensible pour les attaquants qu'aucun ne serait capable d'exploiter quelques vulnérabilités que ce soit.

Vous, persuadé que la sécurité par l'obscurité est vaine, souhaitez obtenir le contenu d'un fichier système (tel /home/my_chall_pwned/flag).

Le système, encore en phase de test, déployé par le développeur est lancé sur Debian 8 à l'aide de la commande suivante :

`su -c "socat -s TCP-LISTEN:50505,reuseaddr,fork,su=my_chall_pwned EXEC:'/home/my_chall_pwned/my_bdd /home/my_chall_pwned/database/test.db'"`

## Write-up

*Aucune validation*