# Simulated "session" (global state)
authenticated_users = set()

# The decorator
def login_required(func):
    def wrapper(username, *args, **kwargs):
        if username not in authenticated_users:
            print(f"Access denied for '{username}'. Please log in.")
            return
        return func(username, *args, **kwargs)
    return wrapper

# Simulate a login function
def login(username):
    authenticated_users.add(username)
    print(f"{username} logged in successfully!")

# A protected function
@login_required
def view_dashboard(username):
    print(f"Welcome to your dashboard, {username}!")

# ----- Testing -----
view_dashboard("alice")       # ❌ Not logged in
login("alice")                # ✅ Login
view_dashboard("alice")       # ✅ Access granted
