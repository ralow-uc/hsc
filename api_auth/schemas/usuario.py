from pydantic import BaseModel, EmailStr

class UsuarioSchema(BaseModel):
    username: str
    contrasennia: str
    nombre: str
    apellido: str
    email: str
    tipousuario_id: int

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    username: str
    contrasennia: str

class UsuarioLoginResponse(BaseModel):
    username: str
    tipousuarioId: int

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    usuario: UsuarioLoginResponse

class RecuperarContrasenaRequest(BaseModel):
    email: EmailStr