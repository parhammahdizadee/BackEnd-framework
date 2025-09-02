from . import users_v1_router

@users_v1_router.get("/hello")
def read_root_v1():
    """Returns a welcome message for the v1 API."""
    return {"message": "Welcome to Version 1 of the API!"}
