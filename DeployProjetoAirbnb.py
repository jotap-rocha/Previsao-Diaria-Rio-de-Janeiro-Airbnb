import pandas as pd
import streamlit as st
import joblib

# Esse arquivo não é para ser executado com ctrl + F5.
# Aperte ctrl + ' para acessar o terminal, use o comando "cd" para entrar na pasta onde está o projeto
# e execute a seguinte linha de código: streamlit run DeployProjetoAirbnb.py

numericos = {'latitude': 0, 'longitude': 0, 'accomodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
             'ano': 0, 'mes': 0, 'n_amenities': 0, 'minimum_nights': 0, 'host_listings_count': 0}

true_false = {'host_is_superhost': 0, 'instant_bookable': 0}

lista = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
         'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
         'cancellation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']}

dicionario = {}

for item in lista:
    for valor in lista[item]:
        dicionario[f'{item}_{valor}'] = 0

for item in numericos:
    if item == 'latitude' or item == 'longitude':
        valor = st.number_input(
            f'{item}', step=0.00001, value=0.0, format="%.5f")
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item}', step=1, value=0)
    numericos[item] = valor

for item in true_false:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    if valor == 'Sim':
        true_false[item] = 1
    else:
        true_false[item] = 0

for item in lista:
    valor = st.selectbox(f'{item}', lista[item])
    dicionario[f'{item}_{valor}'] = 1

botao = st.button('Previsão de Preço do Imóvel')
if botao:
    dicionario.update(numericos)
    dicionario.update(true_false)
    valores_x = pd.DataFrame(dicionario, index=[0])
    modelo = joblib.load('Modelo.joblib')
    preco = modelo.predict(valores_x)
    st.write(f'R$ {preco[0]:.2f}')
