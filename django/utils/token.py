import jwt
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

def verificar_token(request):
    token = request.session.get('token')
    if not token:
        return None

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload
    except (ExpiredSignatureError, InvalidTokenError):
        return None