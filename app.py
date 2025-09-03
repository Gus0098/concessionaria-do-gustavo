import streamlit as st
import pandas as pd

st.sidebar.image('logo.png')
st.sidebar.title('Concessionaria do mbappe')

carros = ['Celta','Fusca preto','Gol bolinha','Mcqueen','Prisma']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)


st.title('concessionaria do mbappe - Escolha certa é aqui!')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

if opcao == 'Celta':
    diaria = 200

elif opcao == 'Fusca preto':
    diaria = 800

elif opcao == 'Gol bolinha':
    diaria = 700

elif opcao == 'Mcqueen':
    diaria = 5000

elif opcao == 'Prisma':
    diaria = 300


if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.20
    aluguel_total = total_dias*total_km