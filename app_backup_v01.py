
import streamlit as st

# ==========================================
# LIFE OS - APPLICATION FOUNDATION
# Version 0.1
# ==========================================

st.set_page_config(
    page_title="LIFE OS | Personal Intelligence",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------
# CUSTOM DESIGN SYSTEM
# ------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

.stApp {
    background: #090D16;
    color: #E8EDF7;
    font-family: 'DM Sans', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

[data-testid="stSidebar"] {
    background: #0D1422;
    border-right: 1px solid #202B3E;
}

[data-testid="stSidebar"] p {
    color: #A9B5C9;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif;
    color: #F2F5FC;
}

.os-brand {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 27px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #F4F7FF;
}

.os-subtitle {
    color: #8290A8;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.os-card {
    background: linear-gradient(
        145deg,
        #141F32,
        #101827
    );
    border: 1px solid #26344B;
    border-radius: 14px;
    padding: 22px;
    min-height: 145px;
}

.os-card-title {
    color: #94A3B8;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.os-card-value {
    color: #F1F5F9;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 25px;
    font-weight: 600;
    margin-top: 14px;
}

.os-card-note {
    color: #71819B;
    font-size: 12px;
    margin-top: 8px;
}

.os-accent {
    color: #8B9FFF;
}

.os-divider {
    border-bottom: 1px solid #26344B;
    margin: 25px 0;
}

.os-tag {
    display: inline-block;
    padding: 6px 11px;
    border-radius: 20px;
    background: #172A35;
    color: #65D6B0;
    font-size: 11px;
    letter-spacing: 1px;
}

.stButton > button {
    border-radius: 9px;
    border: 1px solid #354968;
    background: #182740;
    color: #E8EDF7;
}

.stButton > button:hover {
    border-color: #8298FF;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ------------------------------------------
# SIDEBAR
# ------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="os-brand">◈ LIFE OS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="os-subtitle">Personal Intelligence System</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="os-divider"></div>',
                unsafe_allow_html=True)

    st.caption("WORKSPACE")

    selected_page = st.radio(
        "Navigation",
        [
            "Command Center",
            "Goal Intelligence",
            "Career Intelligence",
            "Project Portfolio",
            "Decision Lab",
            "Daily Intelligence",
            "Personal Analytics"
        ],
        label_visibility="collapsed"
    )

    st.markdown('<div class="os-divider"></div>',
                unsafe_allow_html=True)

    st.caption("SYSTEM")

    st.markdown(
        '<span class="os-tag">DEVELOPMENT MODE</span>',
        unsafe_allow_html=True
    )

    st.markdown("")
    st.caption("LIFE OS · Version 0.1")


# ------------------------------------------
# MAIN HEADER
# ------------------------------------------

st.markdown(
    '<div class="os-subtitle">PERSONAL DECISION INTELLIGENCE</div>',
    unsafe_allow_html=True
)

if selected_page == "Command Center":

    st.title("Your Command Center")

    st.markdown(
        "A unified view of your goals, capabilities, "
        "projects and personal progress."
    )

    st.markdown('<div class="os-divider"></div>',
                unsafe_allow_html=True)

    st.markdown("### Your Intelligence Overview")

    st.info(
        "Your personal workspace is being configured. "
        "Connect your LIFE OS account in the next development step."
    )

    col1, col2, col3, col4 = st.columns(4)

    cards = [
        (col1, "ACTIVE GOALS", "—", "Awaiting account connection"),
        (col2, "SKILLS TRACKED", "—", "Awaiting account connection"),
        (col3, "ACTIVE PROJECTS", "—", "Awaiting account connection"),
        (col4, "DECISIONS LOGGED", "—", "Awaiting account connection")
    ]

    for column, title, value, note in cards:

        with column:
            st.markdown(
                f"""
                <div class="os-card">
                    <div class="os-card-title">{title}</div>
                    <div class="os-card-value">{value}</div>
                    <div class="os-card-note">{note}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("")
    st.markdown("### Your Personal Intelligence")

    left, right = st.columns(2)

    with left:
        with st.container(border=True):
            st.markdown("#### Career Intelligence")
            st.write(
                "Understand your current capabilities, "
                "identify skill gaps and evaluate career readiness."
            )
            st.caption("Module awaiting development")

    with right:
        with st.container(border=True):
            st.markdown("#### Goal Intelligence")
            st.write(
                "Turn long-term ambitions into measurable "
                "goals, milestones and progress."
            )
            st.caption("Module awaiting development")

    st.markdown("")
    st.markdown("### System Status")

    st.markdown(
        '<span class="os-tag">INTERFACE INITIALIZED</span>',
        unsafe_allow_html=True
    )

    st.caption(
        "Database integration, authentication and live analytics "
        "will be connected in subsequent development steps."
    )


# ------------------------------------------
# OTHER MODULES
# ------------------------------------------

else:

    st.title(selected_page)

    module_descriptions = {
        "Goal Intelligence":
            "Manage goals, deadlines, milestones and measurable progress.",

        "Career Intelligence":
            "Evaluate skills, career readiness and professional gaps.",

        "Project Portfolio":
            "Document projects, achievements and practical evidence.",

        "Decision Lab":
            "Structure important decisions, alternatives and outcomes.",

        "Daily Intelligence":
            "Understand daily activities, routines and productivity.",

        "Personal Analytics":
            "Explore your personal performance through interactive analytics."
    }

    st.markdown(
        module_descriptions.get(selected_page, "")
    )

    st.markdown('<div class="os-divider"></div>',
                unsafe_allow_html=True)

    st.info(
        "This module is part of the LIFE OS development roadmap. "
        "Its functional implementation will follow."
    )


# ------------------------------------------
# FOOTER
# ------------------------------------------

st.markdown('<div class="os-divider"></div>',
            unsafe_allow_html=True)

st.caption(
    "LIFE OS | Personal Decision Intelligence System | "
    "Built for measurable personal growth."
)
