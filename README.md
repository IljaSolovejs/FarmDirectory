# FarmDirectory

A Django web application for exploring local farms and their agricultural products. Users can browse farms, view each farm's products, add new products and filter by organic status.

Built as a 4-person university group project at Dublin City University.

**Tech stack:** Python | Django | HTML | CSS | SQLite | Git | Trello

## Features
- **Farm directory:** browse all farms, each with its own detail page
- **Product listings:** see the products sold by each farm
- **Add products:** form-based product creation linked to a farm
- **Organic filter:** filter products by organic status
- **Dynamic home page:** live farm and product counts pulled from the database
- **Farm Plot Calculator (hidden feature):** visit `/<length>/<width>/<yield>/` (e.g. `/10/5/3/`) to calculate plot area and estimated harvest, with a suggested crop based on yield

## My Role – Views & Logic
- Wrote the view functions in `views.py` and the URL patterns for the farm and product detail pages
- Built the home page with live farm and product counts from the database
- Owned the team's Trello board and organised sprint tasks
- Tested the site and recorded the project screencast

## Design
- **Card layout** for quick scanning of farms and products
- **Persistent navigation** across all pages
- **Earthy green/brown palette** to fit the agriculture theme

## Team Workflow
- Agile planning with a Trello board (backlog -> sprint -> doing -> done)
- Git branching: feature branches -> `dev` -> protected `main`, integrated through merge requests

## Run Locally
```bash
pip install django
python manage.py migrate
python manage.py runserver
```
Then open http://127.0.0.1:8000

## Team
Vasileios Papakostas (models & database) | Ilja Solovejs (views & logic) | Danylo Dudar (URLs & navigation) | Denys Maksymov (templates & CSS)
