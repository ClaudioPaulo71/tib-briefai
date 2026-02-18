def get_identity_profile(perfil: str):
    profiles = {
        "Tradicional": {
            "formalidade": "alta", "estilo": "conservador", "objetividade": "alta",
            "usa_emojis": False, "linguagem": "institucional"
        },
        "Startup": {
            "formalidade": "media", "estilo": "inovador", "objetividade": "media",
            "usa_emojis": True, "linguagem": "colaborativa"
        },
        "Técnico": {
            "formalidade": "alta", "estilo": "técnico", "objetividade": "alta",
            "usa_emojis": False, "linguagem": "precisa"
        }
    }
    return profiles.get(perfil, profiles["Tradicional"])