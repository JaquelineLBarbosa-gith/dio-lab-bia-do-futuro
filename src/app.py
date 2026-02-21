import json
import streamlit as st
import pandas as pd
import requests

# =========== CONFIGURAÇÃO DA IA ===========
# URL local do Ollama (conforme exemplo do professor)
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3" # Exemplo de modelo Open Source

# =========== SYSTEM PROMPT ===========
SYSTEM_PROMPT = """Você é o Diogo, um educador financeiro interativo, imparcial e extremamente paciente.
Seu objetivo é desmistificar o mundo dos investimentos para iniciantes e pessoas buscando diversificação.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funcionam.
- JAMAIS atue como vendedor de corretora ou analista.
- Mantenha um tom didático, acessível e sem "economês" complicado.
- Se não souber algo ou pedirem previsões do futuro, admita a limitação: "Como sou um educador, não prevejo o mercado..."
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
"""

# =========== FUNÇÃO DE COMUNICAÇÃO ===========
def perguntar(msg):
    prompt_completo = f"""
    {SYSTEM_PROMPT}
    
    Pergunta do Usuário: {msg}
    """
    
    # Fazendo a requisição para a IA (Ollama)
    try:
        r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt_completo, "stream": False})
        return r.json()['response']
    except:
        return "Desculpe, estou desconectado da minha base no momento. Tente novamente mais tarde!"

# =========== INTERFACE (STREAMLIT) ===========
st.title("🎓 Diogo, Seu Educador Financeiro")
st.markdown("Olá! Eu sou o Diogo. Que conceito sobre finanças vamos desmistificar hoje?")

# Inicializar histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Caixa de texto para o usuário digitar
if prompt := st.chat_input("Sua dúvida sobre finanças..."):
    # Mostrar mensagem do usuário
    with st.chat_message("user"):
        st.markdown(prompt)
    # Salvar no histórico
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Mostrar resposta do assistente com efeito de carregamento
    with st.chat_message("assistant"):
        with st.spinner("Diogo está pensando..."):
            resposta = perguntar(prompt)
            st.markdown(resposta)
    # Salvar resposta no histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta})
