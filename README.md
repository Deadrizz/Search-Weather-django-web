# Search-Weather-django-web

A simple Django application for searching and displaying weather by city. The repository contains a working project with two apps: `searchweather` (weather logic) and `users` (registration/login/logout), as well as the project configuration `weather_django`.

## Repository Structure

```
Search-Weather-django-web/
├─ manage.py
├─ db.sqlite3
├─ weather_django/      # project settings and URLs
├─ searchweather/       # logic for fetching and displaying weather
├─ users/               # authentication (registration/login/logout)
└─ static/
   └─ css/
```

## Requirements

* Python 3.x
* Django (version specified in your environment)
* (If an external weather API is used, you may need an HTTP client such as `requests`.)

## Running Locally

```bash
# 1) Clone the repository
git clone https://github.com/Deadrizz/Search-Weather-django-web.git
cd Search-Weather-django-web

# 2) Create a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

# 3) Install dependencies
pip install django
# if needed:
# pip install requests

# 4) Apply migrations and run the server
python manage.py migrate
python manage.py runserver
```

Open in your browser: `http://127.0.0.1:8000/`.

## Usage

* On the main page, enter a city name to search for weather.
* Registration/login/logout pages are implemented in the `users` app.

## Routes

Project routes are defined in `weather_django/urls.py`, while app-specific routes are inside the respective app directories (`searchweather`, `users`).

## Static Files

CSS files are located in `static/css/`.

---

