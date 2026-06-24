# 🎨 Toonify AI

Toonify AI is a full-stack AI-powered image transformation platform that allows users to upload images and convert them into various artistic styles such as Anime, Pencil Sketch, Oil Painting, Watercolor, Vintage, and Pop Art.

The platform provides secure user authentication, image history management, profile management, payment integration using Razorpay, and an admin dashboard for monitoring system usage.

---

# 🚀 Features

## User Features

- User Registration & Login
- Secure Authentication
- Upload Images
- Multiple Artistic Effects
- AI Anime Generation using AnimeGAN
- Download Generated Images
- Image History Tracking
- Profile Management
- Password Change Functionality
- Pay-Per-Use Payment Model
- Razorpay Payment Integration
- Payment History Tracking

---

## Admin Features

- View Total Users
- View Total Images Generated
- View Total Revenue
- Monitor Platform Usage
- User Statistics Dashboard

---

# 🖼 Supported Effects

| Effect | Type | Pricing |
|----------|----------|----------|
| Anime AI | AI-Based | Paid |
| Pencil Sketch | OpenCV | Paid |
| Oil Painting | OpenCV | Paid |
| Watercolor | OpenCV | Paid |
| Vintage | OpenCV | Paid |
| Pop Art | OpenCV | Paid |

---

# 🏗 System Architecture

```text
Frontend (Streamlit)
        │
        ▼
REST APIs (FastAPI)
        │
        ▼
Service Layer
        │
        ▼
Repository Layer
        │
        ▼
PostgreSQL Database
        │
        ▼
Image Storage
```

---

# 💻 Technology Stack

## Frontend

- Streamlit
- HTML
- CSS
- Razorpay Checkout

### Why Streamlit?

- Rapid UI Development
- Python-Based
- Easy API Integration
- Lightweight

---

## Backend

- FastAPI
- Uvicorn
- SQLAlchemy

### Why FastAPI?

- High Performance
- Async Support
- Automatic API Documentation
- Easy Dependency Injection

---

## Database

- PostgreSQL

### Why PostgreSQL?

- ACID Compliance
- High Reliability
- Scalability
- Strong SQL Support

---

## Image Processing

### OpenCV

Used for:

- Pencil Sketch
- Oil Painting
- Vintage
- Watercolor
- Pop Art

### AnimeGAN

Used for:

- AI Anime Transformation

---

## Payment Gateway

### Razorpay

Used for:

- Order Creation
- Payment Processing
- Transaction Tracking

---

# 📂 Project Structure

```text
TOON
│
├── backend
│   │
│   ├── api
│   │   ├── admin.py
│   │   ├── auth.py
│   │   ├── history.py
│   │   ├── image.py
│   │   ├── payment.py
│   │   └── profile.py
│   │
│   ├── database
│   │   └── connection.py
│   │
│   ├── models
│   │   ├── user.py
│   │   ├── image_history.py
│   │   └── payment.py
│   │
│   ├── repositories
│   │   ├── user_repository.py
│   │   ├── image_repository.py
│   │   └── payment_repository.py
│   │
│   ├── services
│   │   ├── auth_service.py
│   │   ├── image_service.py
│   │   ├── payment_service.py
│   │   ├── razorpay_service.py
│   │   └── admin_service.py
│   │
│   ├── uploads
│   │   ├── originals
│   │   └── cartoons
│   │
│   ├── effects.py
│   ├── effect_prices.py
│   └── main.py
│
├── frontend
│   │
│   ├── services
│   │   ├── auth_api.py
│   │   ├── image_api.py
│   │   ├── history_api.py
│   │   ├── payment_api.py
│   │   ├── profile_api.py
│   │   └── admin_api.py
│   │
│   ├── app.py
│   ├── effects.py
│   └── styles.css
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/toonify-ai.git
```

```bash
cd toonify-ai
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Setup

Create PostgreSQL Database:

```sql
CREATE DATABASE toonify_db;
```

Update database credentials in:

```text
backend/database/connection.py
```

---

# ▶ Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ▶ Run Frontend

```bash
streamlit run frontend/app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
RAZORPAY_KEY=your_key
RAZORPAY_SECRET=your_secret
```

Never push `.env` to GitHub.

---

# 🔄 Application Workflow

1. User registers/login
2. User uploads image
3. Backend stores image
4. Selected effect is applied
5. Generated image is saved
6. History is stored in PostgreSQL
7. User downloads free image OR pays for premium effect
8. Payment is recorded
9. Payment history is displayed

---

# 📈 Future Enhancements

- JWT Authentication
- Google Login
- Cloud Storage (AWS S3)
- Docker Deployment
- Kubernetes Deployment
- Mobile Application
- Video Cartoonization
- Stable Diffusion Integration
- AI-Based Recommendations
- Multi-Language Support

---

# 🎯 Project Objectives

- Simplify image stylization using AI
- Provide multiple artistic effects
- Offer a pay-per-use business model
- Create a scalable and maintainable architecture
- Deliver a smooth user experience

---

# 👩‍💻 Developer

**Kaveri Savarapu**

Full Stack AI Application Developer

Technologies Used:

- Python
- FastAPI
- Streamlit
- PostgreSQL
- OpenCV
- SQLAlchemy
- Razorpay
- AnimeGAN

---

# 📜 License

This project is developed for educational and demonstration purposes.

All rights reserved © 2026 Toonify AI.