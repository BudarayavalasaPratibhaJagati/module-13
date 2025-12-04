# Module 13 – FastAPI JWT Auth + Front-End + Playwright + CI/CD

This project extends the earlier **fast-api-calci** app with:

- JWT-based user registration and login
- Simple front-end pages for register and login
- Playwright end-to-end tests (positive + negative paths)
- GitHub Actions CI pipeline that runs tests and builds/pushes a Docker image

---

## Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy, Pydantic
- **Auth:** `passlib[bcrypt]` password hashing, `python-jose[cryptography]` JWT
- **Front-end:** Plain HTML + vanilla JavaScript (served by FastAPI from `/static`)
- **Testing:** Playwright (JavaScript end-to-end tests)
- **CI/CD:** GitHub Actions, Docker, Docker Hub

---

## Project Structure

Important files and folders:

```text
app/
  main.py               # FastAPI app entrypoint
  models.py             # SQLAlchemy models (User, Calculation, etc.)
  schemas.py            # Pydantic models (UserCreate, UserRead, Token, etc.)
  database.py           # DB engine and SessionLocal
  security.py           # Password hashing + JWT helpers
  routers/
    users.py            # /register and /login routes
static/
  register.html         # Registration form + client-side validation
  login.html            # Login form + client-side validation
tests/
  e2e-auth.spec.js      # Playwright E2E tests for register/login
.github/
  workflows/ci.yml      # CI: run server + Playwright + Docker build/push
Dockerfile              # Container image for the FastAPI app
requirements.txt        # Python dependencies
package.json            # Playwright + npm scripts
