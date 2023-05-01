import streamlit as st

st.set_page_config(page_title="Gerador Inmes", page_icon="https://inmes.com.br/wp-content/uploads/2021/07/cropped-Vers%C3%A3o-Original-2-32x32.png")
# image
st.image("https://inmes.com.br/wp-content/uploads/2021/07/cropped-Vers%C3%A3o-Original-1.png", width=200)
st.title("Gerador de Range de Série")
# input = st.text_input("What is your name?")
valorinserido = st.text_input("Informe a série do produto da seguinte maneira: série inicial-série final -> EX: 0001-9999 Obs: Caso o manual possua mais de um intervalo de série, organize-os separados por vírgula. EX: 10, 15-20, 0001-9999")
# botao enviar
st.button("Gerar")
resultado = []
if st.button:
    if ',' in valorinserido:
        valorinserido = valorinserido.split(',')
        for i in valorinserido:
            if '-' in i:
                i = i.split('-')
                caracter = len(i[0].replace(' ',''))
                valorInicial = int(i[0])
                valorFinal = int(i[1]) + 1
                ranges = range(valorInicial, valorFinal)
                for w in ranges:
                    w = str(w)
                    if len(w) < caracter:
                        w = w.zfill(caracter)
                        resultado.append(w)
                    else:
                        resultado.append(w)
        resultado = str(resultado).replace('[','').replace(']','').replace(' ','').replace("'",'')        
        st.write(resultado)
        

    else:
        if '-' in valorinserido:
            valorinserido = valorinserido.split('-')
            # print(i)
            valorInicial = int(valorinserido[0])
            valorFinal = int(valorinserido[1]) + 1
            ranges = range(valorInicial, valorFinal)
            caracter = len(valorinserido[0].replace(' ',''))
            ranges = range(valorInicial, valorFinal)
            for w in ranges:
                w = str(w)
                if len(w) < caracter:
                    w = w.zfill(caracter)
                    resultado.append(w)
                else:
                    resultado.append(w)
                
            # write result in a text file
            resultado = str(resultado).replace('[','').replace(']','').replace(' ','').replace("'",'')        
            st.text(resultado)

                
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)