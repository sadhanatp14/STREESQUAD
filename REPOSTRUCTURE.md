# Repository Structure

This file documents the top-level layout and purpose of important folders/files in this repository.

- ASSUMPTIONS.md: Project assumptions and constraints.
- DOCKER-COMPOSE.yml: Docker Compose configuration for local services.
- README.md: Project overview and quick start.

- BACKEND/: Python backend service
  - DOCKERFILE: Backend Dockerfile
  - REQUIREMENTS.TXT: Python dependencies
  - APP/
    - MAIN.py: Backend application entrypoint
    - API/
      - ROUTES.py: HTTP route handlers
      - SCHEMAS.py: Request/response schemas
    - CORE/
      - FEATUREENGINEERING.py: Feature engineering utilities
      - SCORING.py: Scoring/inference logic
      - VALIDATION.py: Input validation helpers
    - DB/
      - DATABASE.py: Database connection and helpers
    - EXPLAINABILITY/
      - SHAPEXPLAINER.py: SHAP explainability utilities
    - MODELS/: Trained model artifacts and model-related code

- FRONTEND/: Frontend application
  - APP.py: Frontend entrypoint
  - COMPONENTS/: Reusable UI components
  - DOCKERFILE/: Frontend Dockerfile(s)

- ML/: Model training and data
  - FEATUREDEFINITIONS.md: Feature definitions for training/serving
  - TRAINMODELS.py: Training scripts
  - DATA/
    - PROCESSED/: Processed datasets
    - RAW/: Raw dataset dumps
    - SYNTHETIC/: Synthetic data for testing
  - NOTEBOOKS/: Jupyter notebooks for analysis and experimentation

Notes:
- The Backend appears to be a Python service; check `BACKEND/APP/MAIN.py` to see how it is launched.
- Docker-related files are provided for containerized runs.
- If you want this file updated with run commands or more detail (e.g., env vars, endpoints), tell me and I will expand it.
