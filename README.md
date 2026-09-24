# 💼 Streamlit Portfolio Template

A modern, customizable portfolio/resume website template built with Streamlit, featuring interactive components, responsive design, and seamless Docker deployment.

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51.0-red.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)

## ✨ Features

- 🎨 **Modern Design**: Professional dark theme with gradient accents
- 📱 **Responsive Layout**: Optimized for all screen sizes
- 🔄 **Interactive Components**: Lottie animations, an experience timeline, skill badges, and a contact form
- 🚀 **Fast Performance**: Optimized loading and rendering
- 🐳 **Docker Ready**: Self-contained image for deployment, plus a Compose setup for live editing
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

```bash
docker compose up --build
```

- Access at: `http://localhost:8081`
- The project folder is mounted into the container, so edits show up without rebuilding the image
- Streamlit reloads the app on save (`runOnSave = true` in `.streamlit/config.toml`)

### Docker Production

The image is self-contained (code included), so you can run it anywhere without Compose:

```bash
docker build -t portfolio:latest .
docker run -p 8501:8501 portfolio:latest
```

- Access at: `http://localhost:8501`
- Rebuild the image after changing code or content

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
# Start with live editing (http://localhost:8081)
docker compose up --build

# Run in the background / stop
docker compose up -d
docker compose down

# View logs
docker compose logs -f portfolio

# Standalone production image (http://localhost:8501)
docker build -t portfolio:latest .
docker run -p 8501:8501 portfolio:latest
```

## 🛠️ Technology Stack

- **Frontend Framework**: Streamlit 1.51.0
- **Programming Language**: Python 3.12
- **Charts**: Plotly 5.17.0 (installed and ready to use; not wired into any section yet)
- **Animations**: Lottie Files (streamlit-lottie)
- **Navigation**: streamlit-option-menu
- **Containerization**: Docker & Docker Compose

## 📝 Development Workflow

1. **Start** the app with `docker compose up --build` (or `streamlit run app.py`)
2. **Make changes** to any `.py` file or to `core/data.py`
3. **Save**: Streamlit reloads automatically
4. **Test** at `http://localhost:8081` (Compose) or `http://localhost:8501` (local)
5. **Deploy** the standalone image built from the `Dockerfile`

## 🌐 Deployment

### Deploy to Cloud Platform

The portfolio can be deployed to various platforms:

**Streamlit Cloud:**
```bash
# Push to GitHub, then connect repository to streamlit.io
```

**Heroku:**
```bash
# Heroku needs a Procfile that binds Streamlit to its $PORT
echo 'web: streamlit run app.py --server.port $PORT --server.address 0.0.0.0' > Procfile
heroku create your-portfolio
git push heroku main
```

**AWS/GCP/Azure:**
- Use the standalone Docker image (`docker build -t portfolio:latest .`)
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
