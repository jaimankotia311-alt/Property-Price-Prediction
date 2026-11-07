import joblib
import pandas as pd
import streamlit as st 

model = joblib.load("regression_model.joblib")

st.set_page_config(page_title="Property Price Prediction" , page_icon="🏘️🛖🏠🏡")
st.title("Property project")
st.markdown("Here you will pass on the configuration of houses you wanted to buy and let our model predict the price of house")

area = st.number_input(label="Area" , placeholder="Enter the area : ") 
bedrooms = st.number_input(label="Bed Rooms" , placeholder="Enter the number of bedrooms : ", min_value=1 , step=1)  
bathrooms = st.number_input(label="Bath Rooms" , placeholder="Enter the number of bathrooms : ")  
floors = st.number_input(label="Number of Floors" , placeholder="Enter the number of floors : ")  
house_age = st.number_input(label="Age Of House" , placeholder="Enter the age of house : ")  
parking_spaces = st.number_input(label="Number of Parking" , placeholder="Enter the number of parking spaces : ")  
distance_city_km= st.number_input(label="Distance From City" , placeholder="Enter the distance between city and house: ")
schools = st.number_input(label="Nearby Schools" , placeholder="Enter any nearby schools : ")  
crime_rate = st.number_input(label="Crime Rate" , placeholder="Enter the crime rate : ")  
property_tax = st.number_input(label="Tax of property" , placeholder="Enter the prperty tax : ")  
location_score = st.number_input(label="Score of Location" , placeholder="Enter the score of location : ",min_value=1 , step=1)
 


rooms = bedrooms + bathrooms

area_per_bedroom = area / bedrooms

location_access_score = schools + location_score

new_house = pd.DataFrame({
    "area_sqft": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "floors": [floors],
    "house_age": [house_age],               
    "parking_spaces": [parking_spaces],
    "distance_city_km": [distance_city_km],
    "nearby_schools": [schools],
    "crime_rate": [crime_rate],
    "property_tax": [property_tax],
    "location_score": [location_score],
    "rooms": [rooms],
    "area_per_bedroom": [area_per_bedroom],      
    "location_access_score": [location_access_score]
})

if st.button("Predict"):
    prediction = model.predict(new_house)
    st.write(f"The predicted price of house would be arround approximate : {prediction[0] : ,.2f} rupees" )
    st.success("Congretualltion for reaching the end ! 🏘️")



# py -m streamlit run "C:\Users\Jay Mankotia\OneDrive\Desktop\AI ML\06 Property Project\02_Best_Model.py"
