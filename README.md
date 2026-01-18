# FlowTrack Backend

## Overview

FlowTrack is a **production-style workflow and project management backend** built with Django and Django REST Framework. It is designed to simulate how internal tooling works in real companies: authenticated users manage their own projects, workflows, and tasks with **strict data isolation, JWT authentication, and permission enforcement**.

This project was built as part of an intensive backend engineering challenge with the goal of reaching **intermediate-level Django proficiency** and producing a **portfolio-ready system** that reflects real-world practices rather than tutorials.

---

## Key Features

*  **JWT Authentication** (token-based, stateless)
*  **User-scoped data access** (users can only see their own data)
*  **Permission-by-queryset security model** (unauthorized data is hidden)
*  **Projects, Workflows, and Tasks domain model**
*  **Admin interface for internal management**
*  **Scalable architecture ready for frontend integration**

---

## Tech Stack

* **Backend Framework:** Django
* **API Layer:** Django REST Framework (DRF)
* **Authentication:** JWT (SimpleJWT)
* **Database:** SQLite (dev) → PostgreSQL-ready
* **API Security:** DRF permissions + queryset filtering
* **Version Control:** Git + GitHub

---

## Architecture (High-Level)

**Client (React / API Consumer)**
→ Sends authenticated HTTP requests with JWT token
→ **Django REST API**
→ ViewSets enforce authentication & permissions
→ Querysets filter data by logged-in user
→ Database stores projects, workflows, tasks

This ensures **no user can ever access another user’s data**, even if they guess IDs.

---

## Authentication & Security Model

### Authentication

* Users authenticate using **JWT tokens**
* Access tokens are sent via `Authorization: Bearer <token>` header
* No session-based authentication (API-first design)

### Authorization Strategy

Instead of returning `403 Forbidden`, FlowTrack uses a **security-by-obscurity queryset model**:

* Users only query data they own
* If a user attempts to access another user’s object:

  * The object is **not included in the queryset**
  * Django returns **404 Not Found**

This prevents attackers from learning whether private resources exist.

---

## Permission System (Verified)

The permission system was tested end-to-end:

* ✅ User A can access their own project
* ❌ User B cannot view, edit, or delete User A’s project
* ❌ Unauthorized access returns `404 Not Found`
* ✅ Users can create and manage their own projects independently

This mirrors how **financial and enterprise systems** protect internal data.

---

## Core Domain Models

### Project

Represents a user-owned project.

* Owner (User)
* Name
* Description
* Created / Updated timestamps

### Workflow

Represents a workflow belonging to a project.

* Linked to Project
* Name
* Status

### Task

Represents an actionable task inside a workflow.

* Linked to Workflow
* Title
* Status
* Priority

---

## Admin Panel

FlowTrack includes Django Admin for internal management:

* Manage users
* Create/edit projects
* Assign workflows and tasks
* Useful for internal tooling and support teams

---

## API Design Principles

* RESTful endpoints
* Consistent status codes
* Clean separation of concerns
* ViewSets + serializers
* Permission logic handled server-side

Example endpoint structure:

* `/api/auth/login/`
* `/api/projects/`
* `/api/projects/{id}/`
* `/api/workflows/`
* `/api/tasks/`

---

## Why This Project Matters

This project demonstrates:

* Real-world Django patterns
* Secure multi-user architecture
* Clean backend design
* Readiness for frontend integration
* Understanding beyond CRUD tutorials

It is intentionally designed to reflect **how internal company tools are built**, not demo apps.

---

## Next Steps (Planned)

  React frontend (dashboard, auth, protected routes)
  Filtering, search, and ordering
  Background jobs (async processing)
  Automated tests
  Dockerized deployment

---

## Author

**Oscar Masiyiwa**
Backend-focused Python & Django Developer

---

> FlowTrack is a learning-driven but production-minded system built to demonstrate real backend engineering capability.

