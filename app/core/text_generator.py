import os
from openai import OpenAI
from dotenv import load_dotenv

def generate_text(prompt: str, max_tokens: int = 400, temperature: float = 0.7):
    load_dotenv()                     # carrega .env toda vez que a função roda
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        return "Erro: OPENAI_API_KEY não encontrada. Crie o arquivo .env na raiz do projeto.", 0
    
    client = OpenAI(api_key=api_key)
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um especialista em comunicação corporativa."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        texto = response.choices[0].message.content.strip()
        tokens = response.usage.total_tokens
        return texto, tokens
    except Exception as e:
        return f"Erro ao gerar texto: {str(e)}", 0