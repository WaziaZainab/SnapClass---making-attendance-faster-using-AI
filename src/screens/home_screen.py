import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():

    st.markdown("""
<style>
div.stButton > button {
    background-color: #39FF14;
    color: black;
    font-weight: 700;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

    style_background_home()
    style_base_layout()
    header_home()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="portal-card">
            <div class="small-text">I'm a</div>
            <div class="student-title">Student</div>
        """, unsafe_allow_html=True)

        st.image(
            "https://i.ibb.co/844D9Lrt/mascot-student.png",
              width=120
        )

        if st.button(
            "🎓 Student Panel →",
            key="student_btn",
            use_container_width=True
            
        ):
            st.session_state['login_type'] = 'student'
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="portal-card">
            <div class="small-text">I'm a</div>
            <div class="teacher-title">Teacher</div>
        """, unsafe_allow_html=True)

        st.image(
            "https://i.ibb.co/CsmQQV6X/mascot-prof.png",
              width=145
        )

        if st.button(
            "👩‍🏫 Teacher Panel →",
            key="teacher_btn",
            use_container_width=True
        ):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    footer_home()