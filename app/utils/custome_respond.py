from fastapi import HTTPException
from typing import Any

def response(status_code: int, tag: str, method: str, data: Any = None):
    # Menyesuaikan pesan berdasarkan metode HTTP
    if method == "GET":
        message = f"{tag} retrieved successfully"
    elif method == "POST":
        message = f"{tag} created successfully"
    elif method == "PUT":
        message = f"{tag} updated successfully"
    elif method == "DELETE":
        message = f"{tag} deleted successfully"
    else:
        message = f"{tag} action performed successfully"
    
    # Return the response without the 'data' key if it's None
    response = {
        "status_code": status_code,
        "message": message,
    }

    if data is not None:
        response["data"] = data

    return response
