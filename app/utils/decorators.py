from functools import wraps
from flask import request, jsonify
import os

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "secure_admin_token")

def admin_required(func):
    """
    Decorator to ensure that the user is authenticated as an admin.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get the Authorization header
        token = request.headers.get("Authorization")
        if not token or token != f"Bearer {ADMIN_TOKEN}":
            return jsonify({"message": "Admin access required"}), 403
        return func(*args, **kwargs)
    return wrapper

def validate_json(schema):
    """
    Decorator to validate JSON request payloads using a given schema.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Parse and validate the JSON payload
                data = request.get_json()
                errors = schema.validate(data)
                if errors:
                    return jsonify({"message": "Invalid data", "errors": errors}), 400
            except Exception as e:
                return jsonify({"message": "Invalid JSON format", "error": str(e)}), 400
            return func(*args, **kwargs)
        return wrapper
    return decorator
