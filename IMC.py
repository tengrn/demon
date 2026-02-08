import streamlit as st

st.title("IMC")

poids = st.number_input("donnez le poids :")
taille = st.number_input("donnez la taille:")

if st.button("calcul"):
    
    IMC = poids/((taille)**2)
    
    if IMC<18.5:
        st.warning("maigre")
        
    elif 18.5<IMC<25:
        st.success("poids norma")
        
    elif 25 <IMC<30:
        st.warning("surpoids")
    
    elif IMC >= 30:
        st.warning("obese")
    else:
        st.info("ceci n'est pas un nombre")