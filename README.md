# FastAPI Applications API

A RESTful API for managing job applications built with FastAPI.

## Features

- Create, read, update, and delete job applications
- Filter applications by company name and candidate email
- Optional fields support in PATCH operations
- Proper error handling and status codes

## Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
cd src
uvicorn main:app --reload
```

## API Endpoints

- POST /applications - Create new application
- GET /applications - List all applications
- GET /applications/{candidate_id} - Get specific application
- PUT /applications/{candidate_id} - Update application
- PATCH /applications/{candidate_id} - Partially update application
- DELETE /applications/{candidate_id} - Delete application

## API Documentation

Once the server is running, visit:
- http://127.0.0.1:8000/docs for Swagger UI documentation
- http://127.0.0.1:8000/redoc for ReDoc documentation 