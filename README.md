# SVAW (Scanner de Vulnérabilités des Applications Web)

> **Avertissement** : SVAW ne doit être utilisé que sur des sites dont vous êtes propriétaire ou pour lesquels vous avez une autorisation écrite. L'auteur décline toute responsabilité en cas d'usage non autorisé.

## Description

**SVAW** est un scanner de vulnérabilités écrit en Python. Il détecte les reflets de payloads XSS dans les champs de formulaire d'une page web.

Le projet repose sur trois bibliothèques :

1. `requests` : télécharge la page à analyser.
2. `BeautifulSoup` : analyse le HTML pour repérer les champs `<input>`.
3. `urllib.parse` (`urljoin`) : construit l'adresse complète de destination.

Les scripts de test sont intégrés directement dans `svaw.py`.

## Limites connues

- Un reflet n'est pas une preuve de faille : il doit être vérifié manuellement dans un navigateur.
- Le test des formulaires POST est en cours de développement.

## Installation

```bash
git clone https://github.com/TON_UTILISATEUR/svaw.git
cd svaw
pip install -r requirements.txt
```

## Utilisation

```bash
python svaw.py
```

Le programme demande ensuite l'URL de la cible.

## Licence

Ce projet est distribué sous licence MIT. Voir le fichier `LICENSE`.
