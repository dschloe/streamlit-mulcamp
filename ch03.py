# -*- coding:utf-8 -*-
import pandas as pd 
import streamlit as st 

@st.cache_data
def load_data():
    df = pd.read_csv('./data/profile.csv', parse_dates = ['birthdate']).dropna()
    return df

def main():
    st.write(pd.__version__)
    st.write(st.__version__)

    data = load_data()
    # st.table(data)

    # st.data_editor & st.column_config
    column_configuration = {
        "name": st.column_config.TextColumn(
            "Name", help="The name of the user", max_chars=100
        ),
        "avatar": st.column_config.ImageColumn("Avatar", help="The user's avatar"),
        "active": st.column_config.CheckboxColumn("Is Active?", help="Is the user active?"),
        "homepage": st.column_config.LinkColumn(
            "Homepage", help="The homepage of the user"
        ),
        "gender": st.column_config.SelectboxColumn(
            "Gender", options=["male", "female", "other"]
        ),
        "age": st.column_config.NumberColumn(
            "Age",
            min_value=0,
            max_value=120,
            format="%d years",
            help="The user's age",
        ),
        "status": st.column_config.ProgressColumn(
            "Status", min_value=0, max_value=1, format="%.2f"
        ),
        "birthdate": st.column_config.DateColumn(
            "Birthdate",
            help="The user's birthdate"
        ),
        "email": st.column_config.TextColumn(
            "Email",
            help="The user's email address",
            validate="^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",
        ),
    }

    st.data_editor(
        data,
        column_config=column_configuration,
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
    )

if __name__ == "__main__":
    main()