import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# Import custom modules
from core.enums import Graphic
from core.styles import get_custom_css
from core.components import (
    render_hero_section,
    render_about_section,
    render_work_experience,
    render_project_card,
    render_skills_section,
    render_education_card,
    render_certification_card,
    render_contact_form,
    render_social_links,
    render_footer
)
from core.data import (
    PERSONAL_INFO,
    WORK_EXPERIENCE,
    PROJECTS,
    SKILLS,
    EDUCATION,
    CERTIFICATIONS
)

# Page configuration (must be first Streamlit command)
st.set_page_config(
    page_title=f"{PERSONAL_INFO['name']} - Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# SEO and meta tags
st.markdown(f"""
<meta name="description" content="{PERSONAL_INFO['tagline']} - {PERSONAL_INFO['title']} portfolio.">
<meta name="keywords" content="Portfolio, Resume, Software Engineer, Streamlit">
<meta name="author" content="{PERSONAL_INFO['name']}">
<meta property="og:title" content="{PERSONAL_INFO['name']} - Professional Portfolio">
<meta property="og:description" content="{PERSONAL_INFO['tagline']}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{PERSONAL_INFO['name']} - Portfolio">
<meta name="twitter:description" content="{PERSONAL_INFO['tagline']}">
""", unsafe_allow_html=True)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.markdown(f"## {PERSONAL_INFO['name']}")
    st.markdown(f"*{PERSONAL_INFO['title']}*")
    st.markdown("---")
    
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "About", "Experience", "Projects", "Skills", "Education", "Certifications", "Contact"],
        icons=["house", "person", "briefcase", "rocket", "code-slash", "mortarboard", "award", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#6366f1", "font-size": "18px"},
            "nav-link": {
                "font-size": "14px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#1a1d24",
                "border-radius": "8px",
                "padding": "10px"
            },
            "nav-link-selected": {"background-color": "#6366f1"},
        }
    )
    
    st.markdown("")
    st.markdown("---")
    st.caption(f"© {PERSONAL_INFO['name']}")

# Main content area
if selected == "Home":
    # Hero Section
    render_hero_section(Graphic.coding_boy.value)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # About Me section
    st.markdown(f"""
    <div class="custom-card">
        <h3>About Me</h3>
        <p style="line-height: 1.8; color: #d1d5db;">{PERSONAL_INFO["bio"]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # # Featured Projects Preview
    # st.markdown("## Featured Projects")
    # cols = st.columns(2)
    # featured_projects = PROJECTS[:2]
    # for idx, project in enumerate(featured_projects):
    #     with cols[idx % 2]:
    #         render_project_card(project)
    
    # if st.button("View All Projects →", key="view_all_projects"):
    #     st.session_state.selected = "Projects"
    #     st.rerun()

elif selected == "About":
    st.markdown("# About Me")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="custom-card">
            <h2>Hello! I'm {PERSONAL_INFO['name']}</h2>
            <p style="font-size: 1.2rem; color: #6366f1; margin-bottom: 1.5rem;">
                {PERSONAL_INFO['tagline']}
            </p>
            <p style="line-height: 1.8; color: #d1d5db; font-size: 1.05rem;">
                {PERSONAL_INFO['bio']}
            </p>
            <br>
            <h3>What I Do</h3>
            <ul style="line-height: 2; color: #d1d5db;">
                <li>Build scalable backend systems and microservices</li>
                <li>Design and implement RESTful APIs</li>
                <li>Develop data processing pipelines</li>
                <li>Containerize applications with Docker</li>
                <li>Deploy solutions on cloud platforms (AWS)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st_lottie(Graphic.coding_boy.value, height=400, key="about-animation")
        
        st.markdown("### Location")
        st.info(PERSONAL_INFO['location'])
        
        st.markdown("### Current Role")
        st.info(f"{PERSONAL_INFO['title']} at {PERSONAL_INFO['company']}")

elif selected == "Experience":
    st.markdown("# Work Experience")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        render_work_experience(WORK_EXPERIENCE)
    
    with col2:
        # Quick Stats
        st.markdown(f"""
        <div class="custom-card" style="text-align: center;">
            <h3>Quick Stats</h3>
            <h2 style="color: #6366f1;">{PERSONAL_INFO['years_of_experience']}</h2>
            <p>Years of Experience</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st_lottie(Graphic.tech_stack.value, height=300, key="experience-animation")
        
        st.markdown("""
        <div class="custom-card">
            <h3>Expertise Areas</h3>
            <ul style="line-height: 2; color: #d1d5db;">
                <li>Backend Engineering</li>
                <li>Distributed Systems</li>
                <li>Microservices Architecture</li>
                <li>GenAI & LLM Integration</li>
                <li>Systems & Performance</li>
                <li>Cloud Infrastructure</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown("# Projects")
    st.markdown("---")
    
    st.markdown("""
    Here are some of my notable projects that showcase my skills in software development, 
    system design, and problem-solving.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    for project in PROJECTS:
        render_project_card(project)

elif selected == "Skills":
    st.markdown("# Technical Skills")
    st.markdown("---")
    
    # Centered animation at the top
    col_center = st.columns([1, 2, 1])
    with col_center[1]:
        st_lottie(Graphic.tech_stack.value, height=350, key="skills-animation")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Skills badges below
    render_skills_section(SKILLS)

elif selected == "Education":
    st.markdown("# Education")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        for edu in EDUCATION:
            render_education_card(edu)
            st.markdown("<br>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="custom-card">
            <h3>Focus Areas</h3>
            <ul style="line-height: 2; color: #d1d5db;">
                <li>Backend Engineering</li>
                <li>Distributed Systems</li>
                <li>GenAI & LLM Integration</li>
                <li>Cloud Infrastructure</li>
                <li>Systems Performance</li>
                <li>Data Architecture</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif selected == "Certifications":
    st.markdown("# Certifications")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        for cert in CERTIFICATIONS:
            render_certification_card(cert)
            st.markdown("<br>", unsafe_allow_html=True)
    
    with col2:
        st_lottie(Graphic.certifications.value, height=300, key="cert-animation")
        
        st.markdown("""
        <div class="custom-card">
            <h3>Continuous Learning</h3>
            <p style="color: #d1d5db; line-height: 1.8;">
                I believe in continuous learning and regularly update my skills 
                through online courses, certifications, and hands-on projects.
            </p>
        </div>
        """, unsafe_allow_html=True)

elif selected == "Contact":
    st.markdown("# Contact Me")
    st.markdown("---")
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        render_contact_form()
    
    with col2:
        
        st.markdown("""
        <div class="custom-card">
            <h3>Direct Email</h3>
            <p style="color: #6366f1; font-size: 1.1rem;">{}</p>
            <br>
            <br>
        </div>
        """.format(PERSONAL_INFO.get('email', 'you@example.com')), unsafe_allow_html=True)

# Footer (on all pages)
render_footer()