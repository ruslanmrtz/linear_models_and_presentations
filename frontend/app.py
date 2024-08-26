import streamlit as st
import requests

BACKEND_PATH = 'https://club-15hl.onrender.com'


def main():
    st.title('Country club')

    with st.sidebar:

        endpoint = st.selectbox(
            'What do you want to get?',
            ('users', 'facilities', 'bookings')
        )

        limit = st.slider(
            label='Choose limit',
            min_value=1,
            max_value=50,
            value=10,
            step=1
        )

        execute_button = st.button(
            label='Retrieve data '
        )

    if execute_button:
        url = f'{BACKEND_PATH}/{endpoint}/all?limit={limit}'

        response = requests.get(url).json()

        st.write(response)


if __name__ == '__main__':
    main()
