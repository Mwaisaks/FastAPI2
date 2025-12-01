# 📘 FastAPI Project Dependencies — Explanation & Guide

This document explains the purpose of each dependency in this project, how to determine which dependencies you should add, and what you would install if using **PostgreSQL** or **Supabase**.

-----

## 📦 Installed Dependencies (What They Are For)

1.  **`fastapi`**
      * The core framework used to build the API: routing, request handling, validation, schemas, etc.
2.  **`uvicorn[standard]`**
      * The **ASGI server** that runs FastAPI.
      * `[standard]` installs optimized extras:
          * **`uvloop`** — faster event loop
          * **`httptools`** — faster HTTP
          * **`watchfiles`** — hot reload
          * **`websockets`**
3.  **`fastapi-users[sqlalchemy]`**
      * A plug-and-play **authentication system** that provides:
          * User registration and login
          * Token-based authentication (**JWT**)
          * Password hashing
          * ORM-based user database models
          * OAuth support
      * `[sqlalchemy]` means we are using **SQLAlchemy ORM** with a relational database.
      * This package also installs: `pyjwt`, `argon2-cffi` / `bcrypt`, `email-validator`, `sqlalchemy`, `python-multipart`, `greenlet`.
4.  **`sqlalchemy`**
      * The **ORM** (Object Relational Mapper) used to interact with relational databases (SQLite, PostgreSQL, MySQL, etc).
      * This is included automatically by `fastapi-users[sqlalchemy]`.
5.  **`aiosqlite`**
      * **Async driver for SQLite** databases.
      * *Use this only if your database is SQLite and your app uses async functions.*
6.  **`imagekitio`**
      * Client **SDK for ImageKit**.
      * Used for uploading, transforming, and managing images via the ImageKit API.
7.  **`python-env`**
      * A helper for loading **environment variables**.
      * **Note:** Many projects instead use **`python-dotenv`** (already included inside `uvicorn[standard]`). You may not need this package depending on your setup.

-----

## 🧠 How to Decide Which Dependencies to Add

### 1\. Start with your project requirements

Install dependencies based **ONLY on actual features**:

  * **Authentication** → `fastapi-users`
  * **Database** → `SQLAlchemy` + a database driver
  * **Image upload** → `ImageKit SDK`
  * **Background tasks** → `Celery` / `RQ`
  * **Websockets** → provided by Starlette/FastAPI
  * **Env variables** → `dotenv` package

> Every dependency should solve a real problem.

### 2\. Minimum recommended FastAPI setup

These two will appear in almost every FastAPI project:

  * `fastapi`
  * `uvicorn[standard]`

### 3\. Your database determines extra dependencies

| Database Setup | Dependencies to Add |
| :--- | :--- |
| **SQLite (async)** | `aiosqlite`, `sqlalchemy` |
| **PostgreSQL (async)** | `asyncpg`, `sqlalchemy` |
| **PostgreSQL (sync)** | `psycopg2`, `sqlalchemy` |

-----

## 🗃️ What if I was using PostgreSQL?

If switching from SQLite to PostgreSQL, you need the async driver:

```bash
uv add asyncpg
```

SQLAlchemy will automatically detect and use it.

-----

## 🗃️ What if I am using Supabase?

Supabase is built on top of **PostgreSQL**. You can use it in two different ways:

### ✔️ Option 1: Use Supabase as a PostgreSQL database (most common)

Install the PostgreSQL driver:

```bash
uv add asyncpg
```

Use **SQLAlchemy** normally — your FastAPI backend talks directly to the Supabase PostgreSQL database.

### ✔️ Option 2: Use the Supabase API SDK

Install:

```bash
uv add supabase
```

This allows access to:

  * Supabase auth API
  * Storage buckets
  * Realtime features
  * Edge function calls
  * RPC (Postgres functions)

> You can combine this with SQLAlchemy if needed, depending on your architecture.

-----

## 📌 Summary Table

| Feature | Dependency |
| :--- | :--- |
| **Core API** | `fastapi` |
| **Server** | `uvicorn[standard]` |
| **Auth system** | `fastapi-users[sqlalchemy]` |
| **ORM** | `sqlalchemy` |
| **SQLite (async)** | `aiosqlite` |
| **PostgreSQL (async)** | `asyncpg` |
| **Environment variables** | `python-env` or `python-dotenv` |
| **Images via ImageKit** | `imagekitio` |
| **Supabase API** | `supabase` |

-----

# FastAPI Docs
`url/docs` - swagger api
`url/docs` - newer one


`@app.get("/posts/{id}")` - path parameters

# Throwing Exceptions in FastAPI


# Query Parameters
comes after the question mark

# Post endpoint
schemas.py

enhancing the documentation - creating response classes

# Database Connection


