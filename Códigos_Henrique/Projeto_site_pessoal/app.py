# Texto e título
#st.title()          # Título principal
#st.header()         # Cabeçalho de seção
#st.subheader()      # Subcabeçalho
#st.write()          # Texto geral
#st.markdown()       # Texto com formatação

# Mídia
#st.image()          # Exibir imagens
#st.audio()          # Arquivos de áudio
#st.video()          # Vídeos

# Layout
#st.columns()        # Criar colunas
#st.expander()       # Seções expansíveis
#st.container()      # Containers para organização

# Interatividade
#st.button()         # Botões clicáveis
#st.selectbox()      # Menus dropdown
#st.slider()         # Controles deslizantes

# Informação
#st.info()           # Caixas de informação
#st.success()        # Mensagens de sucesso
#st.warning()        # Avisos
#st.error()          # Mensagens de erro


import streamlit as st

st.title("IFood")
st.image("banner.png")
st.sidebar.image("ifood.png")
st.sidebar.write("Pede agora e chame já, sua comida preferida.")
comida = ["Bolos caseiros","Lasanha","Panqueca","Pudim","Pizza Caseira"]
pagina = st.sidebar.selectbox("Selecione uma comida 🍕 :", comida) 

if comida == "Bolos caseiros":
    tipo_bolo = st.sidebar.selectbox("Escolha o tipo de bolo:", ["Doce", "Salgado"])
    st.title(f"🎂 {comida} {tipo_bolo}")
    st.write(f"Você escolheu um **bolo {tipo_bolo.lower()}**. 😋")

elif comida == "Panqueca":
    tipo_panqueca = st.sidebar.selectbox("Escolha o tipo de panqueca:", ["Doce", "Salgada"])
    st.title(f"🥞 {comida} {tipo_panqueca}")
    st.write(f"Você escolheu uma **panqueca {tipo_panqueca.lower()}**. 😋")

