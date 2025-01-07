# Django API with WordPress Integration

This project is a Django-based web application that interacts with a WordPress site via its API to fetch and display information, such as the user's IP address.
The project is structured to make use of both WordPress and Django, where WordPress serves as a backend API for data retrieval, and Django is used to process and display this data on a frontend.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)

## Features

- Fetches and displays user IP address.
- Displays content fetched from WordPress using the WordPress REST API.
- Handles JSON responses from the WordPress API.
- Simple and clean UI displaying fetched data.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.
- **WordPress**: A content management system that serves as an API endpoint.
- **Python**: Backend programming language.
- **HTML, CSS, JavaScript**: Frontend technologies to display the data.
- **Nginx**: Web server (if deploying on production).
- **Certbot**: For SSL certificate management.

## Installation

Clone this repository to your local machine using Git:
```bash
git clone https://github.com/pardiyono21/django_api_wp.git
cd django_api_wp
```

## Installation
Create a new Python virtual environment to manage dependencies:
```bash
py -m venv env
source env/bin/activate
```

Install all necessary dependencies by running:
```bash
pip install -r requirements.txt
```

Start the Django development server:
```bash
py manage.py runserver
```
