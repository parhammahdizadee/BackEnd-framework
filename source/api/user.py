from routers import router_v1

@router_v1.get("/")
def read_root_v1():
    """Returns a welcome message for the v1 API."""
    return {"message": "Welcome to Version 1 of the API!"}
