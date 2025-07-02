from flask import jsonify

def login(data):
    if data.get("username") == "admin" and data.get("password") == "123456":
        return jsonify({"status": "success"})
    return jsonify({"status": "fail"}), 401