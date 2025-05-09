# 1. Application Web : LUME - Plateforme Sociale d’Articles, Commentaires, IA et Profils

## 1. Contexte et Objectifs

LUME est une plateforme sociale de publication d’articles enrichie par l’intelligence artificielle. Elle permet aux utilisateurs de créer, partager et interagir avec du contenu dans une interface élégante et dynamique. L'intégration de LangChain et OpenAI permet de résumer, traduire et améliorer automatiquement les articles.

---

## 2. Périmètre du Projet

- L’application permet :
  - La gestion complète des utilisateurs avec avatars, bio, et rôles.
  - La création, édition, suppression et publication d’articles avec gestion du brouillon et de la visibilité.
  - Un système de commentaires avec réponses, likes, et suppression douce.
  - Des outils d’IA pour résumer, traduire et générer automatiquement des titres et slugs.
  - Un système de tags pour une navigation thématique intuitive.
  - Une interface d’accueil soignée, animée, et responsive.

---

## 3. Spécifications Fonctionnelles

### 3.1 Gestion des Utilisateurs (App : `persona`)

- Inscription, connexion, déconnexion via Django Allauth.
- Edition de profil (photo, bio).
- Pages profil individuelles stylisées.
- Différents rôles : utilisateur / administrateur.

### 3.2 Gestion des Articles (App : `inkwell`)

- CRUD des articles.
- Interface riche avec Tailwind, animations et effets.
- Possibilité de cacher un article (soft visibility).
- Affichage dans une grille par date, popularité (à venir).

### 3.3 Interactions (App : `echoes`)

- Système de commentaires et réponses.
- Likes sur commentaires (avec HTMX).
- Soft-delete des commentaires.
- Rechargement partiel avec HTMX.

### 3.4 Intelligence Artificielle (App : `InkFuse`)

- Résumé automatique des articles via LangChain.
- Traduction à la volée dans la langue de son choix.
- Génération de titre et slug à partir du contenu.
- Endpoints dynamiques `/ai/summarize/`, `/ai/translate/`, `/ai/suggest/`.

### 3.5 Flux Social (App : `pulse`)

- Page de feed des auteurs suivis (à venir).
- Page des articles populaires ou récents.

### 3.6 Navigation & UI

- Landing page animée avec Hero, fonctionnalités, équipe.
- Menu header réactif avec notifications (futur).
- Design responsive (mobile/tablette/desktop).

---

## 4. Parcours Utilisateur

### Utilisateur :

1. Arrive sur la landing page.
2. Crée un compte ou se connecte.
3. Accède à son profil, crée un article.
4. Explore par tags, lit et commente.
5. Utilise les outils d’IA pour améliorer ses textes.

### Administrateur :

1. Gère les utilisateurs via le panel admin.
2. Supprime les articles/commentaires problématiques.
3. Bénéficie d’un futur tableau de bord (dashboard admin).

---

## 5. Contraintes Techniques

- **Backend** : Django, Django REST Framework.
- **Frontend** : Tailwind CSS, HTMX, Alpine.js.
- **Base de données** : SQLite (dev) → MySQL (prod).
- **IA** : LangChain, OpenAI API (GPT-4 via `ChatOpenAI`).
- **Auth** : Django Allauth.
- **Gestion de projet** : Poetry, fichiers `.env`, bonne structure modulaire.

---
