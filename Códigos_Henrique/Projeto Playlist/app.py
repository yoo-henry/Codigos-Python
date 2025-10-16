import streamlit as st


st.sidebar.image("logo.png")

# Dados de exemplo
generos = ["trap", "rap", "rock", "jazz"]

# Dicionário relacionando gêneros aos seus livros
musica_por_genero = {
    "trap": ["SICKO MODE", "Goosebumps", "Mask Off"],
    "rap": ["Lose Yourself", "Juicy", "HUMBLE"],
    "rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Smells Like Teen Spirit"],
    "jazz": ["Take Five", "So What", "What a Wonderful World"]
}

# Selectbox para escolher o gênero                
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    musica_selecionado = st.sidebar.selectbox(
        "Selecione a música:", 
        musica_por_genero[genero_selecionado]
    )

# Mostrar apenas o livro selecionado
if genero_selecionado and musica_selecionado:
    st.write(f"**musica selecionado:** {musica_selecionado}")
    st.write(f"**Gênero:** {genero_selecionado}")
#Trap
# Trap
if genero_selecionado == "trap" and musica_selecionado == "SICKO MODE":
    st.video("https://www.youtube.com/watch?v=tEPR0kc5cE8")
    st.write("SICKO MODE é uma música energética do Travis Scott, famosa por suas mudanças de ritmo e colaborações marcantes.")
elif genero_selecionado == "trap" and musica_selecionado == "Goosebumps":
    st.video("https://www.youtube.com/watch?v=rsEeiIrJy4E")
    st.write("Goosebumps do Travis Scott traz uma vibe hipnótica, com letras que exploram emoção e intensidade.")
elif genero_selecionado == "trap" and musica_selecionado == "Mask Off":
    st.video("https://www.youtube.com/watch?v=9mukaHt-ABE")
    st.write("Mask Off do Future é conhecida por seu beat icônico e pelo uso marcante de flauta, simbolizando liberdade e ostentação.")

# Rap
elif genero_selecionado == "rap" and musica_selecionado == "Lose Yourself":
    st.video("https://www.youtube.com/watch?v=aDV1ViZnmj4")
    st.write("Lose Yourself do Eminem é um clássico motivacional do rap, destacando perseverança e aproveitamento de oportunidades.")
elif genero_selecionado == "rap" and musica_selecionado == "Juicy":
    st.video("https://www.youtube.com/watch?v=7dP_p5GWCAU")
    st.write("Juicy do Notorious B.I.G. é um hino do rap, narrando a trajetória de superação e sucesso pessoal.")
elif genero_selecionado == "rap" and musica_selecionado == "HUMBLE":
    st.video("https://www.youtube.com/watch?v=48XJJFZTHQ4")
    st.write("HUMBLE do Kendrick Lamar mistura crítica social e estilo marcante, com refrão forte e beat cativante.")

# Rock
elif genero_selecionado == "rock" and musica_selecionado == "Bohemian Rhapsody":
    st.video("https://www.youtube.com/watch?v=786i989KEvk")
    st.write("Bohemian Rhapsody do Queen é um épico do rock, misturando ópera, balada e hard rock de forma única.")
elif genero_selecionado == "rock" and musica_selecionado == "Stairway to Heaven":
    st.video("https://www.youtube.com/watch?v=Ly6ZhQVnVow")
    st.write("Stairway to Heaven do Led Zeppelin é uma das maiores clássicas do rock, famosa pelo solo de guitarra e letras místicas.")
elif genero_selecionado == "rock" and musica_selecionado == "Smells Like Teen Spirit":
    st.video("https://www.youtube.com/watch?v=jS826PwLHdQ")
    st.write("Smells Like Teen Spirit do Nirvana tornou-se o hino grunge dos anos 90, com energia crua e crítica à sociedade.")

# Jazz
elif genero_selecionado == "jazz" and musica_selecionado == "Take Five":
    st.video("https://www.youtube.com/watch?v=tT9Eh8wNMkw")
    st.write("Take Five do Dave Brubeck é um jazz icônico em 5/4, conhecido pelo seu riff de piano e improvisações de sax.")
elif genero_selecionado == "jazz" and musica_selecionado == "So What":
    st.video("https://www.youtube.com/watch?v=afHmzRHMK4Q")
    st.write("So What do Miles Davis é um marco do jazz modal, trazendo suavidade e complexidade harmônica.")
elif genero_selecionado == "jazz" and musica_selecionado == "What a Wonderful World":
    st.video("https://www.youtube.com/watch?v=rBrd_3VMC3c")
    st.write("What a Wonderful World do Louis Armstrong é uma canção atemporal, celebrando a beleza e simplicidade da vida.")
