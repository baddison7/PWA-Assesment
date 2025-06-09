from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    tabs = [
        {"label": "Home", "endpoint": "home"},
    ]
    return render_template("home.html", active_page="home", tabs=tabs, current_tab="Home")

@app.route("/home")
def home_redirect():
    tabs = [
        {"label": "Home", "endpoint": "home"},
    ]
    return render_template("home.html", active_page="home", tabs=tabs, current_tab="Home")


@app.route("/pack_list")
def pack_list():
    tabs = [
        {"label": "Pack List", "endpoint": "pack_list"},
    ]
    return render_template("pack_list.html", active_page="pack_list", tabs=tabs, current_tab="Pack List")

@app.route("/robot_checklist")
def robot_checklist():
    tabs = [
        {"label": "Robot Checklist", "endpoint": "robot_checklist"},
    ]
    return render_template("robot_checklist.html", active_page="robot_checklist", tabs=tabs, current_tab="Robot Checklist")

@app.route("/battery_manager")
def battery_manager():
    tabs = [
        {"label": "Battery manager", "endpoint": "battery_manager"},
    ]
    return render_template("battery_manager.html", active_page="battery_manager", tabs=tabs, current_tab="Battery manager")


@app.route("/login")
def login():
    tabs = [
        {"label": "Login", "endpoint": "login"},
        {"label": "Profile", "endpoint": "login"},
    ]
    return render_template("login.html", active_page="login", tabs=tabs, current_tab="Login")

@app.route("/settings")
def settings():
    tabs = [
        {"label": "Settings", "endpoint": "settings"},
    ]
    return render_template("settings.html", active_page="settings", tabs=tabs, current_tab="Settings")

if __name__ == "__main__":
    app.run(debug=True)
