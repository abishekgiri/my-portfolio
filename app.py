from flask import Flask, render_template, request

app = Flask(__name__)

TAG_CONFIG = {
    "Python": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    "JavaScript": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"},
    "HTML": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"},
    "HTML/CSS": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"},
    "Java": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"},
    "C++": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg"},
    "C": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg"},
    "SQL": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"},
    "Go": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original-wordmark.svg", "name": "Golang"},
    "Flask": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"},
    "React": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"},
    "Tailwind CSS": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-original.svg"},
    "Node.js": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg"},
    "Git": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"},
    "AWS": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg"},
    "Linux": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"},
    "Docker": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"},
    "Matplotlib": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    "Socket.IO": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/socketio/socketio-original.svg"},
    "WebSockets": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/socketio/socketio-original.svg"},
    "Pandas": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg"},
    "Scikit-learn": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    "CSS": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"},
    "NLP": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    "Machine Learning": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    "Data Science": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    "Generative AI": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    "LLM": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    "Design": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg"},
    "Visualization": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/d3js/d3js-original.svg"},
    "Algorithms": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    "CUDA": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cuda/cuda-original.svg"},
    "Parquet": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apache/apache-original.svg"},
    "SIMD": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg"},
    "CMake": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cmake/cmake-original.svg"},
    "Systems Engineering": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"},
    "MongoDB": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg"},
    "Express": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/express/express-original.svg"},
    "Streamlit": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg"},
    "Security": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/argocd/argocd-original.svg"},
    "Data Engineering": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apache/apache-original.svg"},
    "MySQL": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"},
}

@app.route("/")
def index():
    # Load all data for the dashboard view
    import json
    import os
    from collections import Counter

    # Load Projects
    projects_path = os.path.join(app.root_path, 'data', 'projects.json')
    with open(projects_path, 'r') as f:
        projects = json.load(f)

    # Load Experience
    experience_path = os.path.join(app.root_path, 'data', 'experience.json')
    with open(experience_path, 'r') as f:
        experience = json.load(f)

    # Calculate Skills (Reuse logic or refactor, for now duplicating for speed)
    tag_counts = Counter()
    for p in projects:
        if 'tags' in p:
            tag_counts.update(p['tags'])



    skills_data = {"Languages": [], "Tools": []}
    for tag, count in tag_counts.items():
        # Default icon if not found
        default_icon = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/devicon/devicon-original.svg"
        config = TAG_CONFIG.get(tag, {"cat": "Tools", "icon": default_icon})
        level = min(50 + (count * 10), 98)
        skill_entry = {
            "name": config.get("name", tag),
            "icon": config["icon"],
            "level": level
        }
        if config["cat"] in skills_data:
            skills_data[config["cat"]].append(skill_entry)

    # Sort skills by level
    for cat in skills_data:
        skills_data[cat].sort(key=lambda x: x['level'], reverse=True)

    return render_template("index.html", projects=projects, experience=experience, skills=skills_data)

@app.route("/about")
def about():
    import json
    import os
    
    data_path = os.path.join(app.root_path, 'data', 'experience.json')
    experience_data = []
    if os.path.exists(data_path):
        with open(data_path, 'r') as f:
            experience_data = json.load(f)
            
    return render_template("about.html", experience=experience_data)

@app.route("/projects")
def projects():
    import json
    import os

    data_path = os.path.join(app.root_path, 'data', 'projects.json')
    with open(data_path, 'r') as f:
        projects_data = json.load(f)
        
    # Inject logo based on first tag

    
    for project in projects_data:
        # Default logo
        project['logo'] = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"
        
        if 'tags' in project and project['tags']:
            # Try to find the first tag that has an icon
            for tag in project['tags']:
                if tag in TAG_CONFIG:
                    project['logo'] = TAG_CONFIG[tag]['icon']
                    break
    
    return render_template("projects.html", projects=projects_data)

@app.route("/skills")
def skills():
    # Dynamic Skills Calculation
    import json
    import os
    from collections import Counter

    # Load projects to count tags
    data_path = os.path.join(app.root_path, 'data', 'projects.json')
    with open(data_path, 'r') as f:
        projects_list = json.load(f)

    # Count all tags
    tag_counts = Counter()
    for p in projects_list:
        if 'tags' in p:
            tag_counts.update(p['tags'])



    skills_data = {"Languages": [], "Tools": []}
    
    # Process counts into skills_data
    # We normalize counts to a "level" (0-100)
    # Heuristic: Base 50 + (count * 5), max 95
    
    for tag, count in tag_counts.items():
        # Default icon if not found
        default_icon = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/devicon/devicon-original.svg"
        config = TAG_CONFIG.get(tag, {"cat": "Tools", "icon": default_icon})
        
        level = min(50 + (count * 10), 98)
        
        skill_entry = {
            "name": config.get("name", tag),
            "icon": config["icon"],
            "level": level
        }
        
        if config["cat"] in skills_data:
            skills_data[config["cat"]].append(skill_entry)

    # Sort by level descending
    for cat in skills_data:
        skills_data[cat].sort(key=lambda x: x['level'], reverse=True)
    
    return render_template("skills.html", skills=skills_data)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit_form", methods=["POST"])
def submit_form():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")
    
    print(f"New Message from {name} ({email}): {message}")
    
    # Save to file
    with open("messages.txt", "a") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Phone: {phone}\n")
        f.write(f"Message: {message}\n")
        f.write("-" * 20 + "\n")
    
    return f"<h1>Thanks {name}, your message has been received!</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5050)
