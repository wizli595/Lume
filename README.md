<p align="center">
  <img src="static/ink.ico" alt="LUME Logo" width="280" />
</p>

<h1 align="center">🖋️ LUME</h1>
<p align="center">
  <em>A modular, AI-powered platform for writing, discussing, and enhancing articles</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-5.2-green?style=for-the-badge&logo=django" />
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/TailwindCSS-3.4-38b2ac?style=for-the-badge&logo=tailwind-css" />
  <img src="https://img.shields.io/badge/HTMX-%23ec4899?style=for-the-badge&logo=html5" />
  <img src="https://img.shields.io/badge/Alpine.js-blueviolet?style=for-the-badge&logo=alpine.js" />
  <img src="https://img.shields.io/badge/LangChain-AI-ff6f61?style=for-the-badge&logo=openai" />
  <img src="https://img.shields.io/badge/OpenAI-GPT--4-black?style=for-the-badge&logo=openai" />
  <img src="https://img.shields.io/badge/Poetry-Dependency_Management-orange?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/MySQL-Prod-yellow?style=for-the-badge&logo=mysql" />
  <img src="https://img.shields.io/badge/SQLite-Dev-lightgrey?style=for-the-badge&logo=sqlite" />
</p>

**Lume** is a modular, AI-enhanced content platform designed to fuse the power of writing, community, and intelligence into one cohesive experience. Built with Django, LangChain, and Tailwind CSS, the platform offers writers and readers a smart, elegant, and responsive space for publishing and discussing articles.

---

## 🌠 Why "Lume"?

**Lume** (short for _illuminate_) is the name of the Django project. It represents the platform's mission to **shine light on ideas, stories, and conversations**, combining creativity and AI-powered insights to amplify content meaningfully.

---

## 🔧 Apps Overview & Naming

### 📚 `inkwell`

> ✍️ The core of article creation and publishing.

- The name comes from the classic _inkwell_ — the tool writers dipped their pens into. It reflects the timeless act of writing, now modernized with AI.
- Manages article models, forms, views (create/edit/detail/list).
- Includes LangChain-based summarization, translation, and title/slug generation.

---

### 💬 `echoes`

> 🗨️ The discussion system (comments, replies, likes).

- Named for how _comments echo the article_ — responses, reflections, and resonance from the community.
- Handles threaded comments, likes, soft deletion, and reply forms.
- Seamlessly integrated with each article via `object.comments.all`.

---

### 👤 `persona`

> 🧑 User accounts, profiles, avatars.

- “Persona” refers to the identity users present — fitting for profile editing, registration, and account management.
- Integrates Django Allauth and custom user signals.
- Includes stylized pages for login, signup, and user profile.

---

### 🧠 `InkFuse` (LangChain & AI)

> 🤖 Language enhancement tools powered by OpenAI via LangChain.

- Stylized spelling of “summarize” to keep the naming playful and distinct.
- Handles endpoints like `/ai/summarize/`, `/ai/translate/`, and `/ai/suggest/`.
- Dynamically improves content quality and engagement.

---

### 🔥 `pulse`

> 📈 Social feed and trending logic.

- “Pulse” captures the heartbeat of the community — latest posts, trending topics, and followed authors.
- Templates: `following_feed.html`, `trending_feed.html`.

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: Tailwind CSS, HTMX, Alpine.js
- **AI Integration**: LangChain, OpenAI API
- **Authentication**: Django Allauth
- **Database**: SQLite (dev), MySQL (prod)
- **Package Manager**: Poetry

---

## 📁 Project Structure

```
Lume/
├── inkwell/       # Articles
├── echoes/        # Comments system
├── persona/       # Authentication & profiles
├── InkFuse/     # LangChain + OpenAI logic
├── pulse/         # Feeds and social discovery
├── lume/          # Django project settings & root config
└── templates/     # Shared and per-app templates
```

---

## 🧠 AI Features

- ✨ **Summarize Articles**
- 🌍 **Translate Content**
- 📌 **Generate Titles & Slugs**
- 🔖 (Coming Soon) **Auto-tagging & Readability Check**

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/inkfuse.git
cd inkfuse
```

### 2. Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
# Or on Arch Linux:
sudo pacman -S poetry
```

### 3. Install Dependencies

```bash
poetry install
```

### 4. Apply Migrations

```bash
poetry run python manage.py migrate
```

### 5. Run the Server

```bash
poetry run python manage.py runserver
```

---

## 🧪 Run Tests

```bash
poetry run python manage.py test
```

---

---

## 📊 UML Diagrams

Below are the key UML diagrams representing the Lume platform's design and flow.

### 🎯 Use Case Diagram

Shows the interaction between users (Visitor, Writer, Admin) and the system, including AI services:

### ![Badge](https://img.shields.io/badge/UML-Diagram-blueviolet?logo=uml&style=flat-square) Use Case Diagram

![Use Case Diagram](/uml/usecase.png)

---

### 🧱 Class Diagram

Defines the core data models and relationships across apps like `inkwell`, `persona`, `echoes`, and `pulse`:

![Class Diagram](/uml/class.png)

<!-- ---

### ⏱️ Sequence Diagram

Illustrates the sequence of operations when a user creates an article and uses AI tools for enhancement:

![Sequence Diagram](static/uml/sequence_diagram.png) -->

---

### 🧩 Location

All UML source files (`*.puml`) and generated PNGs are stored in:

## 🤝 Contributing

We welcome contributions! Fork the repo, create a feature branch, and open a PR.

---

## 📄 License

MIT License. Do cool things with it.
