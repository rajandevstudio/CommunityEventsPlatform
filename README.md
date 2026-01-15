# Community Events Platform

A full-stack Django application designed for communities to organize and manage events. This platform provides a centralized space for organizers to post events and for community members to discover, sign up for, and participate in them.


**Live Demo:** [Link to your live application] *(TBD)*

## Key Features

*   **User Authentication:** Secure user registration and login.
*   **Event Management:**
    *   Create, update, and delete events.
    *   Browse and filter upcoming events.
    *   View detailed event information.
*   **User Profiles:** View and manage user-specific information.
*   **RESTful API:** A well-defined API for interacting with events and users, built with Django REST Framework.
*   **Scalable Architecture:** Designed with performance and scalability in mind, featuring a custom caching layer.

## Architectural Highlights

This project emphasizes a clean and scalable architecture, drawing from best practices in Django development.

*   **Decoupled API:** The backend is exposed via a RESTful API built with **Django REST Framework (DRF)**, allowing for a decoupled frontend or mobile application in the future.
*   **Custom Caching Framework:** A custom caching mixin (`core.cache.CacheMixin`) is implemented to significantly improve performance for read-heavy operations.
*   **Signal-based Cache Invalidation:** Django signals are used (`events.signals`, `users.signals`) to automatically invalidate cached data upon database modifications (e.g., when an event is updated). This ensures data consistency while maintaining performance.
*   **Custom Permissions & Filtering:** DRF's permission and filtering systems are extended to provide granular control over API access and querying (`apis.events.permissions`, `apis.events.filters`).
*   **Organized Project Structure:** The project is organized into logical Django apps (`users`, `events`, `apis`, `frontend`) to promote modularity and maintainability.

## Technical Stack

*   **Backend:** Python, Django, Django REST Framework
*   **Frontend:** HTML5, CSS3, JavaScript (rendered via Django Templates)
*   **Database:** PostgreSQL (production), SQLite3 (development)
*   **Deployment:** Configured for deployment on Render (`render.yaml`).
*   **Testing:** Unit tests using Django's built-in test framework.
*   **Package Management:** `uv` / `pip`

## Getting Started

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd CommunityEventsPlatform
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

## API Endpoints

The API is browsable via DRF's interface at `/api/`. Key endpoints include:

*   `api/auth/login/`: User login.
*   `api/events/`: List and create events.
*   `api/events/<id>/`: Retrieve, update, or delete a specific event.
*   `api/users/`: List users.
*   `api/users/<id>/`: Retrieve a specific user's details.

## Running Tests

To run the test suite, use the following command:

```bash
python manage.py test
```