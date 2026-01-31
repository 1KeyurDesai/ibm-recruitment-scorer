import streamlit as st
import requests
import json

st.set_page_config(
    page_title="HR Recruitment Copilot",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern CSS matching the reference image design
st.markdown("""
    <style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
   
    @keyframes creamGoldGradient {
        0% {
            background-position: 0% 50%;
        }
        25% {
            background-position: 50% 100%;
        }
        50% {
            background-position: 100% 50%;
        }
        75% {
            background-position: 50% 0%;
        }
        100% {
            background-position: 0% 50%;
        }
    }

    html, body, .main, .block-container {
        background: linear-gradient(120deg,
            #fffefb 0%,
            #fffbe9 25%,
            #fff9e3 50%,
            #fff7d6 75%,
            #fffefb 100%
        );
        background-size: 200% 200%;
        animation: creamGoldGradient 52s linear infinite;
        min-height: 100vh;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    .stApp {
        background: linear-gradient(120deg,
            #fffefb 0%,
            #fffbe9 25%,
            #fff9e3 50%,
            #fff7d6 75%,
            #fffefb 100%
        );
        background-size: 200% 200%;
        animation: creamGoldGradient 52s linear infinite;
    }
   
        .stAlert[data-testid="stAlert-error"], .stError, .stAlert[data-testid="stAlert-error"] div, .stAlert[data-testid="stAlert-error"] * {
            background: #fff3f0 !important;
            color: #b00020 !important;
            border: 1.5px solid #ffb3a7 !important;
            font-weight: 700 !important;
            text-shadow: none !important;
        }
    body > div > button[data-testid="baseButton-header"] {
        background: #ffc857 !important;
        color: #3d3d3d !important;
        border: 1px solid #e6b800 !important;
        border-radius: 10px !important;
        box-shadow: 0 2px 6px rgba(255,200,87,0.18) !important;
        opacity: 1 !important;
        filter: none !important;
        mix-blend-mode: normal !important;
        z-index: 9999 !important;
        transition: all 0.25s ease !important;
    }
    body > div > button[data-testid="baseButton-header"]:hover {
        background: #ffd86b !important;
        border-color: #ffd86b !important;
        box-shadow: 0 4px 10px rgba(255,200,87,0.28) !important;
        opacity: 1 !important;
        filter: none !important;
        mix-blend-mode: normal !important;
    }
    /* Sidebar - match main background gradient */
    .stSidebar, 
    .sidebar .sidebar-content,
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div,
    [data-testid="stSidebar"] > div > div,
    section[data-testid="stSidebar"],
    section[data-testid="stSidebar"] > div {
        background: linear-gradient(120deg,
            #fffefb 0%,
            #fffbe9 25%,
            #fff9e3 50%,
            #fff7d6 75%,
            #fffefb 100%
        ) !important;
        background-color: transparent !important;
        background-size: 200% 200% !important;
        animation: creamGoldGradient 52s linear infinite !important;
        border-right: 1px solid rgba(209, 186, 144, 0.08) !important;
        border: none !important;
        border-right: 1px solid rgba(209, 186, 144, 0.08) !important;
        box-shadow: 2px 0 12px rgba(0, 0, 0, 0.01) !important;
    }
    
    .stSidebar *,
    [data-testid="stSidebar"] * {
        border-color: rgba(209, 186, 144, 0.2) !important;
    }
    
    [data-testid="stSidebar"] {
        background: rgba(252, 248, 240, 0.85) !important;
        background-color: rgba(252, 248, 240, 0.85) !important;
    }
   
    @media (max-width: 768px) {
        .stSidebar {
            position: fixed;
            z-index: 999;
        }
        [data-testid="stSidebar"] {
            z-index: 999;
        }
    }
   
    header {
        visibility: visible !important;
        background: transparent !important;
        background-image: none !important;
        border-bottom: 1px solid rgba(209, 186, 144, 0.08);
    }
   
    [data-testid="stHeader"] {
        background: transparent !important;
        background-image: none !important;
    }
   
    button[data-testid="baseButton-header"] {
        background: #ffc857 !important;
        color: #3d3d3d !important;
        border: 1px solid #e6b800 !important;
        border-radius: 10px !important;
        padding: 0.5rem !important;
        box-shadow: 0 2px 6px rgba(255,200,87,0.18) !important;
        transition: all 0.25s ease !important;
        opacity: 1 !important;
        filter: none !important;
        mix-blend-mode: normal !important;
    }

    button[data-testid="baseButton-header"]:hover {
        background: #ffd86b !important;
        border-color: #ffd86b !important;
        box-shadow: 0 4px 10px rgba(255,200,87,0.28) !important;
        transform: translateY(-1px) !important;
        opacity: 1 !important;
        filter: none !important;
        mix-blend-mode: normal !important;
    }

    [data-testid="stHeader"] button {
        background: #ffc857 !important;
        color: #3d3d3d !important;
        border: 1px solid #e6b800 !important;
        border-radius: 10px !important;
        padding: 0.5rem !important;
        box-shadow: 0 2px 6px rgba(255,200,87,0.18) !important;
    }

    [data-testid="stHeader"] button:hover {
        background: #ffd86b !important;
        border-color: #ffd86b !important;
        box-shadow: 0 4px 10px rgba(255,200,87,0.28) !important;
    }
   
    /* Sidebar button icon */
    [data-testid="stHeader"] button svg {
        color: #3d3d3d !important;
        fill: #3d3d3d !important;
    }
   
    /* Sidebar toggle button when sidebar is open */
    .stSidebar [data-testid="baseButton-header"] {
        background: #ffc857 !important;
        color: #3d3d3d !important;
        border: 1px solid #e6b800 !important;
        border-radius: 10px !important;
        box-shadow: 0 2px 6px rgba(255,200,87,0.18) !important;
        transition: all 0.25s ease !important;
    }
    .stSidebar [data-testid="baseButton-header"]:hover {
        background: #ffd86b !important;
        border-color: #ffd86b !important;
        box-shadow: 0 4px 10px rgba(255,200,87,0.28) !important;
    }
    .stSidebar [data-testid="baseButton-header"] svg {
        color: #3d3d3d !important;
        fill: #3d3d3d !important;
    }
   
    /* Sidebar text colors */
    .stSidebar .stMarkdown, .stSidebar p, .stSidebar h1, .stSidebar h2, .stSidebar h3 {
        color: #2d2d2d !important;
    }
    .stSidebar .stSelectbox label {
        color: #2d2d2d !important;
    }
    
    .stSidebar .element-container {
        margin-bottom: 1.5rem;
        background: transparent !important;
    }
    
    .stSidebar h2, .stSidebar h3 {
        margin-top: 0 !important;
        margin-bottom: 1rem !important;
    }
    
    /* Sidebar selectbox container */
    .stSidebar .stSelectbox {
        margin-bottom: 1rem;
    }
    
    .stSidebar hr {
        border-color: rgba(209, 186, 144, 0.2) !important;
        background-color: rgba(209, 186, 144, 0.2) !important;
    }
    
    .stSidebar .css-1d391kg,
    .stSidebar [class*="css-"],
    .stSidebar .element-container,
    .stSidebar [data-testid="stSidebar"] .element-container {
        background: transparent !important;
        background-color: transparent !important;
    }
    
    .stSidebar .stMarkdown {
        background: transparent !important;
        background-color: transparent !important;
    }
    
    .stSidebar .block-container,
    .stSidebar [class*="block-container"] {
        background: transparent !important;
        background-color: transparent !important;
        padding: 0 !important;
    }
    
    /* Sidebar close button styling */
    .stSidebar [data-testid="stSidebar"] button[kind="header"],
    .stSidebar [data-testid="stSidebar"] button[aria-label="Close sidebar"] {
        background: #ffc857 !important;
        color: #2d2d2d !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem !important;
        width: 2.5rem !important;
        height: 2.5rem !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0 2px 6px rgba(255, 200, 87, 0.2) !important;
        margin: 0.5rem !important;
    }
    
    .stSidebar [data-testid="stSidebar"] button[kind="header"]:hover,
    .stSidebar [data-testid="stSidebar"] button[aria-label="Close sidebar"]:hover {
        background: #ffd86b !important;
        box-shadow: 0 4px 10px rgba(255, 200, 87, 0.3) !important;
    }
    
    .stSidebar [data-testid="stSidebar"] button[kind="header"] svg,
    .stSidebar [data-testid="stSidebar"] button[aria-label="Close sidebar"] svg {
        color: #2d2d2d !important;
        fill: #2d2d2d !important;
        width: 1.2rem !important;
        height: 1.2rem !important;
    }
   
    .stButton>button {
        background: linear-gradient(135deg, #ffc857 0%, #ffb84d 100%);
        color: #2d2d2d !important;
        border-radius: 14px;
        font-weight: 600;
        font-size: 1.05rem;
        box-shadow: 0 3px 12px rgba(255, 200, 87, 0.3);
        border: none;
        padding: 0.85rem 1.5rem;
        transition: all 0.3s ease;
        width: 100%;
        letter-spacing: -0.01em;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #ffb84d 0%, #ffc857 100%);
        box-shadow: 0 6px 16px rgba(255, 200, 87, 0.4);
        transform: translateY(-2px);
        color: #2d2d2d !important;
    }
   
    /* Text area */
    .stTextArea textarea {
        border-radius: 16px;
        background: rgba(255, 255, 255, 0.95);
        border: 1.5px solid rgba(209, 186, 144, 0.2);
        font-size: 1rem;
        color: #2d2d2d !important;
        line-height: 1.6;
        padding: 1rem;
        box-shadow:
            0 2px 8px rgba(0, 0, 0, 0.03),
            inset 0 1px 2px rgba(0, 0, 0, 0.02);
        transition: all 0.3s ease;
    }
    .stTextArea textarea:focus {
        border-color: #ffc857;
        background: #ffffff;
        box-shadow:
            0 4px 16px rgba(255, 200, 87, 0.15),
            inset 0 1px 2px rgba(0, 0, 0, 0.02);
        outline: none;
        color: #2d2d2d !important;
    }
    .stTextArea label {
        color: #2d2d2d !important;
        font-weight: 600;
        font-size: 1.1rem;
    }
   
    /* Selectbox styling */
    .stSelectbox>div>div {
        background: #fefcf8 !important;
        border-radius: 14px !important;
        border: 1.5px solid rgba(209, 186, 144, 0.3) !important;
        color: #2d2d2d !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03) !important;
        padding: 0 !important;
        min-height: 3.5rem !important;
        transition: all 0.3s ease !important;
        font-size: 1.05rem !important;
    }
    .stSelectbox input {
        color: #2d2d2d !important;
        background: #fefcf8 !important;
    }
    .stSelectbox [data-baseweb="select"] {
        background: #fefcf8 !important;
        color: #2d2d2d !important;
    }
    .stSelectbox [role="option"] {
        background: #fff !important;
        color: #2d2d2d !important;
    }
   
    .stSelectbox input {
        color: #2d2d2d !important;
        padding: 1rem !important;
        line-height: 1.5 !important;
    }
   
    .stSelectbox [data-baseweb="select"] {
        min-height: 3.5rem !important;
    }
   
    .stSelectbox [data-baseweb="select"] > div {
        padding: 1rem !important;
        min-height: 3.5rem !important;
        align-items: center !important;
        display: flex !important;
    }
   
    /* Selectbox text should be fully visible */
    .stSelectbox [data-baseweb="select"] > div > div {
        line-height: 1.5 !important;
        padding: 0 !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
    }
   
    .stSelectbox [data-baseweb="select"] span {
        line-height: 1.5 !important;
        padding: 0 !important;
        display: block !important;
    }
   
    .stSelectbox [data-baseweb="select"] [class*="singleValue"] {
        line-height: 1.5 !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
        position: relative !important;
    }
   
    .stSelectbox>div>div:focus-within {
        border-color: rgba(209, 186, 144, 0.5);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
    }
    .stSelectbox label {
        color: #2d2d2d !important;
        font-weight: 600;
        font-size: 1.05rem;
    }
   
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown ul, .stMarkdown ol {
        color: #2d2d2d !important;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: #2d2d2d !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-weight: 600;
        letter-spacing: -0.02em;
    }
    .stMarkdown p {
        color: #5a5a5a !important;
        font-size: 1.05em;
        line-height: 1.6;
    }
   
    .stSuccess, .stError, .stInfo, .stWarning,
    .stAlert[data-testid="stAlert-success"], .stAlert[data-testid="stAlert-success"] *,
    .stAlert[data-testid="stAlert-error"], .stAlert[data-testid="stAlert-error"] *,
    .stAlert[data-testid="stAlert-warning"], .stAlert[data-testid="stAlert-warning"] *,
    .stAlert[data-testid="stAlert-info"], .stAlert[data-testid="stAlert-info"] * {
        background: #fff !important;
        color: #222 !important;
        border-radius: 14px !important;
        border: 2px solid #e0e0e0 !important;
        font-weight: 700 !important;
        text-shadow: none !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04) !important;
        opacity: 1 !important;
        filter: none !important;
    }
    .stSuccess *, .stError *, .stInfo *, .stWarning *,
    .stAlert[data-testid="stAlert-success"] *,
    .stAlert[data-testid="stAlert-error"] *,
    .stAlert[data-testid="stAlert-warning"] *,
    .stAlert[data-testid="stAlert-info"] * {
        color: #222 !important;
        opacity: 1 !important;
        filter: none !important;
        text-shadow: none !important;
    }
    /* Add a colored left border for context */
    .stSuccess, .stAlert[data-testid="stAlert-success"], .stAlert[data-testid="stAlert-success"] * {
        border-left: 6px solid #4caf50 !important;
    }
    .stError, .stAlert[data-testid="stAlert-error"], .stAlert[data-testid="stAlert-error"] * {
        border-left: 6px solid #d33d32 !important;
    }
    .stWarning, .stAlert[data-testid="stAlert-warning"], .stAlert[data-testid="stAlert-warning"] * {
        border-left: 6px solid #ffc857 !important;
    }
    .stInfo, .stAlert[data-testid="stAlert-info"], .stAlert[data-testid="stAlert-info"] * {
        border-left: 6px solid #1976d2 !important;
    }
   
    /* Container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem !important;
        max-width: 1400px;
    }
   
    /* Responsive padding */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem;
            padding-bottom: 3rem !important;
        }
    }
   
    /* Metric card styling */
    .metric-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2.5rem 2rem;
        text-align: center;
        border: 1px solid rgba(209, 186, 144, 0.15);
        box-shadow:
            0 6px 24px rgba(0, 0, 0, 0.04),
            inset 0 1px 0 rgba(255, 255, 255, 0.8);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
   
    .metric-card:hover {
        box-shadow:
            0 10px 32px rgba(0, 0, 0, 0.06),
            inset 0 1px 0 rgba(255, 255, 255, 0.9);
        transform: translateY(-3px);
    }
   
    .metric-value {
        font-size: 4rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ffc857 0%, #ffb84d 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
        margin: 1rem 0;
    }
   
    .metric-label {
        font-size: 0.95rem;
        color: #6a6a6a !important;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }
   
    /* Custom divider */
    hr {
        border: none;
        border-top: 1px solid rgba(209, 186, 144, 0.2);
        margin: 2rem 0;
    }
   
    /* Hide default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
   
    [data-baseweb="popover"],
    [data-baseweb="popover"] > *,
    [data-baseweb="popover"] > * > *,
    [data-baseweb="popover"] > * > * > *,
    [data-baseweb="popover"] > * > * > * > *,
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] > *,
    div[data-baseweb="popover"] > * > *,
    div[data-baseweb="popover"] > * > * > *,
    [data-baseweb="menu"],
    [data-baseweb="menu"] > *,
    [data-baseweb="menu"] > * > *,
    [data-baseweb="menu"] > * > * > *,
    div[data-baseweb="menu"],
    div[data-baseweb="menu"] > *,
    div[data-baseweb="menu"] > * > *,
    [role="listbox"],
    [role="listbox"] > *,
    div[role="listbox"],
    div[role="listbox"] > *,
    ul[role="listbox"],
    ul[role="listbox"] > *,
    .stSelectbox [role="listbox"],
    .stSelectbox [role="listbox"] > *,
    .stSelectbox [data-baseweb="popover"],
    .stSelectbox [data-baseweb="popover"] > *,
    .stSelectbox [data-baseweb="popover"] > * > *,
    [data-baseweb="select"] [role="listbox"],
    [data-baseweb="select"] [role="listbox"] > *,
    [data-testid="stAppViewBlockContainer"] [role="menu"],
    [data-testid="stAppViewBlockContainer"] [role="menu"] > *,
    [data-testid="stAppViewBlockContainer"] [data-baseweb="popover"],
    [data-testid="stAppViewBlockContainer"] [data-baseweb="popover"] > * {
        background: #fefcf8 !important;
        background-color: #fefcf8 !important;
        backdrop-filter: blur(20px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
        border: 1.5px solid rgba(209, 186, 144, 0.3) !important;
        border-radius: 14px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12) !important;
        color: #2d2d2d !important;
    }
   
    [role="option"],
    [role="option"] > *,
    li[role="option"],
    li[role="option"] > *,
    div[role="option"],
    div[role="option"] > *,
    [data-baseweb="menu"] li,
    [data-baseweb="menu"] li > *,
    [data-baseweb="menu"] [role="option"],
    [data-baseweb="menu"] [role="option"] > *,
    [data-baseweb="popover"] [role="option"],
    [data-baseweb="popover"] [role="option"] > *,
    .stSelectbox [role="option"],
    .stSelectbox [role="option"] > *,
    [data-baseweb="select"] [role="option"],
    [data-baseweb="select"] [role="option"] > *,
    [data-testid="stAppViewBlockContainer"] [role="menuitem"],
    [data-testid="stAppViewBlockContainer"] [role="menuitem"] > *,
    [data-testid="stAppViewBlockContainer"] [role="option"],
    [data-testid="stAppViewBlockContainer"] [role="option"] > * {
        background: transparent !important;
        background-color: transparent !important;
        color: #2d2d2d !important;
        padding: 0.875rem 1.25rem !important;
        transition: all 0.2s ease !important;
        border-radius: 8px !important;
        margin: 0.25rem 0.5rem !important;
    }
   
    [role="option"]:hover,
    [role="option"]:hover > *,
    li[role="option"]:hover,
    li[role="option"]:hover > *,
    div[role="option"]:hover,
    div[role="option"]:hover > *,
    [data-baseweb="menu"] li:hover,
    [data-baseweb="menu"] li:hover > *,
    [data-baseweb="menu"] [role="option"]:hover,
    [data-baseweb="menu"] [role="option"]:hover > *,
    [data-baseweb="popover"] [role="option"]:hover,
    [data-baseweb="popover"] [role="option"]:hover > *,
    .stSelectbox [role="option"]:hover,
    .stSelectbox [role="option"]:hover > *,
    [data-baseweb="select"] [role="option"]:hover,
    [data-baseweb="select"] [role="option"]:hover > *,
    [data-testid="stAppViewBlockContainer"] [role="menuitem"]:hover,
    [data-testid="stAppViewBlockContainer"] [role="menuitem"]:hover > *,
    [data-testid="stAppViewBlockContainer"] [role="option"]:hover,
    [data-testid="stAppViewBlockContainer"] [role="option"]:hover > * {
        background: rgba(255, 200, 87, 0.2) !important;
        background-color: rgba(255, 200, 87, 0.2) !important;
        color: #1a1a1a !important;
    }
   
    [role="option"][aria-selected="true"],
    [role="option"][aria-selected="true"] > *,
    li[role="option"][aria-selected="true"],
    li[role="option"][aria-selected="true"] > *,
    div[role="option"][aria-selected="true"],
    div[role="option"][aria-selected="true"] > *,
    [data-baseweb="menu"] [role="option"][aria-selected="true"],
    [data-baseweb="menu"] [role="option"][aria-selected="true"] > *,
    [data-baseweb="popover"] [role="option"][aria-selected="true"],
    [data-baseweb="popover"] [role="option"][aria-selected="true"] > *,
    .stSelectbox [role="option"][aria-selected="true"],
    .stSelectbox [role="option"][aria-selected="true"] > *,
    [data-baseweb="select"] [role="option"][aria-selected="true"],
    [data-baseweb="select"] [role="option"][aria-selected="true"] > * {
        background: rgba(255, 200, 87, 0.25) !important;
        background-color: rgba(255, 200, 87, 0.25) !important;
        color: #1a1a1a !important;
        font-weight: 600 !important;
    }
   
    [data-baseweb="popover"] *,
    [data-baseweb="popover"] * *,
    [data-baseweb="menu"] *,
    [data-baseweb="menu"] * *,
    [role="listbox"] *,
    [role="listbox"] * *,
    [role="option"] *,
    [role="option"] * * {
        color: #2d2d2d !important;
    }
   
    button[data-testid="baseButton-header"] {
        background: #ffc857 !important;
        color: #3d3d3d !important;
        border: 1px solid #e6b800 !important;
        border-radius: 10px !important;
        box-shadow: 0 2px 6px rgba(255,200,87,0.18) !important;
        transition: all 0.25s ease !important;
    }
    button[data-testid="baseButton-header"]:hover {
        background: #ffd86b !important;
        border-color: #ffd86b !important;
        box-shadow: 0 4px 10px rgba(255,200,87,0.28) !important;
    }
   
    /* Responsive columns */
    @media (max-width: 768px) {
        [data-testid="column"] {
            width: 100% !important;
            padding: 0.5rem;
        }
    }
   
    label {
        color: #2d2d2d !important;
    }
   
    /* Input text colors */
    input, textarea, select {
        color: #2d2d2d !important;
    }
   
    /* Empty state message styling */
    .empty-state {
        background: linear-gradient(135deg, rgba(255, 248, 225, 0.95) 0%, rgba(255, 243, 196, 0.95) 100%);
        backdrop-filter: blur(10px);
        border-radius: 18px;
        padding: 2.5rem 2rem;
        margin: 2rem 0;
        border: 1px solid rgba(255, 200, 87, 0.2);
        box-shadow: 0 4px 20px rgba(255, 200, 87, 0.1);
        text-align: center;
    }
   
    .empty-state-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
   
    .empty-state-title {
        color: #2d2d2d !important;
        font-size: 1.4rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }
   
    .empty-state-text {
        color: #5a5a5a !important;
        font-size: 1.05rem !important;
        line-height: 1.6 !important;
    }
   
    /* Skills tags */
    .skill-tag {
        display: inline-block;
        background: rgba(255, 200, 87, 0.15);
        color: #d97706;
        padding: 0.5rem 1.1rem;
        border-radius: 14px;
        margin: 0.3rem;
        font-size: 0.95rem;
        font-weight: 500;
        border: 1px solid rgba(255, 200, 87, 0.3);
    }
   
    /* Analysis section */
    .analysis-section {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(209, 186, 144, 0.15);
    }
   
    /* Sidebar icon color */
    .stSidebar svg, .stSidebar [data-testid="stSidebar"] svg {
        color: #ffc857 !important;
        fill: #ffc857 !important;
    }
    
    .stSidebar,
    .stSidebar > *,
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > *,
    [data-testid="stSidebar"] > * > *,
    .css-1d391kg,
    .css-17eq0hr,
    [class*="sidebar"] {
        background: linear-gradient(120deg,
            #fff8e8 0%,
            #fffbe6 25%,
            #ffe9b0 50%,
            #ffd86b 75%,
            #fff8e8 100%
        ) !important;
        background-size: 200% 200% !important;
        animation: creamGoldGradient 52s linear infinite !important;
    }
    
    .stSidebar,
    [data-testid="stSidebar"],
    .stSidebar * {
        border-color: rgba(209, 186, 144, 0.2) !important;
        outline-color: rgba(209, 186, 144, 0.2) !important;
    }
   
    ::placeholder {
        color: #a0a0a0 !important;
        opacity: 1;
    }
   
    /* Selection color */
    ::selection {
        background: rgba(255, 200, 87, 0.3);
    }
   
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
   
    ::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, 0.02);
        border-radius: 10px;
    }
   
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 200, 87, 0.3);
        border-radius: 10px;
        transition: all 0.3s ease;
    }
   
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 200, 87, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Configuration - Flask API endpoint
FLASK_API_URL = "http://localhost:5000/score_candidate"

# Function to call Flask API
def score_candidate(resume_text, job_desc):
    """Call the Flask backend API to score a candidate"""
    try:
        response = requests.post(
            FLASK_API_URL,
            json={
                "resume_text": resume_text,
                "job_desc": job_desc
            },
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to backend: {str(e)}")
        return None


# Sidebar - True white card using st.container()
job_roles = {
    "Python Developer": "Looking for Python, Flask, SQL experience",
    "Data Scientist": "Looking for Python, ML, statistics background",
    "Frontend Developer": "Looking for React, UI/UX skills",
    "Full Stack Developer": "Looking for React, Node.js, databases",
    "DevOps Engineer": "Looking for AWS, Docker, Kubernetes",
}

with st.sidebar:
    st.markdown(
        """
        <style>
        /* Make the sidebar background transparent */
        section[data-testid="stSidebar"] {
            background: transparent !important;
        }
        section[data-testid="stSidebar"] > div > div > div:first-child {
            background: #fff !important;
            border-radius: 18px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.05);
            padding: 2.2rem 1.2rem 2rem 1.2rem;
            margin: 2.2rem 0 2.5rem 0;
        }
        section[data-testid="stSidebar"]::-webkit-scrollbar {
            width: 12px;
            background: transparent;
        }
        section[data-testid="stSidebar"]::-webkit-scrollbar-thumb {
            background: rgba(0,0,0,0.08);
            border-radius: 8px;
        }
        section[data-testid="stSidebar"]::-webkit-scrollbar-track {
            background: transparent;
        }
        /* For Firefox */
        section[data-testid="stSidebar"] {
            scrollbar-color: rgba(0,0,0,0.08) transparent;
            scrollbar-width: thin;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        section[data-testid="stSidebar"]::-webkit-scrollbar {
            display: none;
            width: 0 !important;
            background: transparent !important;
        }
        section[data-testid="stSidebar"] {
            scrollbar-width: none !important; /* Firefox */
            -ms-overflow-style: none !important; /* IE and Edge */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        "<div style='color: #222; font-weight: 700; font-size: 1.18rem; margin-bottom: 1.2rem; letter-spacing: -0.01em; text-align: center;'>Job Role</div>",
        unsafe_allow_html=True
    )
    selected_job = st.selectbox(
        "Select Job Role",
        job_roles.keys(),
        label_visibility="visible",
        key="sidebar_job_select2"
    )
    st.markdown(
        f"""
        <div style='margin-top: 1.2rem;'>
            <div style='font-size: 0.78rem; color: #888; font-weight: 700; text-transform: uppercase; letter-spacing: 0.09em; margin-bottom: 0.4rem; text-align: left;'>Role Description</div>
            <div style='color: #333; font-size: 1.01rem; line-height: 1.6; padding: 0.4rem 0 0.2rem 0; text-align: left;'>{job_roles[selected_job]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Main content
st.markdown("<h1 style='text-align: center; font-size: 2.8rem; margin-bottom: 0.5rem; margin-top: 1rem;'>HR Recruitment Copilot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6a6a6a; font-size: 1.2rem; margin-bottom: 2.5rem; font-weight: 400;'>Recruitment scorer using IBM watsonx Orchestrate</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📄 Candidate Resume")
    resume_text = st.text_area(
        "Resume Input",
        height=300,
        placeholder="Paste the candidate's resume text here...\n\nInclude:\n• Work experience\n• Skills and technologies\n• Education background\n• Projects and achievements",
        label_visibility="collapsed",
        help="Enter the complete resume text for comprehensive analysis"
    )
    st.markdown("</div>", unsafe_allow_html=True)
   
    # Instructions card
    st.markdown("""
    <div style='
        background: rgba(33, 150, 243, 0.08);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 1.2rem;
        margin-top: 1rem;
        border: 1px solid rgba(33, 150, 243, 0.15);
    '>
        <div style='font-weight: 600; color: #1565c0; margin-bottom: 0.5rem;'>💡 Quick Tips</div>
        <ul style='margin: 0; padding-left: 1.2rem; color: #4a4a4a; font-size: 0.95rem; line-height: 1.6;'>
            <li>Paste complete resume text for best results</li>
            <li>Include all technical skills and experience</li>
            <li>The AI will match against selected job role</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 📊 Candidate Analysis")
   
    analyze = st.button("🔍 Analyze Candidate", use_container_width=True)
   
    if analyze:
        if not resume_text or resume_text.strip() == "":
            st.markdown("""
            <div class="empty-state">
                <div class="empty-state-icon">📝</div>
                <div class="empty-state-title">Resume Required</div>
                <div class="empty-state-text">Please paste the candidate's resume text in the input field to begin the AI-powered analysis.</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Get job description from selected job
            job_desc = job_roles[selected_job]
            
            # Show loading spinner
            with st.spinner("Analyzing candidate profile..."):
                # Call Flask API
                result = score_candidate(resume_text, job_desc)
            
            if result:
                score = result.get('score', 0)
                decision = result.get('decision', 'Unknown')
                explanation = result.get('explanation', 'No explanation provided')
                
                # Determine decision color and icon
                if decision == "Shortlist":
                    decision_color = "#449747"
                    decision_icon = "✓"
                    decision_text = "Shortlisted"
                elif decision == "Reject":
                    decision_color = "#d33d32"
                    decision_icon = "✗"
                    decision_text = "Rejected"
                else:
                    decision_color = "#df911d"
                    decision_icon = "⚠"
                    decision_text = decision
                
                # Fit Score Card
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">Overall Fit Score</div>
                    <div class="metric-value">{score}<span style='font-size: 2rem; opacity: 0.7;'>%</span></div>
                    <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.08);'>
                        <div style='color: {decision_color}; font-weight: 600; font-size: 1.1rem;'>{decision_icon} {decision_text}</div>
                        <div style='color: #6a6a6a; font-size: 0.95rem; margin-top: 0.3rem;'>{explanation}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Display decision with appropriate styling
                if decision == "Shortlist":
                    st.success(f"✅ **Decision:** {decision_text} - {explanation}")
                elif decision == "Reject":
                    st.error(f"❌ **Decision:** {decision_text} - {explanation}")
                else:
                    st.warning(f"⚠️ **Decision:** {decision_text} - {explanation}")
                
                # Additional analysis section
                st.markdown("""
                <div class='analysis-section'>
                    <div style='font-weight: 600; color: #2d2d2d; margin-bottom: 0.8rem; font-size: 1.1rem;'>📋 Analysis Details</div>
                    <div style='color: #4a4a4a; line-height: 1.7;'>
                        The candidate's resume has been analyzed against the selected job role requirements.<br>
                        The fit score is calculated based on keyword matching between the resume and job description.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("❌ **Error:** Could not connect to the backend API. Please ensure the Flask server is running on http://localhost:5000")
   
    else:
        st.markdown("""
        <div style='
            background: rgba(255, 255, 255, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 3rem 2rem;
            text-align: center;
            border: 2px dashed rgba(255, 200, 87, 0.3);
            margin-top: 2rem;
        '>
            <div style='font-size: 4rem; margin-bottom: 1rem; opacity: 0.6;'>🎯</div>
            <div style='color: #6a6a6a; font-size: 1.1rem; line-height: 1.6;'>
                Paste a resume and click<br><strong style='color: #2d2d2d;'>Analyze Candidate</strong> to get started
            </div>
        </div>
        """, unsafe_allow_html=True)
   
    st.markdown("</div>", unsafe_allow_html=True)