# Community Events Platform

A **production-ready, full-stack Django application** that enables communities to create, manage, and participate in events.
The project is designed to demonstrate **real-world backend engineering practices** such as authentication, authorization, caching, scalable API design, and clean architecture.

🌐 **Live Demo:**
👉 [https://communityeventsplatform-qh9p.onrender.com/](https://communityeventsplatform-qh9p.onrender.com/)

---

## 🚀 Key Features

### 🔐 Authentication & Registration

* Secure **user registration and login**
* JWT-based authentication for API access
* Role-aware access control (organizers vs participants)

### 📅 Event Management

* Create, update, and delete events
* Browse and filter upcoming events
* View detailed event information
* Participate in events as a registered user

### 👤 User Profiles

* View and manage user-specific data
* Ownership-based access restrictions

### 🔌 RESTful API

* Clean, well-structured REST APIs built using **Django REST Framework**
* Browsable API interface for development and testing

### ⚡ Performance & Scalability

* Custom caching layer for read-heavy endpoints
* Signal-based cache invalidation to maintain data consistency
* Pagination and filtering for large datasets

---

## 🏗️ Architectural Highlights

This project focuses on **clean backend architecture and scalability**, following Django and REST best practices.

* **Decoupled API Design**
  The backend is exposed via REST APIs using **Django REST Framework**, allowing easy integration with different frontends or mobile clients.

* **Custom Caching Framework**
  A reusable caching mixin (`core.cache.CacheMixin`) is implemented to improve performance for frequently accessed endpoints.

* **Signal-Based Cache Invalidation**
  Django signals (`events.signals`, `users.signals`) automatically invalidate cached data when underlying models change, ensuring freshness without manual intervention.

* **Custom Permissions & Filtering**
  DRF permissions and filters are extended (`apis.events.permissions`, `apis.events.filters`) to provide fine-grained access control and flexible querying.

* **Modular Project Structure**
  The application is organized into logical Django apps:

  * `users`
  * `events`
  * `apis`
  * `frontend`
    This promotes maintainability and long-term scalability.

---

## 🧩 High-Level Architecture

```
Frontend (Django Templates / JS)
        ↓
Django REST Framework APIs
        ↓
Authentication & Permission Layer (JWT)
        ↓
PostgreSQL Database
        ↓
Redis Cache (read-heavy endpoints)
```

---

## 🛠️ Technical Stack

* **Backend:** Python 3.11, Django 5, Django REST Framework
* **Frontend:** HTML5, CSS3, JavaScript (Django Templates)
* **Database:** PostgreSQL (production), SQLite (development)
* **Caching:** Redis (via django-redis)
* **Deployment:** Dockerized and deployed on **Render**
* **Testing:** Django built-in test framework
* **Package Management:** `pip` / `uv`

---

## 📦 Deployment

The application is containerized using **Docker** and deployed on **Render**.

### Deployment Highlights

* Dockerized Django backend with **Gunicorn**
* Environment-based configuration (no secrets in code)
* Managed PostgreSQL database in production
* Static files collected at build time
* HTTPS-enabled public deployment

This setup can be easily adapted to platforms like **Google Cloud Run** or **AWS**.

---

## 🧑‍💻 Getting Started (Local Setup)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/rajandevstudio/CommunityEventsPlatform.git
cd CommunityEventsPlatform
```

---

### 2️⃣ Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Or using `uv`:

```bash
uv sync
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Apply database migrations

```bash
python manage.py migrate
```

---

### 5️⃣ Create a superuser (admin access)

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

Access the app at:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔗 API Endpoints

The API is accessible via the DRF interface at `/api/`.

### Authentication

* `api/auth/register/` → User registration
* `api/auth/login/` → User login

### Events

* `api/events/` → List & create events
* `api/events/<id>/` → Retrieve, update, delete event

### Users

* `api/users/` → List users
* `api/users/<id>/` → Retrieve user details

---

## 🧪 Running Tests

Run the test suite using:

```bash
python manage.py test
```

---

## 🔮 Future Improvements

* Background jobs for notifications (Celery + Redis)
* API rate limiting for public endpoints
* Structured logging and monitoring
* Improved frontend UX

---

## 🎯 Purpose of This Project

This project was built to demonstrate **practical backend engineering skills**, including:

* Secure authentication & authorization
* API design and scalability
* Performance optimization through caching
* Clean, maintainable Django architecture
* Real-world deployment practices

---
