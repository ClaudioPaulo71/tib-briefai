# BriefAI – Seu Primeiro Copiloto de IA para Comunicação Corporativa

**Título do Trabalho:** Seu Primeiro Copiloto de IA: Criando uma Solução Inteligente com IA Generativa

**Autor:** Claudio Paulo  
**Curso:** Graduação em IA e Automação Digital – Rocketseat / UniFECAF  
**Data:** Fevereiro 2025

## Problema Resolvido

O RH e equipes de comunicação interna de empresas enfrentam sobrecarga com tarefas repetitivas: redação de e-mails, resumos de reuniões, mensagens corporativas no WhatsApp e avisos institucionais. Muitos textos precisam seguir uma identidade organizacional específica (formalidade, tom, estilo), o que consome tempo e gera inconsistências.

**BriefAI** é um assistente inteligente que, a partir de inputs simples (tipo de texto, público-alvo, tom de voz, tópicos e perfil da empresa), gera textos corporativos alinhados, rápidos e prontos para uso.

## Tecnologias Utilizadas

- **Backend:** FastAPI (Python)  
- **Modelo LLM:** OpenAI GPT-4o-mini (via API)  
- **Frontend:** HTML + Tailwind CSS + JavaScript vanilla (interface simples e responsiva)  
- **Prompt Engineering:** Prompt modular com perfis de identidade organizacional (Tradicional, Startup, Técnico) + regras rígidas  
- **Outros:** Pydantic (validação), python-dotenv, Uvicorn

## Como Rodar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/tib-briefai.git
   cd tib-briefai

2. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate 

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

4. Inicie o servidor:
   ```bash
   uvicorn app.main:app --reload

5. Acesse a interface no navegador:
   ```bash
   http://localhost:8000

6. Use a interface para gerar textos corporativos.

## Documentação

A documentação completa do projeto está disponível no arquivo README.md.

## Licença

MIT License

Fluxo da Aplicação (Workflow)

Usuário seleciona perfil da empresa (Tradicional / Startup / Técnico)
Preenche: tipo de texto, público-alvo, tom de voz, tópicos
Frontend envia POST para /gerar
Backend:
Carrega perfil de identidade
Monta prompt modular com regras + few-shot implícito
Chama OpenAI GPT-4o-mini
Retorna texto gerado + contagem de tokens

Frontend exibe o resultado formatado

(Adicione aqui prints da tela:

Print 1: Formulário inicial
Print 2: Resultado gerado de exemplo – e-mail formal
Print 3: Resultado gerado – mensagem motivacional startup)

Deploy Futuro (VPS Hostinger – tib-usa.app)

Porta: 8008 (ou outra livre)
Nginx como reverse proxy → subdomínio briefai.tib-usa.app
Systemd service + HTTPS via Certbot
Script de deploy automatizado (ver pasta deploy/ ou branch deploy)

Evoluções Futuras

Histórico de gerações (com autenticação simples)
Suporte a mais perfis e idiomas
Integração com WhatsApp Business API
Versão SaaS com planos pagos

Link da demo (quando deployado): https://briefai.tib-usa.app
Feito para a disciplina Fundamentos de IA Generativa.
