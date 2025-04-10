import requests
import json
import numpy as np

def test_recommendation(query, filters=None):
    url = "http://localhost:8000/recommend"
    headers = {"Content-Type": "application/json"}
    
    if filters is None:
        filters = {}
    
    data = {
        "query": query,
        "filters": filters
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def calculate_recall_at_k(relevant_items, recommended_items, k):
    """Calculate Recall@K metric"""
    relevant_in_top_k = len(set(relevant_items) & set(recommended_items[:k]))
    return relevant_in_top_k / len(relevant_items) if relevant_items else 0

def calculate_average_precision_at_k(relevant_items, recommended_items, k):
    """Calculate Average Precision@K metric"""
    precision_at_k = []
    relevant_count = 0
    
    for i, item in enumerate(recommended_items[:k], 1):
        if item in relevant_items:
            relevant_count += 1
            precision_at_k.append(relevant_count / i)
    
    return sum(precision_at_k) / min(k, len(relevant_items)) if relevant_items else 0

def evaluate_recommendations(recommendations, ground_truth, k=10):
    """Evaluate recommendations using Recall@K and MAP@K metrics"""
    recommended_ids = [r['url'] for r in recommendations]
    recall = calculate_recall_at_k(ground_truth, recommended_ids, k)
    map_score = calculate_average_precision_at_k(ground_truth, recommended_ids, k)
    return recall, map_score

# Test cases from requirements
test_cases = [
    {
        "name": "Java Developer Query",
        "query": "I am hiring for Java developers who can also collaborate effectively with my business teams. Looking for an assessment(s) that can be completed in 40 minutes.",
        "filters": {
            "duration": 40,
            "test_type": ["Knowledge & Skills", "Competencies"]
        }
    },
    {
        "name": "Python/SQL/JS Query",
        "query": "Looking to hire mid-level professionals who are proficient in Python, SQL and Java Script. Need an assessment package that can test all skills with max duration of 60 minutes.",
        "filters": {
            "duration": 60,
            "test_type": ["Knowledge & Skills", "Technical Skills"]
        }
    },
    {
        "name": "JD Screening Query",
        "query": "Here is a JD text, can you recommend some assessment that can help me screen applications. Time limit is less than 30 minutes.",
        "filters": {
            "duration": 30,
            "test_type": ["Cognitive Ability", "Personality & Behaviour"]
        }
    },
    {
        "name": "Analyst Cognitive Query",
        "query": "I am hiring for an analyst and wants applications to screen using Cognitive and personality tests, what options are available within 45 min",
        "filters": {
            "duration": 45,
            "test_type": ["Cognitive Ability", "Personality & Behaviour"]
        }
    }
]

# Run tests and evaluate
print("\nRunning Evaluation Tests...\n")
print("="*80)

for test in test_cases:
    print(f"\nTest Case: {test['name']}")
    print(f"Query: {test['query']}")
    print(f"Filters: {json.dumps(test['filters'], indent=2)}")
    
    result = test_recommendation(test['query'], test['filters'])
    
    if result:
        print("\nResults:")
        for i, assessment in enumerate(result['recommended_assessments'], 1):
            print(f"\n{i}. {assessment['description']}")
            print(f"   Duration: {assessment['duration']} minutes")
            print(f"   Adaptive Support: {assessment['adaptive_support']}")
            print(f"   Remote Support: {assessment['remote_support']}")
            print(f"   Test Types: {', '.join(assessment['test_type'])}")
            print(f"   Similarity Score: {assessment.get('similarity_score', 'N/A')}")
    else:
        print("No results or error occurred")
    
    print("\n" + "="*80) 