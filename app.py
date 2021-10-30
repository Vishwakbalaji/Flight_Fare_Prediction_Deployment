import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('Pickle_file.pkl','rb'))

def predict_flight_fare(Airline,Source,Destination,Total_Stops,Additional_Info,month,flight_time,Duration):
    input=np.array([[Airline,Source,Destination,Total_Stops,Additional_Info,month,flight_time,Duration]]).astype(np.int64)
    prediction=model.predict(input)
    prediction = float(prediction)
    round(prediction,2)
    return (prediction)


def main():
    st.title("Flight Fare Prediction")

    html_temp = """
    <div style="background-color:Blue MOtif ;padding:10px">
    <h2 style="color:white;text-align:left;font-size: 20px">Enter the following details to predict your Flight Ticket Fare </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    Airline = st.text_input("Airline","Type Here: Choose One [Air Asia-0; Air India-1; Another-2; GoAir-3; IndiGo-4; Jet Airways-5; Jet Airways Business-6; Multiple carriers-7; Multiple carriers Premium economy-8; SpiceJet-9; Vistara-10]")
    Source = st.text_input("Source","Type Here: Choose One[Bangalore-0; Chennai-1; Delhi-2; Kolkata-3; Mumbai-4]")
    Destination = st.text_input("Destination","Type Here: Choose One [Banglore-0; Cochin-1; Delhi-2; Hyderabad-3; Kolkata-4; New Delhi-5]")
    Total_Stops = st.text_input("Total_Stops","Type Here: Choose One [0,1,2,3,4]")
    Additional_Info = st.text_input("Additional_Info","Type Here: Choose One [1 Long layover-0; 2 Long layover-1; 1 Short layover-2; Business class-3; Change airports-4; In-flight meal not included-5; No check-in baggage included-6; No info-7; Red-eye flight-8]")
    month = st.text_input("Month","Type Here: Choose One[1,3,4,5,6,9,12]")
    flight_time = st.text_input("Flight_Time","Type Here: Choose One [afternoon-0; evening-1; mid_night-2; morning-3]")
    Duration = st.text_input("Duration","Type Here: Choose One [5400 - 148800]")

    if st.button("Predict"):
        outputs=predict_flight_fare(Airline,Source,Destination,Total_Stops,Additional_Info,month,flight_time,Duration)
        outputs = round(outputs,2)
        st.success('We suggest you to choose an Flight Ticket Fare coverage of Rs.{}'.format(outputs))

if __name__=='__main__':
    main()
