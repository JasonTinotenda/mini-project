# app.py (Backend - Flask)
from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# Sample course data
courses = [
    {
        "id": 1,
        "title": "Introduction to Python Programming",
        "description": "Learn the fundamentals of Python programming language",
        "difficulty": "Beginner",
        "duration": "8 weeks",
        "tags": ["programming", "python", "beginner"],
        "rating": 4.7,
        "students": 1250
    },
    {
        "id": 2,
        "title": "Data Structures and Algorithms",
        "description": "Master essential data structures and algorithms",
        "difficulty": "Intermediate",
        "duration": "10 weeks",
        "tags": ["programming", "algorithms", "computer science"],
        "rating": 4.8,
        "students": 980
    },
    {
        "id": 3,
        "title": "Machine Learning Fundamentals",
        "description": "Introduction to machine learning concepts and techniques",
        "difficulty": "Intermediate",
        "duration": "12 weeks",
        "tags": ["AI", "machine learning", "data science"],
        "rating": 4.9,
        "students": 2100
    },
    {
        "id": 4,
        "title": "Web Development with HTML/CSS/JavaScript",
        "description": "Build responsive websites using core web technologies",
        "difficulty": "Beginner",
        "duration": "10 weeks",
        "tags": ["web development", "frontend", "HTML", "CSS"],
        "rating": 4.6,
        "students": 1850
    },
    {
        "id": 5,
        "title": "Database Management Systems",
        "description": "Learn to design and manage databases effectively",
        "difficulty": "Intermediate",
        "duration": "9 weeks",
        "tags": ["database", "SQL", "backend"],
        "rating": 4.5,
        "students": 1200
    },
    {
        "id": 6,
        "title": "Advanced Python Programming",
        "description": "Deep dive into advanced Python concepts and patterns",
        "difficulty": "Advanced",
        "duration": "10 weeks",
        "tags": ["programming", "python", "advanced"],
        "rating": 4.8,
        "students": 850
    }
]

# Recommendation algorithm (simple tag matching)
def recommend_courses(interests, max_recommendations=4):
    recommendations = []
    for course in courses:
        score = 0
        for interest in interests:
            if interest.lower() in [tag.lower() for tag in course['tags']]:
                score += 1
        if score > 0:
            recommendations.append((course, score))
    
    # Sort by score and return top recommendations
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return [course for course, score in recommendations[:max_recommendations]]

@app.route('/')
def index():
    return render_template('index.html', courses=courses)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    interests = data.get('interests', [])
    recommended = recommend_courses(interests)
    return jsonify(recommended)

if __name__ == '__main__':
    app.run(debug=True)