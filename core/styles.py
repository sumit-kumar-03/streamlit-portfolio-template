"""
Custom CSS styles for professional portfolio appearance.
"""

def get_custom_css():
    """Returns custom CSS for the portfolio."""
    return """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main container */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Headers with gradient */
    h1, h2, h3 {
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
    }
    
    /* Hero section */
    .hero-section {
        padding: 3rem 0;
        text-align: center;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #9ca3af;
        margin-bottom: 2rem;
    }
    
    /* Card styling */
    .custom-card {
        background: linear-gradient(135deg, #1a1d24 0%, #262b36 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #2d3748;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(99, 102, 241, 0.2);
        border-color: #6366f1;
    }
    
    /* Timeline styling */
    .timeline-item {
        position: relative;
        padding-left: 2rem;
        margin-bottom: 2rem;
        border-left: 2px solid #6366f1;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -6px;
        top: 0;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #6366f1;
        box-shadow: 0 0 10px rgba(99, 102, 241, 0.5);
    }
    
    .timeline-company {
        font-size: 1.2rem;
        font-weight: 600;
        color: #fafafa;
        margin-bottom: 0.5rem;
    }
    
    .timeline-position {
        color: #6366f1;
        font-weight: 500;
        margin-bottom: 0.3rem;
    }
    
    .timeline-duration {
        color: #9ca3af;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    /* Project card */
    .project-card {
        background: linear-gradient(135deg, #1a1d24 0%, #262b36 100%);
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid #2d3748;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(99, 102, 241, 0.25);
        border-color: #6366f1;
    }
    
    .project-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #fafafa;
    }
    
    .tech-badge {
        display: inline-block;
        background: rgba(99, 102, 241, 0.1);
        color: #6366f1;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.3rem 0.3rem 0.3rem 0;
        font-size: 0.85rem;
        border: 1px solid rgba(99, 102, 241, 0.3);
    }
    
    /* Social links */
    .social-links {
        display: flex;
        gap: 1rem;
        justify-content: center;
        margin: 2rem 0;
    }
    
    .social-link {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
        display: inline-block;
    }
    
    .social-link:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(99, 102, 241, 0.4);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(99, 102, 241, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5);
    }
    
    /* Download button */
    .stDownloadButton > button {
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(99, 102, 241, 0.3);
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5);
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #6366f1, transparent);
        margin: 2rem 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        border-top: 1px solid #2d3748;
        color: #9ca3af;
    }
    
    .footer a {
        color: #6366f1;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .footer a:hover {
        color: #a855f7;
    }
    
    /* Skill progress bar */
    .skill-bar {
        background: #2d3748;
        border-radius: 10px;
        height: 8px;
        margin: 0.5rem 0;
        overflow: hidden;
    }
    
    .skill-progress {
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
        height: 100%;
        border-radius: 10px;
        transition: width 1s ease;
    }
    
    /* Contact form */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #1a1d24;
        border: 1px solid #2d3748;
        border-radius: 8px;
        color: #fafafa;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #6366f1;
        box-shadow: 0 0 0 1px #6366f1;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1d24 0%, #0e1117 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2rem;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
        }
    }
    
    /* Smooth page transitions */
    .main .block-container {
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Loading animation for charts */
    .stPlotlyChart {
        animation: slideIn 0.6s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Improve tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 8px;
        padding: 10px 20px;
        color: #9ca3af;
        border: 1px solid transparent;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(168, 85, 247, 0.2) 100%);
        color: #6366f1;
        border-color: #6366f1;
    }
    
    /* Skill badge hover effects */
    div[style*="flex-wrap: wrap"] > div {
        cursor: default;
    }
    
    div[style*="flex-wrap: wrap"] > div:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.3);
    }
    
    /* Improve scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1d24;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #6366f1 0%, #a855f7 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #7c7ff5 0%, #b865f9 100%);
    }
    </style>
    """
