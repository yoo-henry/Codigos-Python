
### Coloca um título
# st.title("Imune ao conhecimento ")
# ### Escreve
# st.write("Testando... Esquerda e Direita ") 
# ###  Cria uma Barra lateral
# st.sidebar.title("Barra Lateral")
# ### Criando a lista 
# nomes = ["Henrique lindo","Lucas","Breno","Pedro" ]
# ### Cria a caixa na barra lateral
# st.sidebar.selectbox("Escolhe um nome:", nomes)
import streamlit as st


st.sidebar.title("Aluguel de Carros")
st.sidebar.image("logo.png")
st.sidebar.write("Escolha um modelo de carro")
carros = ["Mercedes-Benz Classe S", "BMW Série 7","Audi A8","Porsche Panamera"]
pagina = st.sidebar.selectbox("Selecione o modelo:", carros) 








# --- Conteúdo principal ---

if pagina == "Mercedes-Benz Classe S":
    diaria = 450
    st.title("Mercedes-Benz Classe S")
    st.image("mercedes.png", caption="Mercedes")
    st.write("Descubra a Mercedes-Benz Classe S, o ápice do luxo e da inovação. Com design elegante, tecnologia de ponta e conforto incomparável, cada viagem se transforma em uma experiência única. Seu motor potente e silencioso une desempenho excepcional à eficiência, enquanto o interior sofisticado oferece materiais premium e sistemas inteligentes que cuidam de você em cada detalhe. Escolher a Classe S é optar por status, segurança e prazer ao dirigir. Transforme seu caminho em um verdadeiro luxo sobre rodas.")
    dias = st.text_input(f"Por quantos dias o {pagina} foi alugada ?")
    km = st.text_input(f"Quantos km você rodou com o {pagina}?")
elif pagina == "BMW Série 7":
    diaria = 400
    st.title("BMW Série 7")
    st.image("BMW.png", caption="BMW")
    st.write("Experimente o poder e a sofisticação da BMW Série 7. Com tecnologia avançada, design imponente e desempenho de tirar o fôlego, este sedã redefine o conceito de dirigir com luxo. Cada detalhe interno combina conforto premium e inovação, garantindo uma experiência única a cada viagem. A Série 7 não é apenas um carro, é uma afirmação de estilo, elegância e desempenho. Eleve seu padrão e sinta o verdadeiro prazer ao volante.")
    dias = st.text_input(f"Por quantos dias o {pagina} foi alugada ?")
    km = st.text_input(f"Quantos km você rodou com o {pagina}?")
elif pagina == "Audi A8":
    diaria = 350
    st.title("Audi A8")
    st.image("audi.png", caption="Audi")
    st.write("Descubra o Audi A8, a síntese perfeita de luxo, tecnologia e desempenho. Com linhas elegantes, interior sofisticado e sistemas inteligentes de assistência, cada viagem se torna confortável e segura. Seu motor potente proporciona aceleração impressionante, enquanto o acabamento premium transforma cada detalhe em excelência. O Audi A8 não é apenas dirigir, é viver a experiência máxima de sofisticação e inovação sobre rodas.")
    dias = st.text_input(f"Por quantos dias o {pagina} foi alugada ?")
    km = st.text_input(f"Quantos km você rodou com o {pagina}?")
elif pagina == "Porsche Panamera":
    diaria = 500
    st.title("porsche panamera")
    st.image("porsche.png", caption="Porsche")
    st.write("Sinta a emoção de dirigir o Porsche Panamera, onde desempenho esportivo encontra luxo absoluto. Com design arrojado, motor potente e tecnologia de ponta, cada trajeto se transforma em pura adrenalina. O interior sofisticado oferece conforto premium, enquanto cada detalhe reflete a excelência da engenharia Porsche. O Panamera não é apenas um carro, é uma experiência de direção única e inesquecível.")
    dias = st.text_input(f"Por quantos dias o {pagina} foi alugada ?")
    km = st.text_input(f"Quantos km você rodou com o {pagina}?")

### calcular
if st.button("calcular"):
    dias = int(dias)
    km = float(km)
    total_dias = dias * diaria
    total_km = km * 15
    aluguel_total = total_dias + total_km
    st.warning(f"Você alugou o {pagina} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}")