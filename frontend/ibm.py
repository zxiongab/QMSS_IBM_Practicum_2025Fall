import streamlit as st

def set_page(page):
    st.session_state['page'] = page

if 'page' not in st.session_state:
    st.session_state['page'] = 'welcome'

# --- GLOBAL STYLES ---
st.markdown("""
    <style>
    /* Hide main menu (hamburger), footer, and top black header */
    [data-testid="stHeader"] {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background-color: #fff !important;
    }
    .sidebar-title {
        color: #2356C5 !important;
        font-weight: 700;
        margin-bottom: 2.5rem;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #fff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BUTTON COLOR DEFINITIONS ---
nav_active_bg = "#2356C5"
nav_active_text = "#E3ECFD"
nav_inactive_bg = "#E3ECFD"
nav_inactive_text = "#2356C5"

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 class='sidebar-title'>EPLC Assistant</h2>", unsafe_allow_html=True)
    page_now = st.session_state['page']
    ask_active = page_now == 'question'
    doc_active = page_now == 'document'

    # "Ask a Question" navigation button
    if st.button("Ask a Question", key="sidebar_ask"):
        set_page('question')
    st.markdown(f"""
        <style>
          button[data-testid="baseButton-sidebar_ask"] {{
            width: 100% !important;
            background-color: {nav_active_bg if ask_active else nav_inactive_bg};
            color: {nav_active_text if ask_active else nav_inactive_text};
            font-weight:600;
            border-radius:8px;
            height:44px;
            margin-bottom:14px;
            border:none;
            transition: background 0.2s, color 0.2s;
          }}
        </style>
    """, unsafe_allow_html=True)

    # "Create a Document" navigation button
    if st.button("Create a Document", key="sidebar_doc"):
        set_page('document')
    st.markdown(f"""
        <style>
          button[data-testid="baseButton-sidebar_doc"] {{
            width: 100% !important;
            background-color: {nav_active_bg if doc_active else nav_inactive_bg};
            color: {nav_active_text if doc_active else nav_inactive_text};
            font-weight:600;
            border-radius:8px;
            height:44px;
            margin-bottom:24px;
            border:none;
            transition: background 0.2s, color 0.2s;
          }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("---", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("Help", "https://your-help-link.com")
    with col2:
        st.markdown(
            """
            <a href="https://github.com/XinleiCheng/QMSS_IBM_Practicum_2025Fall" target="_blank">
                <button style="
                    width:100%;height:36px;border:none;border-radius:8px;
                    background-color:#E3ECFD;color:#2356C5;
                    font-weight:600;font-size:15px;cursor:pointer;">
                    GitHub
                </button>
            </a>
            """, unsafe_allow_html=True
        )

# --- MAIN NAVIGATION BUTTONS ---
def render_nav_buttons():
    page_now = st.session_state['page']
    ask_active = page_now == 'question'
    doc_active = page_now == 'document'
    cols = st.columns([1, 1])
    with cols[0]:
        if st.button("Ask a Question", key="main_ask"):
            set_page('question')
        st.markdown(f"""
            <style>
              button[data-testid="baseButton-main_ask"] {{
                width: 100% !important;
                background-color: {nav_active_bg if ask_active else nav_inactive_bg};
                color: {nav_active_text if ask_active else nav_inactive_text};
                font-weight:600;
                border-radius:8px;
                height:44px;
                border:none;
                transition: background 0.2s, color 0.2s;
              }}
            </style>
        """, unsafe_allow_html=True)
    with cols[1]:
        if st.button("Create a Document", key="main_doc"):
            set_page('document')
        st.markdown(f"""
            <style>
              button[data-testid="baseButton-main_doc"] {{
                width: 100% !important;
                background-color: {nav_active_bg if doc_active else nav_inactive_bg};
                color: {nav_active_text if doc_active else nav_inactive_text};
                font-weight:600;
                border-radius:8px;
                height:44px;
                border:none;
                transition: background 0.2s, color 0.2s;
              }}
            </style>
        """, unsafe_allow_html=True)

# --- MAIN PAGE LOGIC ---
if st.session_state['page'] == 'welcome':
    st.markdown("""
        <div style='text-align:center;margin-top:120px;'>
            <h1 style='font-weight:700;color:#2356C5;'>EPLC Assistant</h1>
            <h3 style='font-weight:400; margin-bottom:40px;color:#2356C5;'>
                Empowering IT Project Managers with smarter, faster documentation.
            </h3>
        </div>
        """, unsafe_allow_html=True
    )
    render_nav_buttons()

elif st.session_state['page'] == 'question':
    st.markdown("""
        <div style='text-align:center;margin-top:100px;'>
            <h2 style='font-weight:700;margin-bottom:32px;color:#2356C5;'>Try Asking...</h2>
        </div>
        """, unsafe_allow_html=True
    )
    render_nav_buttons()
    st.markdown("""
        <div style='text-align:center; margin-bottom:20px;'>
            <button style='background-color:#EEF1F8; color:#2356C5; border:none; border-radius:18px; padding:7px 19px; margin-right:10px; font-size:15px;'>What is the EPLC Initial Phase?</button>
            <button style='background-color:#EEF1F8; color:#2356C5; border:none; border-radius:18px; padding:7px 19px; margin-right:10px; font-size:15px;'>Show me a CDC UP template for planning.</button>
            <button style='background-color:#EEF1F8; color:#2356C5; border:none; border-radius:18px; padding:7px 19px; font-size:15px;'>Explain the difference between initiation and planning phases.</button>
        </div>
        <div style='text-align:center;'>
            <input type='text' style='width:380px;height:38px;border-radius:8px;border:1px solid #dee2e6;font-size:16px;padding-left:12px;color:#2356C5;background:#fff;' placeholder='Type your question here...'>
            <button style='background-color:#2356C5; color:#E3ECFD;border:none;border-radius:7px;height:38px;width:34px;font-size:18px;font-weight:600;margin-left:12px;'>&uarr;</button>
        </div>
        """, unsafe_allow_html=True
    )

elif st.session_state['page'] == 'document':
    st.markdown("""
        <div style='text-align:center;margin-top:80px;'>
            <h3 style='font-weight:700; margin-bottom:34px;color:#2356C5;'>Which Phase are you in?</h3>
            <div style='display:flex;justify-content:center;flex-wrap:wrap;gap:18px;'>
                <button style='background-color:#FFF; color:#2356C5; border:none; border-radius:18px; padding:10px 34px; font-size:15px;margin-right:15px; box-shadow:0px 2px 6px rgba(0,0,0,0.08);'>Design</button>
                <button style='background-color:#FFF; color:#2356C5; border:none; border-radius:18px; padding:10px 34px; font-size:15px;margin-right:15px; box-shadow:0px 2px 6px rgba(0,0,0,0.08);'>Development</button>
                <button style='background-color:#FFF; color:#2356C5; border:none; border-radius:18px; padding:10px 34px; font-size:15px;margin-right:15px; box-shadow:0px 2px 6px rgba(0,0,0,0.08);'>Implementation</button>
                <button style='background-color:#FFF; color:#2356C5; border:none; border-radius:18px; padding:10px 34px; font-size:15px; box-shadow:0px 2px 6px rgba(0,0,0,0.08);'>Requirement</button>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    render_nav_buttons()
