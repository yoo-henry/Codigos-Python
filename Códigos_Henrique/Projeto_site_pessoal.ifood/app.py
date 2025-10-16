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

st.sidebar.image("ifood.png")
st.sidebar.write("Pede agora e chame já, sua comida preferida.")

# --- Menu lateral ---
comidas = ["Home", "Bolos caseiros", "Lasanha", "Panqueca", "Pudim", "Pizza Caseira"]
pagina = st.sidebar.selectbox("Selecione uma comida 🍕 :", comidas)

# --- Preços por comida ---
precos = {
    "Bolo Doce": 25.0,
    "Bolo Salgado": 30.0,
    "Panqueca Doce": 18.0,
    "Panqueca Salgada": 22.0,
    "Lasanha": 28.0,
    "Pudim": 12.0,
    "Pizza Caseira Média": 35.0,
    "Pizza Caseira Grande": 45.0
}

# --- Página inicial ---
if pagina == "Home":
    st.title("🍴 IFood")
    st.image("banner.png")
    st.write("### 🍽️ Bem-vindo ao IFood!")
    st.write("Escolha sua comida favorita no menu ao lado.")

# --- Bolos ---
elif pagina == "Bolos caseiros":
    tipo_bolo = st.sidebar.selectbox("Escolha o tipo de bolo:", ["Doce", "Salgado"])
    nome_bolo = f"Bolo {tipo_bolo}"
    st.title("Bolos Caseiros")
    st.image("bolo.png")
    st.write("Nós temos bolos doces e salgados, selecione o que for de sua preferência")
    st.write(f"💰 Preço: R$ {precos[nome_bolo]:.2f} por kg")

    kg = st.text_input(f"Quantos kg de {nome_bolo} você quer?")

    if st.button("Calcular"):
        try:
            kg = float(kg)
            total = kg * precos[nome_bolo]
            st.warning(f"Você escolheu {kg:.1f} kg de {nome_bolo}. O valor total a pagar é R$ {total:.2f}")
        except:
            st.error("Digite um valor válido para a quantidade.")

# --- Panquecas ---
elif pagina == "Panqueca":
    tipo_panqueca = st.sidebar.selectbox("Escolha o tipo de panqueca:", ["Doce", "Salgada"])
    nome_panqueca = f"Panqueca {tipo_panqueca}"
    st.title("Panquecas")
    st.image("panqueca.png")
    st.write("Panquecas deliciosas 🥞")
    st.write(f"💰 Preço: R$ {precos[nome_panqueca]:.2f} por kg")

    kg = st.text_input(f"Quantos kg de {nome_panqueca} você quer?")

    if st.button("Calcular"):
        try:
            kg = float(kg)
            total = kg * precos[nome_panqueca]
            st.warning(f"Você escolheu {kg:.1f} kg de {nome_panqueca}. O valor total a pagar é R$ {total:.2f}")
        except:
            st.error("Digite um valor válido para a quantidade.")

# --- Lasanha ---
elif pagina == "Lasanha":
    st.title("🍝 Lasanha")
    st.image("lasanha.png")
    st.write("Deliciosa lasanha caseira, com muito queijo. 🤤")
    st.write(f"💰 Preço: R$ {precos['Lasanha']:.2f} por kg")

    kg = st.text_input("Quantos kg de lasanha você quer?")

    if st.button("Calcular"):
        try:
            kg = float(kg)
            total = kg * precos["Lasanha"]
            st.warning(f"Você escolheu {kg:.1f} kg de lasanha. O valor total a pagar é R$ {total:.2f}")
        except:
            st.error("Digite um valor válido para a quantidade.")
# --- Pudim ---
elif pagina == "Pudim":
    st.title("🍮 Pudim")
    st.image("pudim.png")
    st.write("Pudim de leite condensado tradicional, derrete na boca. 😍")
    st.write(f"💰 Preço: R$ {precos['Pudim']:.2f} por kg")

    kg = st.text_input("Quantos kg de pudim você quer?")

    if st.button("Calcular"):
        try:
            kg = float(kg)
            total = kg * precos["Pudim"]
            st.warning(f"Você escolheu {kg:.1f} kg de pudim. O valor total a pagar é R$ {total:.2f}")
        except:
            st.error("Digite um valor válido para a quantidade.")

elif pagina == "Pizza Caseira":
    tamanho = st.sidebar.selectbox("Escolha o tamanho da pizza:", ["Média", "Grande"])
    nome_pizza = f"Pizza Caseira {tamanho}"
    st.title("🍕 Pizza Caseira")
    st.image("pizza.png")
    st.write("Pizza artesanal feita com massa fresca e ingredientes selecionados. 🍅🧀")
    st.write(f"💰 Preço: R$ {precos[nome_pizza]:.2f} por unidade")

    qtd = st.text_input(f"Quantas unidades de {nome_pizza} você quer?")

    if st.button("Calcular"):
        try:
            qtd = int(qtd)
            total = qtd * precos[nome_pizza]
            st.warning(f"Você escolheu {qtd} unidade(s) de {nome_pizza}. O valor total a pagar é R$ {total:.2f}")
        except:
            st.error("Digite um valor válido para a quantidade.")
