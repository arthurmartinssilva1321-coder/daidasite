from dataclasses import dataclass
from pathlib import Path
import streamlit as st

@dataclass
class Obra:
    titulo: str
    autor: str
    ano: int
    genero: str
    descricao: str
    imagem: Path

obras = [
    Obra(
        titulo="Renascentismo mutante",
        autor="Arthur Martins da Silva",
        ano=2026,
        genero="Pop art, renascimento e arte digital",
        descricao="Uma obra que mistura elementos do renascimento com a cultura pop, explorando a dualidade entre o clássico e o moderno.",
        imagem=Path("1.png")
    ),   
    Obra(  
        titulo="Mesmo ao caos, sempre plena",
        autor="Arthur Martins da Silva",
        ano=2026,
        genero="Dadaísmo e arte digital",
        descricao="Mesmo diante do caos e da desgraça, a figura central mantém a serenidade absoluta, ironizando o excesso de dramas cotidianos.",
        imagem=Path("2.png")
    ),
    Obra(
        titulo="O Moneteiro",
        autor="Arthur Martins da Silva",
        ano=2026,
        genero="Dadaísmo e arte digital",
        descricao="Ele está tentando parecer maneiro, mas no fundo está apenas escondendo a catarata por trás de uma estética impressionista.",
        imagem=Path("4.png")
    ),
    Obra(
        titulo="A maior dúvida do mundo",
        autor="Arthur Martins da Silva",
        ano=2026,
        genero="Dadaísmo e arte digital",
        descricao="Uma obra que explora a incerteza e o absurdo, questionando a realidade e a percepção humana: quem veio primeiro, o ovo ou a galinha?",
        imagem=Path("6.png")
    ),
    Obra(
        titulo="Socorro, AHHHHHHHH!",
        autor="Arthur Martins da Silva",
        ano=2026,
        genero="Dadaísmo e arte digital",
        descricao="Uma obra que expressa o desespero visceral e caótico da pressão e do sofrimento por motivos escolares.",
        imagem=Path("8.png"),
    ),
]

st.set_page_config(page_title="Exposição de Arte", page_icon="🎨", layout="wide")

st.sidebar.title("🧭 Navegação")
modo = st.sidebar.radio("Escolha uma opção:", ["Exposição", "Sobre o artista"])

if modo == "Exposição":
    st.title("🎨 Galeria Contemporânea — Arthur Martins")
    st.write("Uma coleção digital que mistura referências clássicas, humor ácido e estética dadaísta.")
    st.divider()

    for item in obras:
        col_img, col_texto = st.columns([1.2, 1])
        
        with col_img:
            if item.imagem.exists():
                st.image(str(item.imagem), use_container_width=True)
            else:
                st.warning(f"Arquivo '{item.imagem}' não encontrado.")
                
        with col_texto:
            st.subheader(item.titulo)
            st.write(f"**Gênero:** {item.genero}")
            st.write(f"**Ano:** {item.ano}")
            st.write("### Conceito da Obra")
            st.write(item.descricao)
            
        st.divider()

elif modo == "Sobre o artista":
    st.title("👨‍🎨 Sobre o Artista")
    st.subheader("Arthur Martins da Silva")
    st.write(
        "Artista digital e desenvolvedor independente. Suas obras transitam entre a "
        "apropriação de clássicos da história da arte, a Pop Art e o Dadaísmo contemporâneo, "
        "utilizando o humor e o absurdo para comentar a cultura atual e a rotina escolar."
    )
    st.info("Todas as peças foram ilustradas digitalmente no Ibis Paint e expostas nesta plataforma desenvolvida em Python com Streamlit.")



