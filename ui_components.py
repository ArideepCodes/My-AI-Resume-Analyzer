import streamlit as st

def apply_modern_styles():
    """Apply modern styles by loading the CSS file"""
    # Styles are now loaded from style.css in app.py
    pass

def page_header(title, subtitle=None):
    """Render a consistent page header with gradient background"""
    st.markdown(
        f'''
        <div class="page-header">
            <h1 class="header-title">{title}</h1>
            {f'<p class="header-subtitle">{subtitle}</p>' if subtitle else ''}
        </div>
        ''',
        unsafe_allow_html=True
    )

def hero_section(title, subtitle=None, description=None):
    """Render a modern hero section with gradient background and animations"""
    if description and not subtitle:
        subtitle = description
        description = None

    st.markdown(
        f'''
        <div class="page-header hero-header">
            <h1 class="header-title">{title}</h1>
            {f'<div class="header-subtitle">{subtitle}</div>' if subtitle else ''}
            {f'<p class="header-description">{description}</p>' if description else ''}
        </div>
        ''',
        unsafe_allow_html=True
    )

def feature_card(icon, title, description):
    """Render a modern feature card with hover effects"""
    st.markdown(f"""
        <div class="card feature-card">
            <div class="feature-icon icon-pulse">
                <i class="{icon}"></i>
            </div>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)

def about_section(title, description, team_members=None):
    st.markdown(f"""
        <div class="about-section">
            <h2>{title}</h2>
            <p class="about-description">{description}</p>
            <p class="about-description">👨‍💻 Created with ❤️ by <strong>Arideep Kanshabanik</strong></p>
            <p class="about-description">🔗 <a href="https://github.com/ArideepCodes" target="_blank">GitHub: ArideepCodes</a></p>
            {generate_team_section(team_members) if team_members else ''}
        </div>
        <style>
            .about-section {{
                background: linear-gradient(135deg, #2D2D2D 0%, #1E1E1E 100%);
                border-radius: 20px;
                padding: 3rem 2rem;
                margin: 2rem 0;
                position: relative;
                overflow: hidden;
            }}
            .about-section::before {{
                content: '';
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: radial-gradient(circle, rgba(0,180,219,0.1) 0%, transparent 70%);
                animation: rotate 20s linear infinite;
            }}
            .about-section h2 {{
                color: #E0E0E0;
                margin-bottom: 1.5rem;
                font-size: 2rem;
            }}
            .about-description {{
                color: #B0B0B0;
                line-height: 1.6;
                font-size: 1.1rem;
                max-width: 800px;
                margin-bottom: 2rem;
            }}
            .team-section {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1.5rem;
                margin-top: 2rem;
            }}
            .team-member {{
                background: #2D2D2D;
                border-radius: 15px;
                padding: 1.5rem;
                text-align: center;
                border: 1px solid #3D3D3D;
                transition: all 0.3s ease;
            }}
            .team-member:hover {{
                transform: translateY(-5px);
                border-color: #00B4DB;
            }}
            .team-member img {{
                width: 120px;
                height: 120px;
                border-radius: 50%;
                margin-bottom: 1rem;
            }}
            .team-member h3 {{
                color: #E0E0E0;
                margin-bottom: 0.5rem;
            }}
            .team-member p {{
                color: #B0B0B0;
            }}
        </style>
    """, unsafe_allow_html=True)

def generate_team_section(team_members):
    if not team_members:
        return ""
    team_html = '<div class="team-section">'
    for member in team_members:
        team_html += f"""
            <div class="team-member">
                <img src="{member['image']}" alt="{member['name']}">
                <h3>{member['name']}</h3>
                <p>{member['role']}</p>
            </div>
        """
    team_html += '</div>'
    return team_html
