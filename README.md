# Flask SQLAlchemy Foundations - Earthquake Data Lab

This lab demonstrates how to use Flask and SQLAlchemy to define data models, set up database migrations, seed a SQLite database, and expose data through API endpoints. The project focuses on querying historical earthquake data.

---

## 📁 Project Structure

```
server/
├── app.py                  # Main Flask application
├── models.py               # SQLAlchemy models
├── seed.py                 # Optional: database seeding script
├── migrations/             # Alembic migration files
├── instance/
│   └── app.db              # SQLite database (auto-created)
├── testing/
│   ├── app_earthquake_test.py
│   ├── app_magnitude_test.py
│   └── models_test.py      # Test suite
├── README.md
└── ...
```

---

## 🧱 Model Definition

```python
class Earthquake(db.Model):
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pipenv install
pipenv shell
```

### 2. Set up the database

```bash
flask db init       # (only once)
flask db migrate -m "Initial migration"
flask db upgrade
```

### 3. Seed the database

If your project includes a `seed.py` or built-in seeding logic, run it:

```bash
python seed.py
```

Or manually insert data via SQLite:

```bash
sqlite3 instance/app.db
> INSERT INTO earthquakes (magnitude, location, year) VALUES (9.5, 'Chile', 1960);
> .quit
```

---

## 📡 Available Endpoints

### `GET /`

Returns a simple test message to confirm the server is running.

#### Response:

```json
{
  "message": "Flask SQLAlchemy Lab 1"
}
```

---

### `GET /earthquakes/<int:id>`

Fetch a single earthquake by ID.

#### Example:

```bash
GET /earthquakes/1
```

#### Response:

```json
{
  "id": 1,
  "location": "Chile",
  "magnitude": 9.5,
  "year": 1960
}
```

Returns 404 if no matching record is found.

---

### `GET /earthquakes/magnitude/<float:magnitude>`

Return all earthquakes with magnitude greater than or equal to the provided value.

#### Example:

```bash
GET /earthquakes/magnitude/8.5
```

#### Response:

```json
{
  "count": 3,
  "quakes": [
    {
      "id": 1,
      "location": "Chile",
      "magnitude": 9.5,
      "year": 1960
    },
    ...
  ]
}
```

---

## ✅ Test Coverage

The test suite includes:

- Model validation
- Route responses and data structure
- Status code checks (200/404)

Run tests with:

```bash
pytest
```

---

## 🧠 What I Learned

- How to define models using SQLAlchemy
- The relationship between model attributes and database columns
- How to perform filtering queries (e.g., `.filter_by()`, `.filter()`)
- How to return data via Flask `jsonify()`
- How to seed and inspect a SQLite database using `sqlite3`
- How to structure a Flask RESTful API

---

## 🛠 Future Improvements

- Add POST/PUT/DELETE routes to support full CRUD
- Implement pagination and sorting on list endpoints
- Add unit tests for edge cases (e.g., invalid IDs, empty queries)

---

## 📬 Contact

This lab was completed as part of a software development curriculum at Flatiron School. For questions or collaboration opportunities, feel free to reach out!
