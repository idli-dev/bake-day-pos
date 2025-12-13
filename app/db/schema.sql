PRAGMA foreign_keys = ON;

-- Creates the menu table
CREATE TABLE
  IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL,
    price INTEGER NOT NULL,
    available INTEGER DEFAULT 1
  );

CREATE TABLE
  IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    -- delivery | parcel | dine-in
    order_type TEXT NOT NULL,
    customer_name TEXT,
    phone_no TEXT,
    address TEXT,
    table_no INTEGER,
    -- 1 = open | 0 = closed
    status INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  );

CREATE TABLE
  IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    menu_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    price INTEGER NOT NULL,
    -- check if those ID's are legit
    FOREIGN KEY (order_id) REFERENCES orders (id),
    FOREIGN KEY (menu_id) REFERENCES menu (id)
  );

CREATE INDEX IF NOT EXISTS daily_index ON orders (created_at);