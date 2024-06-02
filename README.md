# Django || Mumbai Flood App

## Introduction

This is a full-stack system for predicting and displaying potential flood/rainfall data. The backend is built with Django, with PostgreSQL as the database. Celery with Redis is used for task scheduling to fetch and process data periodically.

## Project Structure

- **Frontend**: React (website) and React Native (mobile app)
- **Backend**: Django
- **Database**: PostgreSQL
- **Task Scheduling**: Celery with Redis

## Models

### Crowdsource
- **Purpose**: Saves data from form inputs and their location. Fetches tweets and performs NLP functions for required operations.
- **Fields**:
  - `location` (e.g., `PointField` for geolocation)
  - `data` (e.g., JSONField for form data)
  - `created_at` (DateTimeField)

### Awstations
- **Purpose**: Stores data from automated weather stations.
- **Fields**:
  - `station_id` (CharField)
  - `data` (JSONField)
  - `timestamp` (DateTimeField)

### Weatherstations
- **Purpose**: Stores data from weather stations.
- **Fields**:
  - `station_id` (CharField)
  - `data` (JSONField)
  - `timestamp` (DateTimeField)

### Blog
- **Purpose**: Blog model for posting updates and articles.
- **Fields**:
  - `title` (CharField)
  - `content` (TextField)
  - `created_at` (DateTimeField)

## Celery Tasks

### Schedule 1: Every 15 Minutes
- **Task**: Fetch data from stations and store the time series. Update required variables.

### Schedule 2: Once a Day
- **Task**: Fetch GFS data and use the model to forecast rainfall.

## Setup and Installation

### Prerequisites
- Python 3.x
- Django
- PostgreSQL
- Redis
- Celery
