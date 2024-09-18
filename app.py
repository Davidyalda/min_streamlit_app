import streamlit as st

st.title("Tågbiljett Kiosk")
st.header("Välkommen")
st.subheader("Här köper man biljetter")
under_18 = 130
över_18 = 230
över_65 =100
Fråga_användaren_om_ålder = st.slider("Skriv din ålder!")
if Fråga_användaren_om_ålder <=17:
    st.write("Du ska betala 130 kr")

elif Fråga_användaren_om_ålder >=65:
    st.write("du ska betala 100 kr")

else:
    st.write("du ska betala 230 kr")
