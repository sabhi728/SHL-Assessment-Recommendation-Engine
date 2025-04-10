# 🚀 SHL Assessment Recommendation Engine

## 📋 Project Description

The SHL Assessment Recommendation Engine is an intelligent system designed to help organizations and HR professionals select the most appropriate SHL assessments for their specific needs. This AI-powered solution uses natural language processing to provide personalized assessment recommendations based on job descriptions and requirements.

### 🎯 Key Features

- **Intelligent Matching**: Utilizes sentence transformers for semantic understanding
- **Real-time Recommendations**: Provides instant, data-driven suggestions
- **RESTful API**: Easy integration with existing HR systems
- **Modern Web Interface**: User-friendly dashboard for easy interaction
- **Comprehensive Assessment Database**: Wide range of SHL assessments with detailed metadata

## 🛠️ Technology Stack

### Backend
- FastAPI (Python web framework)
- Sentence Transformers (NLP for semantic similarity)
- Pydantic (Data validation)
- Uvicorn (ASGI server)

### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla)
- Tailwind CSS (Styling)

## 📚 API Documentation

### Base URL
```
http://localhost:8000
```

### Available Endpoints

1. **Health Check**
   ```
   GET /health
   ```
   Response:
   ```json
   {
       "status": "healthy"
   }
   ```

2. **Assessment Recommendation**
   ```
   POST /recommend
   ```
   Request Body:
   ```json
   {
       "query": "Job description or query string"
   }
   ```
   Response:
   ```json
   {
       "recommended_assessments": [
           {
               "url": "https://www.shl.com/solutions/products/product-catalog/view/assessment-name/",
               "adaptive_support": "Yes/No",
               "description": "Assessment description",
               "duration": 60,
               "remote_support": "Yes/No",
               "test_type": ["Type1", "Type2"]
           }
       ]
   }
   ```

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd shl-recommendation-engine
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix/MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the application**
   - Web Interface: `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs`

## 📁 Project Structure

```
shl-recommendation-engine/
├── main.py              # Main FastAPI application
├── requirements.txt     # Project dependencies
├── data/               # Data files
│   └── shl_products.json  # Assessment database
├── static/             # Static assets
│   ├── css/
│   └── images/
├── templates/          # HTML templates
│   └── index.html
└── test_api.py        # API test cases
```

## 🧪 Testing

### API Testing
Run the test script to verify API functionality:
```bash
python test_api.py
```

### Example Test Cases
1. **Technical Role**
   ```json
   {
       "query": "Looking for a Python developer with experience in web development"
   }
   ```

2. **Leadership Role**
   ```json
   {
       "query": "Need to assess leadership potential and team management skills"
   }
   ```

3. **AI/ML Role**
   ```json
   {
       "query": "Evaluating candidates for AI and machine learning positions"
   }
   ```

## 🔧 Configuration

The application uses the following environment variables (optional):
- `API_HOST`: Host address (default: 0.0.0.0)
- `API_PORT`: Port number (default: 8000)

## 📊 Assessment Types

The system supports various assessment types including:
- Knowledge & Skills
- Technical Skills
- Competencies
- Personality & Behaviour
- AI & ML
- Cognitive Ability
- And more...

---

<div align="center">
  <sub>Built with ❤️ by Abhishek sharma</sub>
</div>
