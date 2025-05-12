
# Hello World API (Python + Flask)

A simple RESTful API built with Python and Flask that demonstrates basic CRUD (Create, Read, Update, Delete) operations on a greeting message.

---

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [File Structure](#file-structure)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Production Deployment](#production-deployment)
- [Logging](#logging)
- [License](#license)

---

## Features

- Simple REST API with CRUD operations
- In-memory storage for a greeting message
- JSON request/response format
- Console logging for all CRUD actions
- Easy to extend for learning or prototyping

---

## How It Works

- **Import Flask module:**  
  Loads the Flask library for building the API.

- **Create Flask app:**  
  Initializes a Flask application.

- **Initialize greeting variable:**  
  Stores the greeting message in memory.

- **CREATE endpoint (`POST /hello`):**  
  - Receives a new greeting in the request body.
  - Sets the `greeting` variable to the provided value or defaults to "Hello, World!".
  - Logs the created greeting.
  - Responds with status 201 and the new greeting.

- **READ endpoint (`GET /hello`):**  
  - Returns the current value of the `greeting` variable as JSON.
  - Logs the greeting read action.

- **UPDATE endpoint (`PUT /hello`):**  
  - Receives an updated greeting in the request body.
  - Stores the old greeting for logging.
  - Updates the `greeting` variable to the new value (or keeps the old one if not provided).
  - Logs the old and new greetings.
  - Responds with a message and the updated greeting.

- **DELETE endpoint (`DELETE /hello`):**  
  - Logs the current greeting before deletion.
  - Sets the `greeting` variable to an empty string.
  - Logs that the greeting was deleted.
  - Responds with a message confirming deletion.

- **Start the server:**  
  - Runs the Flask development server on port 5000 by default.

---

## File Structure

```hello-world-api/
├── app.py         # Main API server file
├── requirements.txt # Python dependencies (optional)
└── README.md      # Project documentation
```

---

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/hello-world-api.git
   cd hello-world-api
   ```

2. **(Optional) Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install flask
   ```

4. **Start the server:**

   ```bash
     python app.py
   ```

5. **The API will be running at:**  
   [http://localhost:5000/hello](http://localhost:5000/hello)

---

## API Endpoints

| Method | Endpoint    | Description                  | Request Body Example           |
|--------|-------------|------------------------------|-------------------------------|
| POST   | `/hello`    | Create/set a greeting        | `{ "greeting": "Hi there!" }` |
| GET    | `/hello`    | Read the current greeting    | _none_                        |
| PUT    | `/hello`    | Update the greeting          | `{ "greeting": "Hello, API!"}`|
| DELETE | `/hello`    | Delete the greeting          | _none_                        |

---

## Usage Examples

**Create a greeting:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"greeting":"Hi there!"}' http://localhost:5000/hello
```

**Read the greeting:**

```bash
curl http://localhost:5000/hello
```

**Update the greeting:**

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"greeting":"Hello, API!"}' http://localhost:5000/hello
```

**Delete the greeting:**

```bash
curl -X DELETE http://localhost:5000/hello
```

---

## Production Deployment

- **Do not use the Flask development server in production.**
- Use a WSGI server like **Waitress** (Windows) or **Gunicorn** (Linux/macOS):

**Waitress (Windows):**

```bash
pip install waitress
waitress-serve --listen=0.0.0.0:5000 app:app
```

**Gunicorn (Linux/macOS):**

```bash
pip install gunicorn
gunicorn app:app
```

---

## Logging

- All CRUD actions log relevant data to the console using Flask's logger.

---

## License

MIT License

---

**Happy coding!**
