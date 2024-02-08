import streamlit as st 
import pandas as pd
import numpy as np
import requests

st.title('Apis')

#function for first api
def planets(api_key):
    #ask the user for the name of the planet
    name = st.text_input("Enter the name of the planet")
    if name == "":
        st.write("Please enter the name of the planet")
        return
    api_url = 'https://api.api-ninjas.com/v1/planets?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        data = response.json()
        st.write(data)
    else:
        print("Error:", response.status_code, response.text)

def quotes(api_key):
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        st.write(response.json())
    else:
        print("Error:", response.status_code, response.text)

def country(api_key):
    countryname = st.text_input("Enter the name of the country")
    if countryname == "":
        st.write("Please enter the name of the country")
        return
    api_url = 'https://api.api-ninjas.com/v1/country?name='.format(countryname)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        data = response.json()
        st.write(data)
    else:
        print("Error:", response.status_code, response.text)

#main function to call the apis
def main():
    
    planets_api_key = 'Hj5ZKIpU5sysDLglGp9Tew==CCpkqlHOokQ2qLYI'

    #call the first api
    st.subheader("Planets")
    planets(planets_api_key)

    #call the second api
    st.subheader("Quote")
    quotes(planets_api_key)

    #call the third api
    st.subheader("Country")
    country(planets_api_key)

if __name__ == '__main__':
    main()
