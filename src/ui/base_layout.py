import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

            .stApp {
                background:
                    radial-gradient(circle at top,
                    #1E1B4B 0%,
                    #0F172A 45%,
                    #020617 100%) !important;
            }

            .stApp div[data-testid="stColumn"]{
                background: rgba(30, 41, 59, 0.72) !important;
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);

                padding: 2rem !important;
                border-radius: 2rem !important;

                border: 1px solid rgba(255,255,255,0.08);

                box-shadow:
                    0 8px 32px rgba(0,0,0,0.35),
                    0 0 25px rgba(99,102,241,0.12);

                transition: all 0.3s ease;
            }

            .stApp div[data-testid="stColumn"]:hover{
                transform: translateY(-4px);
                box-shadow:
                    0 15px 40px rgba(0,0,0,0.45),
                    0 0 35px rgba(99,102,241,0.20);
            }
                
            

        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>

            .stApp {
                background:
                    radial-gradient(circle at top,
                    #1E1B4B 0%,
                    #0F172A 45%,
                    #020617 100%) !important;
            }

        </style>
    """, unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        #MainMenu,
        footer,
        header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 2rem !important;
        }

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3rem !important;
            line-height: 1 !important;
            margin-bottom: 0 !important;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 1 !important;
            margin-bottom: 0 !important;
        }

        h3,
        h4,
        p {
            font-family: 'Outfit', sans-serif !important;
            color: white !important;
        }

        .small-text {
            color: #94A3B8;
            font-size: 1rem;
            text-align: center;
            margin-bottom: 0.4rem;
        }

        .student-title,
        .teacher-title {
            color: #FFFFFF;
            font-size: 2rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 1rem;
        }

        button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

        .stButton > button:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow:
                0 15px 35px rgba(99,102,241,0.45);
        }

        .stTextInput input,
        .stSelectbox div[data-baseweb="select"],
        .stTextArea textarea {
            background: #1E293B !important;
            color: #F8FAFC !important;
            border-radius: 16px !important;
            border: 1px solid #334155 !important;
        }

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-thumb {
            background: #6366F1;
            border-radius: 10px;
        }
                
    

/* 🌙 STRONG POPUP / TOAST DARK FIX */
div[data-testid="stToast"],
div[data-testid="toastContainer"],
div[role="alert"],
.stAlert {
    background-color: #1E293B !important;
    color: #F8FAFC !important;
    border: 1px solid #334155 !important;
    border-radius: 16px !important;
    box-shadow: 0 12px 35px rgba(0,0,0,0.6) !important;
}

/* ✍️ INPUT PLACEHOLDER FIX */
input::placeholder {
    color: #22c55e !important;
    opacity: 1 !important;
}

/* ✍️ TEXTAREA PLACEHOLDER FIX */
textarea::placeholder {
    color: #38bdf8 !important;
    opacity: 1 !important;
}

/* 🔥 Streamlit input override extra strong */
.stTextInput input {
    background: #1E293B !important;
    color: #F8FAFC !important;
}

                
        /* 🧊 REMOVE WHITE BACKGROUND ISSUE (SAFE WAY) */

        .stApp > div {
            background: transparent !important;
        }

        /* 📦 ONLY CONTENT TEXT STYLING (NO BOX BREAK) */
        /* h1, h2, h3, h4, p, span, label {  color: #F8FAFC !important;}*/

        /* 🧾 INPUT + CARD KEEP DARK WITHOUT BREAKING LAYOUT */
        .stTextInput input,
        .stSelectbox div[data-baseweb="select"],
        .stTextArea textarea {
            background: #1E293B !important;
            color: #F8FAFC !important;
            border-radius: 14px !important;
            border: 1px solid #334155 !important;
        }
        
        /* FORCE DARK DIALOG */

div[data-testid="stDialog"] {
    background: #0F172A !important;
}

div[data-testid="stDialog"] > div {
    background: #0F172A !important;
}

div[role="dialog"] {
    background: #0F172A !important;
}

div[role="dialog"] > div {
    background: #0F172A !important;
}

div[role="dialog"] section {
    background: #0F172A !important;
}
        </style>
    """, unsafe_allow_html=True)