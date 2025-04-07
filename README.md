# SHL Assessment Recommendation Engine

This project implements a recommendation engine for SHL assessments using machine learning and AI techniques. The engine provides an intuitive web interface for users to input their requirements and receive personalized SHL product recommendations.

## Technology Stack

### Frontend
- **Framework**: FastAPI with Jinja2 templating
- **Styling**: 
  - Tailwind CSS for responsive design
  - Custom CSS for unique components
  - Font Awesome for icons
- **JavaScript**:
  - Alpine.js for reactive components
  - Chart.js for data visualization
  - Axios for API communication
- **UI Components**:
  - Custom form elements
  - Interactive data tables
  - Modal dialogs
  - Toast notifications
  - Progress indicators

### Backend
- **Framework**: FastAPI
- **Machine Learning**:
  - Scikit-learn for recommendation algorithms
  - Natural Language Processing (NLP) for requirement analysis
- **Database**: SQLite for development, PostgreSQL for production
- **API**: RESTful endpoints with OpenAPI documentation

## Features

### Core Features
- Product recommendation based on user requirements
- Natural language processing for understanding assessment needs
- Machine learning-based matching algorithm
- REST API interface for easy integration
- Configurable recommendation parameters

### Interactive UI Features
- Modern, responsive web interface
- Real-time recommendation updates
- Interactive requirement input form
- Visual product comparison dashboard
- Detailed product information cards
- User-friendly navigation
- Mobile-responsive design
- Loading indicators and feedback
- Error handling with user-friendly messages

### UI/UX Enhancements
- **Accessibility Features**:
  - ARIA labels for screen readers
  - Keyboard navigation support
  - High contrast mode
  - Responsive font sizing
- **User Experience**:
  - Guided onboarding process
  - Interactive tutorials
  - Contextual help tooltips
  - Smooth page transitions
  - Progressive loading
- **Visual Design**:
  - Consistent color scheme
  - Modern typography
  - Micro-interactions
  - Loading skeletons
  - Animated transitions
- **Feedback Mechanisms**:
  - Success/error notifications
  - Form validation messages
  - Progress indicators
  - Confirmation dialogs
  - Undo/redo functionality

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your configuration:
```
SHL_API_KEY=your_api_key
MODEL_PATH=models/
DATA_PATH=data/
```

4. Run the application:
```bash
uvicorn main:app --reload
```

## Project Structure

- `main.py`: Main application and API endpoints
- `recommender/`: Core recommendation engine
- `data/`: SHL product catalog data
- `models/`: Trained ML models
- `config.py`: Configuration settings
- `requirements.txt`: Project dependencies
- `templates/`: HTML templates
  - `index.html`: Main application interface
  - `test.html`: Testing interface
- `static/`: Static assets
  - `css/`: Stylesheets
  - `js/`: JavaScript files
  - `images/`: UI assets and icons

## UI Components

### Main Interface
- **Requirement Input Form**
  - Text input for assessment requirements
  - Dropdown menus for specific criteria
  - Checkboxes for additional options
  - Submit button with loading state
  - Auto-save functionality
  - Form validation with visual feedback

- **Recommendation Display**
  - Product cards with key information
  - Visual comparison charts
  - Detailed product descriptions
  - Action buttons for each recommendation
  - Filter and sort options
  - Export functionality

- **Navigation**
  - Main menu with all sections
  - Breadcrumb navigation
  - Quick access buttons
  - Search functionality
  - Recent history
  - Favorites/bookmarks

### Interactive Features
- Real-time form validation
- Dynamic content loading
- Smooth transitions and animations
- Responsive layout adjustments
- Error message displays
- Success notifications
- Loading spinners and progress indicators
- Drag-and-drop functionality
- Infinite scroll for long lists
- Real-time search filtering

## API Endpoints

- `POST /recommend`: Get assessment recommendations
- `GET /products`: List available SHL products
- `GET /health`: Check service health

## Browser Support
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Performance Optimization
- Lazy loading of components
- Image optimization
- Code splitting
- Caching strategies
- Progressive Web App (PWA) support
- Service worker implementation

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.