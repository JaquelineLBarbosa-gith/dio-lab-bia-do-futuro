# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `glossario_financeiro.txt` | TXT | Definir termos e jargões do mercado de forma simples |
| `tipos_investimento.json` | JSON | Explicar categorias, prós e contras da Renda Fixa e Variável |
| `faq_iniciantes.txt` | TXT | Base para responder as dúvidas mais comuns de quem nunca investiu |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Como o Diogo é um educador neutro, os dados fictícios de transações bancárias e perfis de clientes (presentes no modelo original) foram substituídos. A base foi adaptada para conter puramente documentos educacionais e informativos sobre o mercado financeiro.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os dados (textos e JSON) são carregados na memória do agente e passados como "contexto" junto com a pergunta do usuário (técnica de RAG - Retrieval-Augmented Generation).

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os arquivos servem como a "verdade absoluta" do Diogo. Quando o usuário pergunta sobre um investimento, a IA busca a explicação dentro desses documentos aprovados, garantindo que a resposta seja neutra e evitando que ela invente regras financeiras (alucinação).

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Base de Conhecimento Consultada pela IA:
- Tópico: Tesouro Direto
- Risco: Baixo (Garantido pelo Governo Federal)
- Liquidez: Alta (Pode ser resgatado diariamente)
- Regra de Segurança do Agente: Explicar o conceito de forma didática, mas NUNCA recomendar o aporte direto ou prever rentabilidade futura.
