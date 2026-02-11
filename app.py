from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static", "img"),
        "favicon.svg",
        mimetype="image/svg+xml",
    )

TAG_CONFIG = {
    # Languages
    "Python": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    "JavaScript": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"},
    "Go": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original-wordmark.svg", "name": "Golang"},
    "Java": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"},
    "C++": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg"},
    "C": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg"},
    "SQL": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"},
    "HTML": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"},
    "CSS": {"cat": "Languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"},
    
    # Frameworks & Libraries
    "React": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"},
    "Flask": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"},
    "Node.js": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg"},
    "Express": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/express/express-original.svg"},
    "PyTorch": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg"},
    "Pandas": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg"},
    "Matplotlib": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"}, # Fallback
    "Scikit-learn": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg"},
    "Streamlit": {"cat": "Tools", "icon": "https://streamlit.io/images/brand/streamlit-mark-color.png"}, # Custom URL if needed or generic

    # Infrastructure & Tools
    "AWS": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg"},
    "Docker": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"},
    "Kubernetes": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg"},
    "Terraform": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/terraform/terraform-original.svg"},
    "Kafka": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apachekafka/apachekafka-original.svg"},
    "Redis": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg"},
    "MongoDB": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg"},
    "PostgreSQL": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg"},
    "MySQL": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"},
    "Git": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"},
    "Linux": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"},

    # Concepts / Other (Generic Icons)
    "Distributed Systems": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/networkx/networkx-original.svg"}, # Approximation
    "Machine Learning": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg"}, # Using TF icon for general ML
    "Generative AI": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/openai/openai-original.svg"}, # If available, or generic
    "LLM": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/openai/openai-original.svg"}, 
    "VLM": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    "NLP": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    "Design": {"cat": "Tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg"},
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

    # Calculate Skills
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
        if config.get("cat") in skills_data:
            skills_data[config["cat"]].append(skill_entry)

    # Sort skills by level
    for cat in skills_data:
        skills_data[cat].sort(key=lambda x: x['level'], reverse=True)
        # Deduplicate
        seen = set()
        unique_skills = []
        for s in skills_data[cat]:
            if s['name'] not in seen:
                unique_skills.append(s)
                seen.add(s['name'])
        skills_data[cat] = unique_skills

    # Filter Research Papers
    research_papers = []
    normal_projects = []
    
    for p in projects:
        is_research = False
        if p.get('category') == 'ai' or 'Research' in p.get('tags', []):
             if 'Paper' in p.get('title', '') or 'Research' in p.get('title', '') or 'Defense' in p.get('title', '') or 'Failure' in p.get('title', ''):
                 is_research = True
        
        if is_research:
            research_papers.append(p)
        else:
            normal_projects.append(p)


    return render_template("index.html", 
                           projects=normal_projects, 
                           skills=skills_data)

@app.route("/projects")
def projects_page():
    import json
    import os
    projects_path = os.path.join(app.root_path, 'data', 'projects.json')
    with open(projects_path, 'r') as f:
        projects = json.load(f)
        
    # Categorize Projects
    grouped_projects = {
        "Distributed Systems & Infrastructure": [],
        "AI Research & Engineering": [],
        "Full Stack & Web": []
    }
    
    for p in projects:
        # Determine category based on tags
        tags = p.get('tags', [])
        title = p.get('title', '')
        category = p.get('category', '')
        
        if 'Distributed Systems' in tags or 'Go' in tags or 'Kubernetes' in tags or 'Docker' in tags or 'Kafka' in tags:
             grouped_projects["Distributed Systems & Infrastructure"].append(p)
        elif 'AI' in tags or 'ML' in tags or 'NLP' in tags or 'Research' in tags or category == 'ai':
             grouped_projects["AI Research & Engineering"].append(p)
        else:
             grouped_projects["Full Stack & Web"].append(p)

    return render_template("projects.html", grouped_projects=grouped_projects)

@app.route("/publications")
def publications():
    import json
    import os
    projects_path = os.path.join(app.root_path, 'data', 'projects.json')
    with open(projects_path, 'r') as f:
        projects = json.load(f)

    research_papers = []
    for p in projects:
        if p.get('category') == 'ai' or 'Research' in p.get('tags', []):
             if 'Paper' in p.get('title', '') or 'Research' in p.get('title', '') or 'Defense' in p.get('title', '') or 'Failure' in p.get('title', ''):
                 research_papers.append(p)
                 
    return render_template("publications.html", papers=research_papers)

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
        
        if config.get("cat") in skills_data:
            skills_data[config["cat"]].append(skill_entry)

    # Sort by level descending
    for cat in skills_data:
        skills_data[cat].sort(key=lambda x: x['level'], reverse=True)
        # Deduplicate
        seen = set()
        unique_skills = []
        for s in skills_data[cat]:
            if s['name'] not in seen:
                unique_skills.append(s)
                seen.add(s['name'])
        skills_data[cat] = unique_skills
    
    return render_template("skills.html", skills=skills_data)



@app.route("/about")
def about():
    import json
    import os
    experience_path = os.path.join(app.root_path, 'data', 'experience.json')
    with open(experience_path, 'r') as f:
        experience = json.load(f)
    return render_template("about.html", experience=experience)

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
