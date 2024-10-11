# WhatsAppAIModerateur
C'est un petit programme sympa qui utilise l'API de WhatsApp pour nous aider à garder notre groupe propre et agréable. Il peut détecter automatiquement le spam, les pubs et même les utilisateurs qui ne respectent pas les règles.

---

# Bot de Modération pour Groupe WhatsApp de Cybersécurité HASHCODE SECURITY

Ce projet est un bot de modération développé en Python pour le groupe WhatsApp de cybersécurité de la communauté HashCode Informatique. Le bot vise à maintenir un environnement sûr et respectueux en détectant et en modérant les comportements indésirables tels que le spam et la publicité non autorisée.

## Fonctionnalités

- **Détection de spam et de publicité** : Analyse des messages pour détecter les spammeurs et les personnes faisant de la publicité non autorisée, utilisant des filtres de mots-clés, de fréquence de messages, ou d'autres critères.
- **Bannissement automatique des utilisateurs** : Identification et bannissement automatique des utilisateurs enfreignant les règles du groupe.
- **Avertissements et sanctions progressives** : Envoi d'avertissements pour comportements indésirables légers, avec sanctions croissantes en cas de récidive.
- **Gestion des demandes de modération** : Les membres peuvent signaler des messages ou des utilisateurs pour examen, et les administrateurs peuvent prendre des mesures.
- **Personnalisation des règles de modération** : Paramètres configurables pour ajuster la détection et les actions de modération selon les besoins du groupe.
- **Journalisation des actions de modération** : Enregistrement des actions de modération pour des raisons de transparence et de responsabilité.
- **Gestion des demandes d'assistance** : Réponse aux demandes d'assistance des membres concernant les règles de modération et les sanctions.
- **Rapports de statistiques** : Génération de rapports sur l'activité de modération (avertissements, bannissements, etc.).
- **Interaction avec les administrateurs** : Notification aux administrateurs des activités de modération nécessitant une intervention manuelle.
- **Système d'apprentissage automatique pour l'amélioration continue** : Utilisation de techniques d'apprentissage automatique pour améliorer la détection des comportements indésirables.

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/Eurin-lumen/WhatsAppAIModerateur.git
   ```

2. **Installer les dépendances** :
   ```bash
   cd WhatsAppAIModerateur
   pip install -r requirements.txt
   ```

3. **Configurer les paramètres** :
   - Renommer `config.example.py` en `config.py` et renseigner les informations nécessaires.

4. **Lancer le bot** :
   ```bash
   python bot.py
   ```

## Contribution

Les contributions à ce projet sont les bienvenues ! Suivez ces étapes pour contribuer :

1. **Forker le projet** : Allez sur la [page GitHub du projet](https://github.com/Eurin-lumen/WhatsAppAIModerateur) et cliquez sur le bouton "Fork" en haut à droite pour créer une copie du dépôt dans votre compte GitHub.
   
2. **Cloner votre fork** :
   ```bash
   git clone https://github.com/<VotreNomUtilisateurGitHub>/WhatsAppAIModerateur.git
   ```

3. **Créer une nouvelle branche** pour votre fonctionnalité ou correction de bug :
   ```bash
   git checkout -b feature/NouvelleFonctionnalite
   ```

4. **Effectuer vos modifications** et les committer :
   ```bash
   git commit -am "Ajouter une nouvelle fonctionnalité"
   ```

5. **Pusher la branche** vers votre dépôt forké :
   ```bash
   git push origin feature/NouvelleFonctionnalite
   ```

6. **Soumettre une Pull Request** : Une fois les modifications poussées, allez sur la page GitHub du projet d'origine et soumettez une Pull Request depuis votre dépôt forké.

### Ajouter votre nom en tant que contributeur

Pour ajouter votre nom à la liste des contributeurs, veuillez ajouter votre nom dans la section **Auteurs** en suivant le format ci-dessous. N'oubliez pas de créer une Pull Request une fois que vos modifications sont prêtes.

```markdown
## Auteurs

- [Nom du Contributeur 1](https://github.com/nomutilisateur)
- [Nom du Contributeur 2](https://github.com/nomutilisateur)
- HashCode Security
```

## Auteurs

- HashCode Security
- [Ajouter votre nom ici en tant que contributeur !](https://github.com)

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
