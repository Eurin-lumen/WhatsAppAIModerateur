# WhatsAppAIModerateur
C'est un petit programme sympa qui utilise l'API de WhatsApp pour nous aider à garder notre groupe propre et sympa. Il peut détecter automatiquement le spam, les pubs et même les utilisateurs qui ne respectent pas les règles.

--- 

# Bot de Modération pour Groupe WhatsApp de Cybersécurité

Ce projet est un bot de modération développé en Python pour le groupe WhatsApp de cybersécurité de la communauté HashCode Informatique. Le bot vise à aider à maintenir un environnement sûr et respectueux en détectant et en modérant les comportements indésirables tels que le spam et la publicité non autorisée.

## Fonctionnalités

- **Détection de spam et de publicité** : Le bot analyse les messages pour détecter les spammeurs et les personnes faisant de la publicité non autorisée, utilisant des filtres de mots-clés, de fréquence de messages ou d'autres critères.

- **Bannissement automatique des utilisateurs** : Identification automatique des utilisateurs enfreignant les règles du groupe, avec un bannissement automatique en conséquence.

- **Avertissements et sanctions progressives** : Envoi d'avertissements aux utilisateurs en cas de comportement indésirable léger, avec une augmentation des sanctions (par exemple, bannissement temporaire puis permanent) en cas de récidive.

- **Gestion des demandes de modération** : Possibilité pour les membres du groupe de signaler des messages ou des utilisateurs pour examen par les administrateurs, avec une fonctionnalité de modération pour les administrateurs pour gérer les signalements et prendre des mesures appropriées.

- **Personnalisation des règles de modération** : Paramètres configurables pour ajuster les critères de détection et les actions de modération en fonction des besoins spécifiques du groupe.

- **Journalisation des actions de modération** : Enregistrement des actions de modération effectuées par le bot pour des raisons de transparence et de responsabilité.

- **Gestion des demandes d'assistance** : Capacité à répondre aux demandes d'assistance des membres du groupe concernant les règles de modération et les sanctions.

- **Rapports de statistiques** : Génération de rapports périodiques sur l'activité de modération, y compris le nombre d'avertissements émis, les utilisateurs bannis, etc.

- **Interaction avec les administrateurs** : Notification aux administrateurs des activités de modération importantes nécessitant une intervention manuelle.

- **Système d'apprentissage automatique pour l'amélioration continue** : Utilisation de techniques d'apprentissage automatique pour améliorer la précision de la détection des comportements indésirables au fil du temps.

## Installation

1. **Cloner le dépôt** :
   ```
   git clone https://github.com/yourusername/bot-moderation-whatsapp.git
   ```

2. **Installer les dépendances** :
   ```
   cd bot-moderation-whatsapp
   pip install -r requirements.txt
   ```

3. **Configurer les paramètres** :
   - Renommer `config.example.py` en `config.py` et renseigner les informations nécessaires.

4. **Lancer le bot** :
   ```
   python bot.py
   ```

## Contribution

Les contributions à ce projet sont les bienvenues ! Si vous souhaitez contribuer, veuillez suivre les étapes suivantes :

1. **Forker le projet**.
2. **Créer une branche** pour votre fonctionnalité (`git checkout -b feature/NouvelleFonctionnalite`).
3. **Commiter vos modifications** (`git commit -am 'Ajouter une nouvelle fonctionnalité'`).
4. **Pusher la branche** (`git push origin feature/NouvelleFonctionnalite`).
5. **Créer une nouvelle Pull Request**.

## Auteurs

- HashCode Security

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

