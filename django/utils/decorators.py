from functools import wraps
from django.shortcuts import redirect
from utils.token import verificar_token

def login_requerido(view_func):
    def wrapper(request, *args, **kwargs):
        payload = verificar_token(request)
        if not payload:
            return redirect('iniciar')
        request.usuario_payload = payload
        return view_func(request, *args, **kwargs)
    return wrapper

def admin_requerido(vista_func):
    @wraps(vista_func)
    def wrapper(request, *args, **kwargs):
        if request.session.get("tipousuarioId") != 1:
            return redirect("inicio")
        return vista_func(request, *args, **kwargs)
    return wrapper