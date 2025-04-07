# 🚀 SHL Assessment Recommendation Engine

<br>

## 📋 Table of Contents
- [✨ Features](#-features)
- [🛠️ Technology Stack](#️-technology-stack)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🔧 Setup Guide](#-setup-guide)
- [📚 API Documentation](#-api-documentation)

## ✨ Features

### 🎯 Core Features
- 🤖 AI-powered product recommendations
- 📊 Real-time requirement analysis
- 🔍 Intelligent matching algorithm
- 🔄 REST API integration
- ⚙️ Customizable parameters

### 🎨 Interactive UI
- 📱 Responsive design
- ⚡ Real-time updates
- 🎯 User-friendly forms
- 📈 Visual dashboards
- 🎮 Interactive elements

## 🛠️ Technology Stack

### Frontend
<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-0.68.0-green.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/Tailwind_CSS-3.0-blue.svg" alt="Tailwind CSS">
  <img src="https://img.shields.io/badge/Alpine.js-3.0-purple.svg" alt="Alpine.js">
  <img src="https://img.shields.io/badge/Chart.js-3.0-red.svg" alt="Chart.js">
</div>

### Backend
<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Scikit_learn-1.0-orange.svg" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/PostgreSQL-13.0-blue.svg" alt="PostgreSQL">
</div>

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/shl-recommendation-engine.git
cd shl-recommendation-engine

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload
```

## 📁 Project Structure
```
shl-recommendation-engine/
├── main.py              # Main application
├── run_server.py        # Server configuration
├── config.py            # Configuration settings
├── requirements.txt     # Project dependencies
├── templates/           # HTML templates
├── static/             # Static assets
├── models/             # ML models
└── data/               # Data files
```

## 🔧 Setup Guide

1. **Environment Setup**
   ```bash
   # Create .env file
   cp .env.example .env
   # Edit .env with your configuration
   ```

2. **Database Setup**
   ```bash
   # Initialize database
   python scripts/init_db.py
   ```

3. **Run Tests**
   ```bash
   pytest tests/
   ```

## 📚 API Documentation

### Available Endpoints
- `POST /recommend` - Get assessment recommendations
- `GET /products` - List available products
- `GET /health` - Check service health

For detailed API documentation, visit: `http://localhost:8000/docs`

---

<div align="center">
  <sub>Built with ❤️ by the Abhishek sharma</sub>
</div>
