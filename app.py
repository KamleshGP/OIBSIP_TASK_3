import streamlit as st
import pandas as pd
import pickle
from PIL import Image

model = pickle.load(open("cpp.pk2", "rb"))

df = pd.read_csv("Cleaned_CarPrice.csv")

cname = df["carname"].unique()
ftype = df["fueltype"].unique()
atype = df["aspiration"].unique()
cbody = df["carbody"].unique()
dwheel = df["drivewheel"].unique()
etype = df["enginetype"].unique()

st.title("Car Price Pridictor")

image = Image.open('car background.png')
st.image(image)

cname1 = st.selectbox("**Select Car Name :** ", cname, index=0)
ftype1 = st.selectbox("**Select Fuel Type :** ", ftype, index=0)
atype1 = st.selectbox("**Select Aspiration  Type :** ", atype, index=0)
cbody1 = st.selectbox("**Select Car Body Type :** ", cbody, index=0)
dwheel1 = st.selectbox("**Select Drive Wheel :** ", dwheel, index=0)
etype1 = st.selectbox("**Select Engine Type :** ", etype, index=0)
st1 = st.number_input("**Enter stroke :**")
hp1 = st.number_input("**Enter horsepower :**")
pe1 = st.number_input("**Enter peakrpm :**")

if st.button("Predict"):
    prediction = int(model.predict(pd.DataFrame([[cname1, ftype1, atype1, cbody1, dwheel1, etype1, st1, hp1, pe1]],
                                                columns=["carname", "fueltype", "aspiration", "carbody", "drivewheel",
                                                         "enginetype", "stroke", "horsepower", "peakrpm"])))
    st.write(f"### Predicted Price is :- RS.{prediction}")
