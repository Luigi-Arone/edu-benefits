# 🎓 EduBenefits

Verifique quais softwares e serviços oferecem planos gratuitos ou descontos para o seu email institucional (universidades, institutos federais, startups).

> 🚀 **[Acesse o dashboard ao vivo](https://edubenefits.streamlit.app)**

## Funcionalidades

- **Verificador** — detecta automaticamente se o domínio é acadêmico ou de startup, cruza com a base de serviços e exibe elegibilidade
- **Contribuir** — página para sugerir novos domínios de instituições e novos serviços

## Estrutura

```
edu-benefits/
├── app.py                  # Página principal (verificador)
├── data.py                 # Base de serviços + lógica de classificação de domínio
├── pages/
│   └── 1_Contribuir.py     # Página de contribuição
├── contributions.json      # Gerado automaticamente com as sugestões recebidas
├── requirements.txt
└── .streamlit/
    └── config.toml         # Tema
```

## Deploy no Streamlit Cloud

1. Faça um fork ou push deste projeto para um repositório GitHub público (ou privado)
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Clique em **New app**
4. Selecione o repositório, branch `main` e arquivo `app.py`
5. Clique em **Deploy** — pronto!

> O arquivo `contributions.json` é gerado localmente. No Streamlit Cloud, o filesystem é efêmero — as contribuições se perdem ao reiniciar. Para persistência em produção, substitua o `save_contribution` por um banco de dados (ex: Supabase free tier, Google Sheets via API, ou o próprio `st.connection` com SQLite).

## Rodando localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Adicionando serviços ou domínios

- **Serviços:** edite a lista `SERVICES` em `data.py`
- **Domínios BR:** adicione à set `BR_UNI_DOMAINS` em `data.py`
- **Padrões globais:** ajuste a função `classify_domain` em `data.py`
