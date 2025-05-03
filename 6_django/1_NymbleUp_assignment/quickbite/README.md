# 🍟 QuickBite POS - Django REST Backend

QuickBite POS is a backend system built using Django & Django REST Framework

---

## Tech Stack

- **Framework:** Django + Django REST Framework
- **Database:** SQLite (can be switched to PostgreSQL/MySQL)

---

## 🚀 Core Features

- Menu Listing
- Place Orders
- Update Order Status
- View Orders
- Daily Sales Analysis (last 4 days)

---

## 🌐 API Endpoints

Endpoint - Method - Description

`/api/menu/` - GET - List all available menu items
`/api/orders/place/` - POST - Place a new order
`/api/orders/` - GET - List all orders
`/api/orders/<id>/update-status/` - PUT - Update order status
`/api/sales/average/` - GET - Get average daily sales
