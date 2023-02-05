CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE discussion_zones (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  discussion_zone_id INTEGER REFERENCES discussion_zones (id),
  name VARCHAR(255) NOT NULL
);

CREATE TABLE topics (
  id SERIAL PRIMARY KEY,
  category_id INTEGER REFERENCES categories (id),
  user_id INTEGER REFERENCES users (id),
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE replies (
  id SERIAL PRIMARY KEY,
  topic_id INTEGER REFERENCES topics (id),
  user_id INTEGER REFERENCES users (id),
  content TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);