import streamlit as st
import pandas as pd 
import pickle

model=pickle.load(open('pipe.pkl','rb'))

st.header('siRNA Inhibitor Performance Predictor')
st.image('image.jpg')

st.subheader('Input')
Start= st.number_input('siRNA start position')
End= st.number_input('siRNA end position')
G= st.number_input('siRNA Guanine content')
U= st.number_input('siRNA Uracil content')
bi= st.number_input('Stability of dimers with antisense strand')
uni=st.number_input('Antisense strand intra-molecular stability')
duplex= st.number_input('overall sense-antisense pair stability')
Pos1= st.number_input('stability of sense-antisense base pairs in position 1')
Pos2= st.number_input('stability of sense-antisense base pairs in position 2')
Pos6= st.number_input('stability of sense-antisense base pairs in position 6')
Pos13= st.number_input('stability of sense-antisense base pairs in position 13')
Pos14= st.number_input('stability of sense-antisense base pairs in position 14')
Pos18= st.number_input('stability of sense-antisense base pairs in position 18')
Dif= st.number_input('Stability difference in position 1 and 18')
Contentp= st.number_input('Preffered dinucleotide content')
Contenta=st.number_input('Avoided dinucleotide content')
Consp=st.number_input('Preffered position-dependent nucleotide consensus')
Consa=st.number_input('Avoided position-dependent nucleotide consensus')
cons_sum=st.number_input('Sum of the position-dependent nucleotide consensus')
Hyb19=st.number_input('Potential target copies number in mRNA')
target=st.number_input('Stabilities of mRNA local target')

if st.button('Submit'):
    columns=['Start', 'End', 'G', 'U', 'bi', 'uni', 'duplex', 'Pos1', 'Pos2', 'Pos6',
       'Pos13', 'Pos14', 'Pos18', 'Dif_5-3', 'Content+', 'Content-', 'Cons+',
       'Cons-', 'Cons_Sum', 'Hyb19', 'target']
    
    x=pd.DataFrame([[Start,End,G,U,bi,uni,duplex,Pos1,Pos2,Pos6,Pos13,Pos14,Pos18,Dif,Contentp,Contenta,Consp,Consa,cons_sum,Hyb19,target]],columns=columns)

    pred=model.predict(x)
    st.text(f'siRNA Performance: {pred[0]}')