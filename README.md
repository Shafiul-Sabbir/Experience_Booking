```
# 🎫 Experience Booking API

This is a simplified **Experience Booking API**, inspired by the Bokun platform, built using **Django**, **Django REST Framework**, **Celery**, and **Redis**. It supports:

- User authentication with roles (provider, customer)
- Experience creation and availability scheduling
- Slot-based bookings with capacity control
- Concurrency-safe booking system
- Periodic cleanup of expired bookings

---

## 🌟 Features

- ✅ User Registration & Login (JWT or Session Auth)
- ✅ Provider Role: Create experiences
- ✅ Auto Slot Generation on Experience Creation using Celery task
- ✅ Book Slots as Customer with Concurrency Handling
- ✅ Celery Task for Expiring Unconfirmed Bookings
- ✅ Celery Beat for Periodic Expiry Task

---

## ⚙️ Technologies Used

- Python 3.x
- Django 4.x
- Django REST Framework
- Celery
- Redis
- SQLite (local/dev)
- Swagger / DRF-YASG (for testing and documenting API Endpoints)

---

## 🛠️ Project Setup

### 1. 🔃 Clone the Repository

```bash
git clone https://github.com/Shafiul-Sabbir/Experience_Booking.git
```

### 2. 📦 Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. 🧰 Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. 🔑 Configure Environment Variables

Create a `.env` file in the project root and add:

```env
SECRET_KEY=your_project_secret_key

```

### 5. 📂 Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. 👤 Create Superuser (optional)

```bash
python manage.py createsuperuser
```

---

## 🚀 Run the Project

### Django Development Server

```bash
python manage.py runserver
```

### Celery Worker

> ⚠️ Windows users must have to download and install 'Memurai' for supporting redis on windows.

```bash
celery -A experience_booking worker --loglevel=info --pool=solo
```

> ⚠️ Windows users must use `--pool=solo` with Celery.

### Celery Beat Scheduler

```bash
celery -A experience_booking beat --loglevel=info --pool=solo
```

---

## 📅 Periodic Task (Booking Expiry)

In `settings.py`, add the scheduled task:

```python
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'expire-pending-bookings-every-15-minutes': {
        'task': 'bookings.tasks.expire_pending_bookings',
        'schedule': crontab(minute='*/15'),
    },
}
```

This task will run every 15 minutes to cancel unconfirmed bookings.

---

## 🔗 API Endpoints (Example)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/register/` | POST | User registration |
| `/api/login/` | POST | User login |
| `/api/refresh/` | POST | User refresh |
| `/api/experiences/` | POST/GET | Create or list experiences |
| `/api/experiences/{id}` | GET | Retrieve Detail of an experience |
| `/api/bookings/` | POST | Create or list bookings |
| `/api/bookings/{id}` | DELETE | Delete a booking |

> Use Postman or Swagger for testing.

---

## 🧪 Run Tests

```bash
python manage.py test
```

---

## 📄 Folder Structure

```
experience_booking/
│
├── bookings/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
|   ├── urls.py
│   |── tasks.py  ← Celery task to expire bookings
|   |── tests.py  ← Unit tests for core logic testing of bookings
│
├── experiences/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
|   ├── urls.py
│   |── tasks.py  ← Slot generation
|   |── tests.py  ← Unit tests for core logic testing of experiences
|
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
|   ├── urls.py
|   |── tests.py  ← Unit tests for core logic testing of users
│
├── experience_booking/
│   ├── settings.py
│   ├── urls.py
│   └── celery.py
│
├── manage.py
├──README.md
└── requirements.txt
```

---

## 💡 Tips

- Always run **Celery worker and beat** in separate terminals.
- Set `timezone` in `settings.py` to your local timezone.
- If using Docker, expose Redis and use `.env` for service URLs.
- For production, turn off `DEBUG`, use secure secrets, and switch to PostgreSQL.

---

## 🧔 Author

**Sabbir**
Junior Backend Developer | Django & DevOps Enthusiast
📧 [shafiulsabbir95@gmail.com]
🔗 [https://portfolio-of-shafiul-sabbir.vercel.app/]
🔗 [https://github.com/Shafiul-Sabbir]
🔗 [https://www.linkedin.com/in/md-shafiul-azam-sabbir-1740bb227/]

---

## 📜 License

This project is licensed under the MIT License.

```

---
