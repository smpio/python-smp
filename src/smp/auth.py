import datetime


def create_jwt(app_id, app_secret, user_id=None, scopes=None, duration=None, extra_payload=None):
    import jwt

    if duration is None:
        duration = datetime.timedelta(minutes=5)

    payload = {
        'iss': app_id,
        'scp': scopes,
        'exp': datetime.datetime.utcnow() + duration,
    }

    if user_id is not create_jwt.undefined_user:
        payload['sub'] = user_id

    if extra_payload:
        payload['extra'] = extra_payload

    return jwt.encode(payload, app_secret, algorithm='HS256')


create_jwt.undefined_user = type('undefined_user', (), {})()
