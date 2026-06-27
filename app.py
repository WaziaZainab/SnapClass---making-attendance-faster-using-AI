import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog


def main():

    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon="https://i.ibb.co/HLRt0Cy4/Logo-Smart-Attend.png"
    )

    if "dialog_opened" not in st.session_state:
        st.session_state.dialog_opened = False

    if "login_type" not in st.session_state:
        st.session_state.login_type = None

    # Save join code before any rerun
    join_code = st.query_params.get("join-code")
    if join_code:
        st.session_state["pending_join_code"] = join_code

    # Always use saved join code
    join_code = st.session_state.get("pending_join_code")

    # Screens
    match st.session_state.login_type:
        case "teacher":
            teacher_screen()

        case "student":
            student_screen()

        case None:
            home_screen()

    

    if join_code:

        # Redirect to student login if needed
        if st.session_state.login_type != "student":
            st.session_state.login_type = "student"
            st.rerun()

        # Show enroll dialog after login
        if (
            st.session_state.get("is_logged_in")
            and st.session_state.get("user_role") == "student"
            and not st.session_state.dialog_opened
        ):
            st.session_state.dialog_opened = True
            auto_enroll_dialog(join_code)

            # Clear after successful dialog
            st.session_state.pop("pending_join_code", None)
            st.query_params.clear()


main()