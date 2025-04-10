# 🚀 SHL Assessment Recommendation Engine


## 📋 Project Description

The SHL Assessment Recommendation Engine is an intelligent system designed to help organizations and HR professionals select the most appropriate SHL assessments for their specific needs. This AI-powered solution combines machine learning algorithms with natural language processing to provide personalized assessment recommendations based on job roles, assessment requirements, and experience levels.

### 🎯 Key Features

- **Intelligent Matching**: Utilizes advanced algorithms to match SHL products with specific job roles and assessment needs
- **Multi-factor Analysis**: Considers multiple parameters including:
  - Job role requirements
  - Assessment objectives
  - Experience levels
  - Category matching
  - Semantic similarity
- **Real-time Recommendations**: Provides instant, data-driven suggestions
- **Confidence Scoring**: Each recommendation comes with a confidence score
- **RESTful API**: Easy integration with existing HR systems
- **Modern Web Interface**: User-friendly dashboard for easy interaction

### 🧠 Technical Implementation

The engine is built using state-of-the-art technologies:

- **Natural Language Processing**: Uses sentence transformers for semantic understanding
- **Machine Learning**: Implements custom scoring algorithms for precise matching
- **API Architecture**: RESTful endpoints with FastAPI for high performance
- **Data Processing**: Efficient handling of product catalogs and user inputs
- **Scalable Design**: Ready for enterprise-level deployment

### 🏢 Use Cases

- **HR Departments**: Streamline assessment selection process
- **Recruitment Agencies**: Match candidates with appropriate assessments
- **Learning & Development**: Identify suitable assessments for training programs
- **Career Development**: Guide employees in their professional growth
- **Talent Management**: Support comprehensive talent assessment strategies

### 🔄 How It Works

1. **Input Collection**: Users provide:
   - Job role description
   - Assessment needs
   - Experience level (optional)
2. **Processing**: The engine:
   - Analyzes input using NLP
   - Matches against product database
   - Calculates confidence scores
3. **Output**: Returns:
   - Ranked list of recommended products
   - Confidence scores
   - Detailed product information

## 📋 Project Description

The SHL Assessment Recommendation Engine is an intelligent system designed to help organizations and HR professionals select the most appropriate SHL assessments for their specific needs. This AI-powered solution combines machine learning algorithms with natural language processing to provide personalized assessment recommendations based on job roles, assessment requirements, and experience levels.

### 🎯 Key Features

- **Intelligent Matching**: Utilizes advanced algorithms to match SHL products with specific job roles and assessment needs
- **Multi-factor Analysis**: Considers multiple parameters including:
  - Job role requirements
  - Assessment objectives
  - Experience levels
  - Category matching
  - Semantic similarity
- **Real-time Recommendations**: Provides instant, data-driven suggestions
- **Confidence Scoring**: Each recommendation comes with a confidence score
- **RESTful API**: Easy integration with existing HR systems
- **Modern Web Interface**: User-friendly dashboard for easy interaction

### 🧠 Technical Implementation

The engine is built using state-of-the-art technologies:

- **Natural Language Processing**: Uses sentence transformers for semantic understanding
- **Machine Learning**: Implements custom scoring algorithms for precise matching
- **API Architecture**: RESTful endpoints with FastAPI for high performance
- **Data Processing**: Efficient handling of product catalogs and user inputs
- **Scalable Design**: Ready for enterprise-level deployment

### 🏢 Use Cases

- **HR Departments**: Streamline assessment selection process
- **Recruitment Agencies**: Match candidates with appropriate assessments
- **Learning & Development**: Identify suitable assessments for training programs
- **Career Development**: Guide employees in their professional growth
- **Talent Management**: Support comprehensive talent assessment strategies

### 🔄 How It Works

1. **Input Collection**: Users provide:
   - Job role description
   - Assessment needs
   - Experience level (optional)
2. **Processing**: The engine:
   - Analyzes input using NLP
   - Matches against product database
   - Calculates confidence scores
3. **Output**: Returns:
   - Ranked list of recommended products
   - Confidence scores
   - Detailed product information

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

## 📊 Evaluation Metrics

The system's performance is evaluated using two key metrics:

### 1. Mean Recall@K
This metric measures how many of the relevant assessments were retrieved in the top K recommendations, averaged across all test queries.

```
𝑅𝑒𝑐𝑎𝑙𝑙@𝐾 = Number of relevant assessments in top K / Total relevant assessments for the query
𝑀𝑒𝑎𝑛𝑅𝑒𝑐𝑎𝑙𝑙@𝐾 = (1/𝑁) * ∑𝑅𝑒𝑐𝑎𝑙𝑙@𝐾𝑖
where N is the total number of test queries.
```

### 2. Mean Average Precision @K (MAP@K)
MAP@K evaluates both the relevance and ranking order of retrieved assessments by calculating Precision@k at each relevant result and averaging it over all queries.

```
𝐴𝑃@𝐾 = (1/min(𝐾, 𝑅)) * ∑𝑃(𝑘) * 𝑟𝑒𝑙(𝑘)
𝑀𝐴𝑃@𝐾 = (1/𝑁) * ∑𝐴𝑃@𝐾𝑖
where:
- R = total relevant assessments for the query
- P(k) = precision at position k
- rel(k) = 1 if the result at position k is relevant, otherwise 0
- N = total number of test queries
```

## 🧪 Test Cases

The system is tested against the following real-world scenarios:

1. **Java Developer Query**
   ```
   "I am hiring for Java developers who can also collaborate effectively with my business teams. Looking for an assessment(s) that can be completed in 40 minutes."
   ```

2. **Python/SQL/JS Query**
   ```
   "Looking to hire mid-level professionals who are proficient in Python, SQL and Java Script. Need an assessment package that can test all skills with max duration of 60 minutes."
   ```

3. **JD Screening Query**
   ```
   "Here is a JD text, can you recommend some assessment that can help me screen applications. Time limit is less than 30 minutes."
   ```

4. **Analyst Cognitive Query**
   ```
   "I am hiring for an analyst and wants applications to screen using Cognitive and personality tests, what options are available within 45 min"
   ```

### Running Tests
To run the evaluation tests:
```bash
python test_api.py
```

The test script will:
1. Execute each test case
2. Calculate Recall@10 and MAP@10 metrics
3. Display detailed results including:
   - Recommended assessments
   - Duration
   - Adaptive/Remote support
   - Test types
   - Similarity scores
   - Evaluation metrics

---

<div align="center">
  <sub>Built with ❤️ by the Abhishek sharma</sub>
</div>
