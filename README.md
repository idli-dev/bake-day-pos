# Bake-Day POS

Bake-Day is a **local, offline-first restaurant POS system** designed for small setups running on a single machine.  
It prioritizes **reliability, simplicity, and speed** over cloud-heavy complexity.

Built to handle real restaurant needs: orders, KOTs, billing, and daily summaries.

---

## Goals

- Work **offline**, always
- Run on **low-end hardware**
- Support **thermal POS printers** (ESC/POS)
- Be easy to extend with a **web UI**
- Stay simple and maintainable

---

## Tech Stack

- **FastAPI** — application and API layer
- **SQLite** — local persistence
- **ESC/POS** — thermal printer communication
- **HTML UI** — lightweight browser-based interface

No cloud dependency. No heavy frameworks.

---

## Project Structure

- `app/` — core application
  - `services/` — business logic (orders, menu, reports)
  - `api/` — FastAPI routes and dependencies
  - `ui/` — templates and static assets
  - `printer/` — bill and KOT printing
  - `db/` — schema and migrations
- `data/` — runtime data (SQLite database)
- `tests/` — automated tests
- `main.py` — application entry point

This structure cleanly separates **logic, interface, and hardware concerns**.

---

## Design Principles

- Business logic is **framework-agnostic**
- Printing is **isolated from the application**
- UI and API reuse the same services
- Database stores **facts**, not derived summaries
- Simple now, extensible later

---

## Current Scope

- Menu management
- Orders (dine-in, parcel, delivery)
- Kitchen Order Tickets (KOT)
- Bill printing
- Daily summaries

---

## Non-Goals (for now)

- Cloud hosting
- Multi-branch synchronization
- Complex authentication or role management

---

Bake-Day is intentionally boring — because **boring systems don’t break during a dinner rush**.
