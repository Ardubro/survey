import uuid

from django.http import HttpRequest, HttpResponse


def is_valid_uuid4(uuid_raw: str) -> bool:
    """Checks if uuid found in cookie is valid."""
    try:
        uuid_str = str(uuid_raw)
        uuid.UUID(uuid_str, version=4)
        return True
    except (TypeError, ValueError):
        return False


def user_id_get_or_create(request: HttpRequest) -> bool:
    """
    Searches user_id in the cookie, validates it and inserts it into request.
    If user_id not found - generate a new one with uuid4.
    """
    cookie_uuid = request.COOKIES.get('user_id')
    cookie_is_set = cookie_uuid is not None
    if cookie_is_set and not is_valid_uuid4(cookie_uuid):
        cookie_uuid = None
    user_id = cookie_uuid or str(uuid.uuid4())
    request.data['user_id'] = user_id
    return cookie_is_set


def set_user_id_to_cookie(user_id: str, response: HttpResponse, cookie_is_set: bool) -> None:
    """If user_id not found in cookies - sets it."""
    if not cookie_is_set:
        response.set_cookie('user_id', user_id)
