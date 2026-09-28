"""
Reusable UI components for the portfolio.
"""
import streamlit as st
from streamlit_lottie import st_lottie
from core.data import PERSONAL_INFO, SOCIAL_LINKS
from core.local_storage import save_contact_to_file


def render_hero_section(lottie_animation):
    """Render the hero/introduction section."""
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown(f'<h1 class="hero-title">Hello, I\'m<br>{PERSONAL_INFO["name"]}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-subtitle">{PERSONAL_INFO["title"]} at <a href="{PERSONAL_INFO["company_url"]}" target="_blank">{PERSONAL_INFO["company"]}</a></p>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size: 1.1rem; font-weight: 500; background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">{PERSONAL_INFO["tagline"]}</p>', unsafe_allow_html=True)
        
        st.markdown("")
        col_btn1, col_btn2 = st.columns(2)
        
        # with col_btn1:
        #     if st.button("Contact Me", width="stretch"):
        #         st.session_state.selected = "Contact"
        #         st.rerun()
        
        # with col_btn2:
        #     try:
        #         with open("./cv/resume.pdf", "rb") as pdf_file:
        #             st.download_button(
        #                 label="Resume",
        #                 data=pdf_file,
        #                 file_name="resume.pdf",
        #                 mime="application/pdf",
        #                 width="stretch"
        #             )
        #     except FileNotFoundError:
        #         st.button("Resume", width="stretch", disabled=True)
    
    with col2:
        if lottie_animation:
            st_lottie(lottie_animation, height=350, key="hero-animation")
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_about_section():
    """Render the about me section."""
    st.markdown(f"""
    <div class="custom-card">
        <h3>About Me</h3>
        <p style="line-height: 1.8; color: #d1d5db;">{PERSONAL_INFO["bio"]}</p>
    </div>
    """, unsafe_allow_html=True)


def render_timeline_item(experience):
    """Render a single work experience timeline item."""
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-company">{experience['company']}</div>
        <div class="timeline-position">{experience['position']}</div>
        <div class="timeline-duration">{experience['duration']}</div>
        <p style="color: #d1d5db; margin-bottom: 1rem;">{experience['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if experience.get('achievements'):
        st.markdown("**Key Achievements:**")
        for achievement in experience['achievements']:
            st.markdown(f"- {achievement}")
    
    # if experience.get('tech_stack'):
    #     st.markdown("**Tech Stack:**")
    #     tech_html = " ".join([f'<span class="tech-badge">{tech}</span>' for tech in experience['tech_stack']])
    #     st.markdown(tech_html, unsafe_allow_html=True)


def render_work_experience(experiences):
    """Render the work experience section."""
    for exp in experiences:
        render_timeline_item(exp)
        st.markdown("<br>", unsafe_allow_html=True)


def render_project_card(project):
    """Render a single project card."""
    st.markdown(f"""
    <div class="project-card">
        <div class="project-title">{project['name']}</div>
        <p style="color: #d1d5db; line-height: 1.6; margin-bottom: 1rem;">{project['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if project.get('highlights'):
        st.markdown("**Highlights:**")
        for highlight in project['highlights']:
            st.markdown(f"- {highlight}")
    
    st.markdown("")
    
    # Tech stack badges
    if project.get('tech_stack'):
        tech_html = " ".join([f'<span class="tech-badge">{tech}</span>' for tech in project['tech_stack']])
        st.markdown(tech_html, unsafe_allow_html=True)
    
    st.markdown("")
    
    # Links
    cols = st.columns(4)
    with cols[0]:
        if project.get('github'):
            st.markdown(f"[GitHub]({project['github']})")
    with cols[1]:
        if project.get('demo'):
            st.markdown(f"[Demo]({project['demo']})")
    
    st.markdown("<br>", unsafe_allow_html=True)


def get_proficiency_level(value):
    """Convert numeric value to proficiency level."""
    if value >= 90:
        return "Expert", "#10b981"  # Green
    elif value >= 80:
        return "Advanced", "#6366f1"  # Blue
    elif value >= 70:
        return "Intermediate", "#a855f7"  # Purple
    else:
        return "Beginner", "#9ca3af"  # Gray


def render_skill_badges(skills_dict, category):
    """Render skills as clean badges."""
    st.markdown(f"### {category}")
    st.markdown("")
    
    # Create a grid of skill badges
    skills_html = '<div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 1.5rem;">'
    
    for skill in skills_dict.keys():
        # Simple skill badge HTML
        skills_html += f'''
        <div style="
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(168, 85, 247, 0.1) 100%);
            border: 1px solid #6366f1;
            border-radius: 8px;
            padding: 0.65rem 1.25rem;
            display: inline-flex;
            align-items: center;
            transition: all 0.3s ease;
        ">
            <span style="
                font-weight: 500;
                font-size: 0.95rem;
                color: #fafafa;
            ">{skill}</span>
        </div>
        '''
    
    skills_html += '</div>'
    st.markdown(skills_html, unsafe_allow_html=True)


def render_skills_section(skills_data):
    """Render the skills section with badge display."""
    # st.markdown("""
    # <div class="custom-card">
    # """, unsafe_allow_html=True)
    
    for category, skills_dict in skills_data.items():
        # Category heading with gradient
        st.markdown(f"""
        <h3 style="
            background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
        ">{category}</h3>
        """, unsafe_allow_html=True)
        
        # Skills as badges
        skills_html = " ".join([f'<span class="tech-badge">{skill}</span>' for skill in skills_dict.keys()])
        st.markdown(skills_html, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)




def render_education_card(edu):
    """Render an education card."""
    status_badge = "Completed" if edu['status'] == "Completed" else "Pursuing"
    
    st.markdown(f"""
    <div class="custom-card">
        <h4>{edu['degree']}</h4>
        <p style="color: #6366f1; font-weight: 500;">{edu['institution']}</p>
        <p style="color: #9ca3af;">{status_badge}</p>
    </div>
    """, unsafe_allow_html=True)


def render_certification_card(cert):
    """Render a certification card."""
    st.markdown(f"""
    <div class="custom-card">
        <h4><a style="color: #fafafa; text-decoration: none;">
            {cert['name']} 
        </a></h4>
        <p style="color: #6366f1; font-weight: 500;">{cert['issuer']}</p>

    """, unsafe_allow_html=True)
    
    if cert.get('skills'):
        skills_html = " ".join([f'<span class="tech-badge">{skill}</span>' for skill in cert['skills']])
        st.markdown(skills_html, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)


def render_contact_form():
    """Render a contact form with local file storage."""
    st.markdown("""
    <div class="custom-card">
        <h3>Get In Touch</h3>
        <p style="color: #d1d5db;">Feel free to reach out for collaborations, opportunities, or just a chat!</p>
        <br>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name *", placeholder="Your full name")
        email = st.text_input("Email *", placeholder="your.email@example.com")
        subject = st.text_input("Subject", placeholder="What is this about?")
        message = st.text_area("Message *", height=150, placeholder="Your message here...")
        
        submitted = st.form_submit_button("Send Message", width="stretch")
        
        if submitted:
            # Validate fields
            if not name or not email or not message:
                st.error("Please fill in all required fields (Name, Email, Message).")
            elif "@" not in email or "." not in email:
                st.error("Please enter a valid email address.")
            else:
                # Save to local file
                with st.spinner("Saving your message..."):
                    success, result_message = save_contact_to_file(
                        name=name,
                        email=email,
                        subject=subject,
                        message=message
                    )
                
                if success:
                    st.success("Thank you for reaching out! I'll get back to you soon.")
                    # st.balloons()
                else:
                    st.error(f"{result_message}")
                    st.info(f"""
                    If the error persists, please reach me directly at **{PERSONAL_INFO.get('email', 'you@example.com')}**
                    """)


def render_social_links():
    """Render social media links."""
    st.markdown("### Connect With Me")
    
    cols = st.columns(4)
    
    with cols[0]:
        if SOCIAL_LINKS.get('linkedin'):
            st.markdown(f"""
            <a href="{SOCIAL_LINKS['linkedin']}" target="_blank" class="social-link">
                LinkedIn
            </a>
            """, unsafe_allow_html=True)
    
    with cols[1]:
        if SOCIAL_LINKS.get('github'):
            st.markdown(f"""
            <a href="{SOCIAL_LINKS['github']}" target="_blank" class="social-link">
                GitHub
            </a>
            """, unsafe_allow_html=True)
    
    with cols[2]:
        if SOCIAL_LINKS.get('email'):
            st.markdown(f"""
            <a href="{SOCIAL_LINKS['email']}" class="social-link">
                Email
            </a>
            """, unsafe_allow_html=True)
    
    with cols[3]:
        if SOCIAL_LINKS.get('twitter'):
            st.markdown(f"""
            <a href="{SOCIAL_LINKS['twitter']}" target="_blank" class="social-link">
                Twitter
            </a>
            """, unsafe_allow_html=True)


def render_footer():
    """Render the footer."""
    # st.markdown("---")
    st.markdown(f"""
    <div class="footer">
        <p>© 2024 {PERSONAL_INFO['name']}. Built with Streamlit.</p>
        <p>
            <a href="{SOCIAL_LINKS.get('github', '#')}">GitHub</a> • 
            <a href="{SOCIAL_LINKS.get('linkedin', '#')}">LinkedIn</a> • 
            <a href="{SOCIAL_LINKS.get('email', '#')}">Email</a>
        </p>
    </div>
    """, unsafe_allow_html=True)
