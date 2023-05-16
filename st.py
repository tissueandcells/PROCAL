import streamlit as st
import pickle

st.set_page_config(page_title="PROCAL")

def get_predicted(covid_params):
    with open("model_n.sav" , 'rb') as f:
        model_n = pickle.load(f)
    return model_n.predict(covid_params)


st.title("Procalcitonin Value Prediction")

'Procalcitonin (PCT) has developed into a promising new biomarker for early detection of (systemic) bacterial infections. '


form = st.form("My_Covid_Form")
with form:
    cols = st.columns((3, 3, 1))
    txt_ldh = cols[0].text_input("LDH")
    txt_crp = cols[0].text_input("CRP")
    txt_lymphocyte = cols[0].text_input("LYMPHOCYTE")
    txt_alt= cols[0].text_input("ALT")
    txt_so2 = cols[0].text_input("SO2")
    txt_mcv = cols[0].text_input("MCV")
    
    
    
    submitted = st.form_submit_button("Predict")

if submitted:
    result = st.success(get_predicted([[float(txt_ldh), float(txt_crp), float(txt_lymphocyte),
                              float(txt_alt), float(txt_so2), float(txt_mcv)]]))



    if result[0] == 1:
        st.write("PCT value is above the normal value.") 
    else:
        st.write("PCT value is below the normal value.")
    









