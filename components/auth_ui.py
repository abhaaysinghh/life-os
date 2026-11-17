import streamlit as st
from core.auth import register_user, login_user


def show_auth_screen(supabase):

    st.markdown(
        "<h1 style='text-align:center;'>◈ LIFE OS</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:#8290A8;'>"
        "YOUR LIFE. YOUR DATA. YOUR DECISIONS."
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    _, center, _ = st.columns([1, 1.5, 1])

    with center:

        tab_login, tab_signup = st.tabs(["Login", "Create Account"])

        with tab_login:

            st.subheader("Welcome back")

            email = st.text_input(
                "Email address",
                key="login_email"
            )

            password = st.text_input(
                "Password",
                type="password",
                key="login_password"
            )

            if st.button("Sign In", use_container_width=True):

                if not email or not password:
                    st.error("Enter your email and password.")

                else:
                    try:
                        result = login_user(supabase, email, password)

                        if result.session is None:
                            st.error(
                                "Login requires email confirmation. "
                                "Check your inbox."
                            )
                        else:
                            st.session_state.user = result.user
                            st.session_state.session = result.session
                            st.success("Login successful.")
                            st.rerun()

                    except Exception:
                        st.error(
                            "Login failed. Check your credentials "
                            "and email confirmation."
                        )

        with tab_signup:

            st.subheader("Create your account")

            full_name = st.text_input(
                "Full name",
                key="signup_name"
            )

            email = st.text_input(
                "Email address",
                key="signup_email"
            )

            password = st.text_input(
                "Create password",
                type="password",
                key="signup_password"
            )

            confirm_password = st.text_input(
                "Confirm password",
                type="password",
                key="signup_confirm"
            )

            if st.button("Create Account", use_container_width=True):

                if not full_name or not email or not password:
                    st.error("Complete all required fields.")

                elif password != confirm_password:
                    st.error("Passwords do not match.")

                elif len(password) < 8:
                    st.error("Password must contain at least 8 characters.")

                else:
                    try:
                        result = register_user(
                            supabase,
                            full_name,
                            email,
                            password
                        )

                        if result.session is None:
                            st.success(
                                "Account created. Check your email "
                                "to confirm your account, then log in."
                            )
                        else:
                            st.session_state.user = result.user
                            st.session_state.session = result.session
                            st.success("Account created successfully.")
                            st.rerun()

                    except Exception:
                        st.error(
                            "Registration failed. Check your email "
                            "or try another address."
                        )
