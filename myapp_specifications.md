# 1. Application Web : LUME - Plateforme Sociale d’Articles, Commentaires et Tags

## 1. Contexte et Objectifs

Les plateformes modernes de contenu doivent non seulement permettre aux utilisateurs de publier des articles, mais aussi de favoriser les échanges, les interactions et la personnalisation de l’expérience utilisateur. Le projet **LUME** vise à créer une application web interactive qui permet aux utilisateurs d’écrire des articles, commenter, suivre des sujets via des tags, et gérer leur profil dans une interface moderne et animée.

## 2. Périmètre du Projet

- L’application doit permettre :
  - La gestion des utilisateurs (inscription, profil, équipe).
  - La création et gestion des articles.
  - Le système de commentaires et de likes.
  - L’organisation des contenus par tags.
  - Un système d’accueil dynamique et professionnel.
  - L'intégration future de fonctionnalités IA (résumé d’articles, suggestions personnalisées...).

## 3. Spécifications Fonctionnelles

### 3.1 Gestion des Utilisateurs

- Inscription, authentification, déconnexion.
- Création de profil utilisateur avec avatar et bio.
- Visualisation de son propre profil et de celui des autres.
- Rôles : Utilisateur / Administrateur.

### 3.2 Gestion des Articles

- CRUD des articles.
- Éditeur markdown ou enrichi (titre, contenu, image).
- Attribution automatique à l’auteur connecté.
- Tri par date, popularité ou tags.

### 3.3 Commentaires et Interactions

- Système de commentaires sous chaque article.
- Possibilité de supprimer ou modifier ses commentaires.
- Système de likes sur articles et commentaires.

### 3.4 Tags et Navigation Thématique

- Ajout de tags lors de la publication d’un article.
- Consultation des articles par tag.
- Affichage de tags populaires.

### 3.5 Accueil et Navigation

- Landing page animée avec sections :
  - Héros avec call-to-action.
  - Fonctionnalités principales.
  - Section "À propos".
  - Présentation de l’équipe : **Youssef**, **Wizli**, **Salim**, **Ilias**.
- Design responsive et animations avec Tailwind CSS.

### 3.6 Notifications et Historique (à venir)

- Notification des réponses à ses commentaires.
- Historique des articles publiés.
- Système de messagerie privée (futur).

## 4. Gestion des Utilisateurs

- **Utilisateurs** : rédigent, interagissent, personnalisent leur profil.
- **Admins** : modèrent, gèrent les utilisateurs et les contenus.

## 5. Parcours Utilisateur

### Utilisateur :

1. Atterrit sur la page d’accueil animée.
2. S’inscrit ou se connecte.
3. Accède à son profil et commence à publier.
4. Lit, like, commente des articles.
5. Découvre du contenu par tags.

### Administrateur :

1. Gère les utilisateurs via le panel admin.
2. Supprime les contenus inappropriés.
3. Analyse l’activité des utilisateurs.

## 6. Contraintes Techniques

- **Backend** : Django, Django REST Framework.
- **Frontend** : Tailwind CSS, JavaScript, HTMX .
- **Base de données** : PostgreSQL.
- **Authentification** : Django Allauth.
- **Intégration IA prévue** : résumés automatiques, suggestion d’articles, détection de spam, amélioration de contenu.
