# 🏨 ALX Travel App

A **production-ready Django REST API** for a travel listing platform built following industry best practices and 12-factor app methodology.

[![Django Version](https://img.shields.io/badge/Django-5.2.1-green.svg)](https://djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Key Features

- **🏠 Listings Management**: Complete CRUD operations for travel accommodations
- **🔧 REST API**: Built with Django REST Framework with filtering, search, and pagination
- **📖 API Documentation**: Automatic Swagger/OpenAPI documentation with drf-yasg
- **🔒 Security**: Secure environment variable management with django-environ
- **🗄️ Database**: MySQL integration with optimized queries
- **⚡ Background Tasks**: Celery with RabbitMQ for asynchronous processing
- **🌐 CORS**: Cross-Origin Resource Sharing for frontend integration
- **🎯 Code Quality**: Pylint integration with 9+ score across all modules

## 🛠️ Tech Stack

| Category           | Technology            | Version |
| ------------------ | --------------------- | ------- |
| **Backend**        | Django                | 5.2.1   |
| **API**            | Django REST Framework | 3.16.0  |
| **Database**       | MySQL                 | 8.0+    |
| **Documentation**  | drf-yasg              | 1.21.10 |
| **Task Queue**     | Celery                | 5.5.2   |
| **Message Broker** | RabbitMQ/Pika         | 1.3.2   |
| **Environment**    | django-environ        | 0.12.0  |
| **CORS**           | django-cors-headers   | 4.7.0   |

## 📋 Prerequisites

- **Python 3.12+**
- **MySQL 8.0+**
- **RabbitMQ** (optional, for background tasks)
- **Git** (for version control)

## ⚡ Quick Start

### 1. Clone & Setup

```bash
# Clone the repository
git clone <your-repository-url>
cd alx_travel_app

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Generate a secure SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Edit .env file with your settings
nano .env
```

**Required Environment Variables:**

```bash
# Security
SECRET_KEY=your-generated-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=alxtravelapp
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306

# CORS (for frontend integration)
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 3. Database Setup

```sql
-- Create MySQL database
CREATE DATABASE alxtravelapp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
GRANT ALL PRIVILEGES ON alxtravelapp.* TO 'your_mysql_user'@'localhost';
FLUSH PRIVILEGES;
```

### 4. Django Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

### 5. Access the Application

| Interface          | URL                            | Description                   |
| ------------------ | ------------------------------ | ----------------------------- |
| **🔧 Admin Panel** | http://127.0.0.1:8000/admin/   | Django admin interface        |
| **📖 Swagger UI**  | http://127.0.0.1:8000/swagger/ | Interactive API documentation |
| **📋 ReDoc**       | http://127.0.0.1:8000/redoc/   | Alternative API documentation |
| **🔗 API Root**    | http://127.0.0.1:8000/api/     | REST API endpoints            |

## 📁 Project Structure

```
alx_travel_app/                     # 📦 Project root
├── 📄 README.md                    # Project documentation
├── 📄 SECURITY.md                  # Security guidelines
├── 📄 requirements.txt             # Python dependencies
├── 🔒 .env                         # Environment variables (not in VCS)
├── 📋 .env.example                 # Environment template
├── 🚫 .gitignore                   # Git ignore rules
├── ⚙️ manage.py                    # Django management script
├── 📁 alx_travel_app/              # Django project package
│   ├── ⚙️ settings.py              # Django settings
│   ├── 🌐 urls.py                  # Main URL configuration
│   ├── 🔧 wsgi.py                  # WSGI configuration
│   ├── ⚡ asgi.py                  # ASGI configuration
│   └── 🔄 celery_app.py            # Celery configuration
├── 📁 listings/                    # Listings app
│   ├── 🗄️ models.py               # Database models
│   ├── 🔧 views.py                 # API views
│   ├── 📝 serializers.py           # DRF serializers
│   ├── 🌐 urls.py                  # App URLs
│   ├── ⚙️ admin.py                 # Admin configuration
│   └── 📁 migrations/              # Database migrations
├── 📁 static/                      # Static files
├── 📁 media/                       # Uploaded files
└── 📁 templates/                   # HTML templates
```

## 🔗 API Endpoints

### 🏠 Listings API

| Method   | Endpoint                  | Description                      |
| -------- | ------------------------- | -------------------------------- |
| `GET`    | `/api/listings/`          | List all listings with filtering |
| `POST`   | `/api/listings/`          | Create new listing               |
| `GET`    | `/api/listings/{slug}/`   | Retrieve specific listing        |
| `PUT`    | `/api/listings/{slug}/`   | Update listing                   |
| `DELETE` | `/api/listings/{slug}/`   | Delete listing                   |
| `GET`    | `/api/listings/featured/` | Get featured listings            |

### 🎯 Features

- **🔍 Filtering**: By type, location, guests, bedrooms
- **🔎 Search**: Full-text search in title, description, location
- **📊 Ordering**: By price, date, bedrooms, guests
- **📄 Pagination**: Efficient data loading

## 🧪 Development

### Running Tests

```bash
# Run all tests
python manage.py test

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

### Code Quality

```bash
# Install development dependencies
pip install pylint pylint-django

# Run linting
pylint --load-plugins=pylint_django --django-settings-module=alx_travel_app.settings **/*.py
```

### Background Tasks (Optional)

```bash
# Install and start RabbitMQ (Ubuntu/Debian)
sudo apt-get install rabbitmq-server
sudo systemctl start rabbitmq-server

# Start Celery worker
celery -A alx_travel_app worker -l info

# Start Celery beat (for scheduled tasks)
celery -A alx_travel_app beat -l info
```

## 🔒 Security

This project follows security best practices:

- **✅ Environment Variables**: All sensitive data externalized
- **✅ No Hardcoded Secrets**: Credentials never in source code
- **✅ Secure Defaults**: DEBUG=False, strong validation
- **✅ CORS Configuration**: Controlled cross-origin access
- **✅ SQL Injection Protection**: Django ORM with parameterized queries

📖 **Read**: [SECURITY.md](SECURITY.md) for detailed security guidelines.

## 🚀 Production Deployment

### Environment Variables for Production

```bash
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_HOST=your-production-db-host
# ... other production settings
```

### Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Use strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up SSL/HTTPS
- [ ] Configure static files serving
- [ ] Set up monitoring and logging
- [ ] Configure database backups

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **📖 Documentation**: Check the `/swagger/` endpoint for API docs
- **🐛 Issues**: Report bugs in the GitHub issues section
- **💬 Discussions**: Use GitHub discussions for questions

## 🏆 Project Status

**✅ Milestone 1 Complete**: Setup and Database Configuration

- ✅ Django project setup with best practices
- ✅ MySQL database integration
- ✅ Environment variable management
- ✅ API documentation with Swagger
- ✅ Security hardening
- ✅ Code quality standards

---

**Built with ❤️ for the ALX Software Engineering Program**
