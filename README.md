# Prime Portfolio

A futuristic, high-performance personal portfolio website built with Flask and Tailwind CSS. Designed to showcase projects and skills with a premium, dynamic aesthetic.

![Portfolio Preview](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg) *(Replace with actual screenshot)*

## 🚀 Features

*   **Futuristic Design**: Glassmorphism, neon accents, and smooth animations.
*   **Dynamic Content**: Projects and skills are loaded dynamically from JSON data.
*   **Interactive UI**: 3D tilt effects, hover animations, and responsive layout.
*   **Skill Visualization**: Automatic skill categorization and level calculation based on project tags.
*   **Contact Form**: Functional contact form that saves messages locally (extensible to email).

## 🛠️ Tech Stack

*   **Backend**: Python, Flask
*   **Frontend**: HTML5, Tailwind CSS, JavaScript
*   **Styling**: Custom CSS for advanced effects (glassmorphism, animations)
*   **Icons**: Devicon
*   **Deployment**: Vercel (Ready)

## 📂 Project Structure

```
my-portfolio/
├── app.py              # Main Flask application
├── data/               # JSON data for projects and experience
│   ├── projects.json
│   └── experience.json
├── static/             # Static assets
│   ├── css/
│   ├── js/
│   └── img/
├── templates/          # HTML templates
├── requirements.txt    # Python dependencies
└── vercel.json         # Vercel deployment config
```

## ⚡ Quick Start

### Prerequisites

*   Python 3.8+
*   Git

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/abishekgiri/my-portfolio.git
    cd my-portfolio
    ```

2.  **Create a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application**
    ```bash
    python3 app.py
    ```

5.  **Visit the site**
    Open [http://localhost:5050](http://localhost:5050) in your browser.

## 🌍 Deployment

This project is configured for easy deployment on **Vercel**.

1.  Push your code to GitHub.
2.  Import the repository on Vercel.
3.  Vercel will automatically detect the `vercel.json` and deploy.

See `deployment_guide.md` for more details.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---
© 2025 Abishek Kumar Giri
