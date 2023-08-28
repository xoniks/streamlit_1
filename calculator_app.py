import streamlit as st

num1 = st.number_input("Please enter a number",key=1)
num2 = st.number_input("Please enter a number",key=2)

import streamlit as st

operation = st.selectbox( 
    'Choose the operation',
    ('No Option','Add', 'Subtract', 'Divide','Multiply'))

if operation=='Add':
    st.write(num1+num2)
elif operation=='Subtract':
    st.write(num1-num2)
elif operation=='Divide':
    if num2!=0:
        st.write(num1/num2)
    else:
        st.warning('Zero Division')
elif operation=='Multiply':
    st.write(num1*num2)
else:
    st.write('No operation added')