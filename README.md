# Student Feedback App

A simple Flask web app where students submit their name, email (@niet.co.in only), course, and feedback. Submitted feedback is displayed on the same page. Includes a CI pipeline using GitHub Actions.

## Tech Stack
- Python, Flask
- Docker
- GitHub Actions (CI/CD)
- Pytest

## Project Structure
```
feedback-app/
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
└── .github/workflows/ci.yml
```

## Run Locally

```
pip install -r requirements.txt
python app.py
```
Open http://localhost:5000

## Run with Docker

```
docker build -t feedback-app .
docker run -p 5000:5000 feedback-app
```

## Run Tests

```
pytest
```

## CI/CD Pipeline

On every push to `main`, GitHub Actions:
1. Installs dependencies
2. Runs tests
3. Builds the Docker image
4. Runs the container and smoke tests it

## Notes
- Only emails ending with `@niet.co.in` are accepted.
- Feedback is stored in memory and resets when the app restarts.