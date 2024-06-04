# -*- coding:utf-8 -*-

import streamlit as st 

def main():
    value1 = st.slider("숫자 선택", 0, 100)
    # st.write(value1)
    st.sidebar.write(value1)

    value2 = st.sidebar.slider("숫자 선택(sidebar)", 0, 100)
    # st.sidebar.write(value2)
    st.write(value2)

    with st.sidebar:
        value3 = st.slider("숫자 선택, with sidebar", 0, 100)
        st.write(value3)
        
        import matplotlib.pyplot as plt 
        st.markdown("Matplotlib")
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        st.pyplot(fig)

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    st.pyplot(fig)

if __name__ == "__main__":
    main()