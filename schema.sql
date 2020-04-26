DROP TABLE IF EXISTS employees ;

CREATE TABLE employees (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  surname TEXT UNIQUE NOT NULL,
  age INTEGER NOT NULL,
  telephone TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  link_social TEXT,
  profession TEXT NOT NULL,
  education INTEGER NOT NULL,
  main_skill TEXT NOT NULL,
  address TEXT NOT NULL,
  previous_job TEXT NOT NULL,
  other_info TEXT,
  readiness INTEGER,
  help TEXT,
  password TEXT NOT NULL
);