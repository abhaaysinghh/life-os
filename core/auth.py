def register_user(supabase, full_name, email, password):
    return supabase.auth.sign_up({
        "email": email,
        "password": password,
        "options": {
            "data": {
                "full_name": full_name
            }
        }
    })


def login_user(supabase, email, password):
    return supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })


def logout_user(supabase):
    return supabase.auth.sign_out()
