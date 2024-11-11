
# 3IVIS GDP Data Visualization App

This project is a web application developed for a task at 3ivis, featuring an interactive data visualization tool for displaying historical GDP data. The application uses Django and Django REST Framework for the backend, along with D3.js for dynamic chart rendering on the frontend.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [Usage](#usage)
  - [API Authentication](#api-authentication)
  - [Accessing the Chart Data API](#accessing-the-chart-data-api)
  - [Web Pages](#web-pages)
- [Basic Commands](#basic-commands)
- [Technical Stack](#technical-stack)
- [Screenshots](#screenshots)
- [Deployment](#deployment)
- [License](#license)

---

## Project Overview

This application allows users to view historical GDP data interactively and provides an API for developers to retrieve the data. Access to the data and chart is restricted to authenticated users only, aligning with secure data practices.

## Features

- **Interactive Chart**: Visualize GDP data with a D3.js-based line chart.
- **RESTful API**: Retrieve chart data securely using a token-based authentication system.
- **Authentication**: Only authenticated users can access the chart and data API.
- **User-Friendly Interface**: A clean and responsive UI built with Bootstrap.

## Getting Started

### Prerequisites

- **Python 3.x**: Make sure Python is installed on your system. You can download it from [Python's website](https://www.python.org/downloads/).
- **pip**: Python package installer, which comes with Python.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/3ivis-gdp-visualization.git
   cd 3ivis-gdp-visualization
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` File** (Optional but recommended for sensitive information)

   Create a `.env` file in the root directory to store environment variables, such as secret keys.

   ```txt
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ```

5. **Set Up the Database**

   Run migrations to set up the database schema:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser** (for accessing the admin panel and generating tokens)

   ```bash
   python manage.py createsuperuser
   ```

### Running the Project

1. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

2. **Access the Application** in your web browser at `http://127.0.0.1:8000/`

---

## Usage

### API Authentication

To access the API, you need an API token:

1. **Login to the Admin Panel** at `http://127.0.0.1:8000/admin/`.
2. **Generate a Token** for your user by navigating to the **Tokens** section and creating one.

Alternatively, you can obtain a token via the API by sending a POST request with your username and password to `/api/auth/`.

Example request using `curl`:

```bash
curl -X POST -d "username=yourusername&password=yourpassword" http://127.0.0.1:8000/api/auth/
```

### Accessing the Chart Data API

With your token, you can access the chart data API at `/api/chart-data/` by including the token in your request headers.

Example request using `curl`:

```bash
curl -H "Authorization: Token your_token_here" http://127.0.0.1:8000/api/chart-data/
```

### Web Pages

- **Home Page**: A welcoming page introducing the application. Accessible at `http://127.0.0.1:8000/`.
- **About Page**: Information about the project and its purpose. Accessible at `http://127.0.0.1:8000/about/`.
- **Chart Page**: An interactive D3.js chart displaying GDP data. Only accessible to logged-in users at `http://127.0.0.1:8000/chart/`.

---

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on one browser (e.g., Chrome) and your superuser logged in on another (e.g., Firefox) to test user permissions.

### Type Checks

To run type checks with mypy:

```bash
$ mypy ivis_task
```

### Test Coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```bash
$ coverage run -m pytest
$ coverage html
$ open htmlcov/index.html
```

#### Running tests with pytest

```bash
$ pytest
```

### Live Reloading and Sass CSS Compilation

For live reloading and SASS compilation, refer to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/2-local-development/developing-locally.html#using-webpack-or-gulp).

---

## Technical Stack

- **Django**: Web framework used for backend logic and serving API endpoints.
- **Django REST Framework**: Provides the API endpoints and token-based authentication.
- **D3.js**: JavaScript library used for interactive data visualization.
- **Bootstrap**: CSS framework used for responsive and attractive design.

## Screenshots

### Home Page
![Home Page](path/to/home_page_screenshot.png)

### About Page
![About Page](path/to/about_page_screenshot.png)

### Chart Page (Authenticated)
![Chart Page](path/to/chart_page_screenshot.png)

---

## Deployment

For deployment instructions, please follow the steps provided in the documentation.

---

## License

This project is licensed under the MIT License.
