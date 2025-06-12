from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from datetime import datetime

app = Flask(__name__)

os.makedirs("checklists", exist_ok=True)

@app.route("/")
def home():
    return render_template("home.html", active_page="home")

@app.route("/home")
def home_redirect():
    return render_template("home.html", active_page="home")

@app.route("/pack_list")
def pack_list():
    return render_template("pack_list.html", active_page="pack_list")

@app.route("/robot_checklist", methods=["GET", "POST"])
def robot_checklist():
    return render_template("robot_checklist.html", active_page="robot_checklist")

@app.route("/battery_manager")
def battery_manager():
    return render_template("battery_manager.html", active_page="battery_manager")

@app.route("/login")
def login():
    return render_template("login.html", active_page="login")

@app.route("/settings")
def settings():
    return render_template("settings.html", active_page="settings")

@app.route("/save_robot_checklist", methods=["POST"])
def save_robot_checklist():
    data = request.json.get("data", [])
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_path = "checklists"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"robot_checklist_{now}.txt")
    with open(file_path, "w") as f:
        for line in data:
            f.write(line + "\n")
    return "", 200

@app.route("/save_pack_list", methods=["POST"])
def save_pack_list():
    data = request.json.get("data", [])
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_path = "packlists"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"pack_list_{now}.txt")
    with open(file_path, "w") as f:
        for line in data:
            f.write(line + "\n")
    return "", 200

if __name__ == "__main__":
    app.run(debug=True, port=5002)
