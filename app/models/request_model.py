from pydantic import BaseModel

class RequestModel(BaseModel):
    tipo: str
    publico: str
    tom: str
    topicos: str
    perfil: str
    language: str = "English"