# 💼 Streamlit Portfolio Template

A modern, customizable portfolio/resume website template built with Streamlit, featuring interactive components, responsive design, and seamless Docker deployment.

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51.0-red.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)

## ✨ Features

- 🎨 **Modern Design**: Professional dark theme with gradient accents
- 📱 **Responsive Layout**: Optimized for all screen sizes
- 🔄 **Interactive Components**: Animated charts, timelines, and visualizations
- 🚀 **Fast Performance**: Optimized loading and rendering
- 🐳 **Docker Ready**: Easy deployment with Docker and Docker Compose
- 📊 **Data-Driven**: Separated data from presentation logic
- 🎯 **Section Navigation**: Sidebar menu for easy browsing

## 🏗️ Project Structure

```
streamlit-portfolio-template/
├── app.py                  # Main application entry point
├── core/
│   ├── components.py       # Reusable UI components
│   ├── data.py            # Portfolio content data
│   ├── enums.py           # Lottie animations and constants
│   ├── styles.py          # Custom CSS styles
│   └── local_storage.py   # Contact form submission storage
├── .streamlit/
│   └── config.toml        # Streamlit theme configuration
├── cv/
│   └── resume.pdf         # Your resume PDF (add your own)
├── lottiefiles/           # Animation files
├── scripts/
│   └── entrypoint.sh      # Docker entrypoint script
├── Dockerfile             # Docker image definition
├── docker-compose.yml     # Docker compose configuration
└── requirements.txt       # Python dependencies
```

## 🚀 Quick Start

### Local Development (without Docker)

1. **Clone the repository**
   ```bash
   git clone https://github.com/sumit-kumar-03/streamlit-portfolio-template.git
   cd streamlit-portfolio-template
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   ```
   http://localhost:8501
   ```

### Docker Development (Recommended)

1. **Start development server with hot reload**
   ```bash
   docker-compose up portfolio-dev
   ```
   - Access at: `http://localhost:8501`
   - Auto-reloads on code changes
   - Volume-mounted for live editing

2. **Build and run**
   ```bash
   docker-compose build
   docker-compose up
   ```

### Docker Production

1. **Start production server**
   ```bash
   docker-compose --profile production up portfolio-prod
   ```
   - Access at: `http://localhost:8081`
   - Optimized for performance
   - No hot reload

2. **Or run standalone**
   ```bash
   docker build -t portfolio:prod .
   docker run -p 8501:8501 portfolio:prod
   ```

## 🎨 Customization

### Update Personal Information

Edit `core/data.py` to customize your portfolio content:

```python
PERSONAL_INFO = {
    "name": "Your Name",
    "title": "Your Title",
    "email": "your.email@example.com",
    # ... more fields
}
```

### Modify Theme Colors

Edit `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#6366f1"       # Main accent color
backgroundColor = "#0e1117"     # Background
secondaryBackgroundColor = "#1a1d24"
textColor = "#fafafa"
```

### Add Projects, Experience, or Skills

Update the respective sections in `core/data.py`:
- `WORK_EXPERIENCE`
- `PROJECTS`
- `SKILLS`
- `EDUCATION`
- `CERTIFICATIONS`

## 📦 Docker Commands

```bash
# Development mode (hot reload)
docker-compose up portfolio-dev

# Production mode
docker-compose --profile production up portfolio-prod

# Build only
docker-compose build

# Stop all services
docker-compose down

# View logs
docker-compose logs -f portfolio-dev

# Rebuild and start
docker-compose up --build
```

## 🛠️ Technology Stack

- **Frontend Framework**: Streamlit 1.51.0
- **Programming Language**: Python 3.12
- **Visualization**: Plotly 5.17.0
- **Animations**: Lottie Files (streamlit-lottie)
- **Navigation**: streamlit-option-menu
- **Containerization**: Docker & Docker Compose

## 📝 Development Workflow

1. **Make changes** to any `.py` file in the project
2. **Changes auto-reload** if using `portfolio-dev` service
3. **Test locally** at `http://localhost:8501`
4. **Commit** when satisfied
5. **Deploy** using production Docker configuration

## 🌐 Deployment

### Deploy to Cloud Platform

The portfolio can be deployed to various platforms:

**Streamlit Cloud:**
```bash
# Push to GitHub, then connect repository to streamlit.io
```

**Heroku:**
```bash
heroku create your-portfolio
git push heroku main
```

**AWS/GCP/Azure:**
- Use the production Docker image
- Deploy to container services (ECS, Cloud Run, etc.)

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ✏️ Make It Yours

1. Replace the placeholder content in `core/data.py` with your own details.
2. Update the intro text in `core/enums.py` (`InfoSection`).
3. Drop your resume into `cv/resume.pdf` (and uncomment the Resume button in `core/components.py`).
4. Tweak theme colors in `.streamlit/config.toml`.

---

**Built with ❤️ using Streamlit**
