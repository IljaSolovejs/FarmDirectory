# CSC1025 – 2026 Group Project
## Project 1 – Group A123

## Project Title
**Farm & Product Directory**

## Project Description
This project is a Django-based web application developed as part of the CSC1025 module. The website focuses on **Food Systems and Agriculture**, allowing users to explore farms and their associated agricultural products in a structured directory format.

Users can:
- Browse farms
- View product details
- Add new products
- Filter products by organic status

The project demonstrates the use of:
- Django models
- Views
- Templates
- URL routing
- Database relationships

The team also applied:
- Agile project management using Trello
- Version control using GitLab

## Project Team Members
**P1 – Vasileios Papakostas**  
vasileios.papakostas2@mail.dcu.ie  
**P2 – Ilja Solovejs**  
ilja.solovejs2@mail.dcu.ie  
**P3 – Denys Maksymov**  
denys.maksymov2@mail.dcu.ie  
**P4 – Danylo Dudar**  
danylo.dudar2@mail.dcu.ie

## Development Workflow
- Main development branch: dev
- Feature branches created from dev
- Final version merged into main

## Hidden Feature: Farm Plot Calculator
Visit a URL in the format `/<length>/<width>/<yield>/` to access the Farm Plot Calculator.

- **length** - plot length in metres (positive integer)
- **width** - plot width in metres (positive integer)
- **yield** - estimated crop yield in kg per m² (positive integer)

Example: `http://127.0.0.1:8000/10/5/3/`

This will calculate the total plot area and estimated harvest, and suggest a suitable crop based on the yield rate.