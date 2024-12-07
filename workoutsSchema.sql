CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_type TEXT NOT NULL,
    distance REAL NOT NULL,
    calories REAL NOT NULL,
    time REAL NOT NULL
);
