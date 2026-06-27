import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time


@st.dialog("Enroll in Subject")
def enroll_dialog():

    # ✅ CLEAN CSS (NO CONFLICT)
    st.markdown("""
    <style>

    /* Overlay */
    div[data-testid="stDialog"] {
        background: rgba(0,0,0,0.65) !important;
    }

    /* Popup Box */
    div[data-testid="stDialog"] > div {
        background: #0F172A !important;
        border-radius: 16px !important;
        width: 380px !important;
        padding: 22px !important;
        box-shadow: 0 20px 50px rgba(0,0,0,0.6) !important;
    }

    /* Input */
    div[data-testid="stTextInput"] input {
        background: #1E293B !important;
        color: #F8FAFC !important;
        border: 2px solid #EB459E !important;
        border-radius: 10px !important;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: #94A3B8 !important;
    }

    /* Label */
    div[data-testid="stTextInput"] label {
        color: #EB459E !important;
        font-weight: 600 !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown(
        "<h3 style='text-align:center;color:#EB459E;'>Enroll in Subject</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:#CBD5E1;'>Enter subject code</p>",
        unsafe_allow_html=True
    )

    # INPUT
    join_code = st.text_input(
        "Subject Code",
        placeholder="e.g. ECS604",
        key="subject_code_input"
    )

    # BUTTON
    if st.button("Enroll Now", use_container_width=True):

        if not join_code.strip():
            st.warning("Please enter a subject code")
            return

        res = (
            supabase.table("subjects")
            .select("subject_id, name, subject_code")
            .eq("subject_code", join_code.strip())
            .execute()
        )

        if not res.data:
            st.error("Invalid subject code")
            return

        subject = res.data[0]
        student_id = st.session_state.student_data["student_id"]

        check = (
            supabase.table("subject_students")
            .select("*")
            .eq("subject_id", subject["subject_id"])
            .eq("student_id", student_id)
            .execute()
        )

        if check.data:
            st.warning("Already enrolled")
            return

        enroll_student_to_subject(student_id, subject["subject_id"])

        st.success("Enrolled successfully!")

        time.sleep(1)
        st.rerun()