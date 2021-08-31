import datetime


def create_jwt(app_id, app_secret, user_id=None, scopes=None, duration=None, extra_payload=None):
    import jwt

    if duration is None:
        duration = datetime.timedelta(minutes=5)

    payload = dict(
        iss=app_id,
        scp=scopes,
        exp=datetime.datetime.utcnow() + duration,
        **(extra_payload or {})
    )

    if user_id is not create_jwt.undefined_user:
        assert 'sub' not in payload, 'got multiple values for payload key "sub"'
        payload['sub'] = user_id

    return jwt.encode(payload, app_secret, algorithm='HS256')


create_jwt.undefined_user = type('undefined_user', (), {})()
