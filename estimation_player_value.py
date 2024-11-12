import pickle
import streamlit as st

tim = pickle.load(open('estimation_players_value.sav','rb'))
st.title('estimation players value euro')

potential = st.number_input('Input potential')
age = st.number_input('Input age')
crossing = st.number_input('Input crossing ')
finishing = st.number_input('Input finishing')
heading_accuracy = st.number_input('Input heading accuracy')
short_passing = st.number_input('Input short passing ')
dribbling= st.number_input('Input dribbling')
ball_control= st.number_input('Input ball control')
freekick_accuracy= st.number_input('Input freekick accuracy')
long_passing= st.number_input('Input long passing')
acceleration= st.number_input('Input acceleration')
sprint_speed= st.number_input('Input sprint speed')
agility = st.number_input('Input agility')
reactions = st.number_input('Input reactions')
balance = st.number_input('Input balance')
shot_power = st.number_input('Input shot power')
jumping = st.number_input('Input jumping')
stamina = st.number_input('Input stamina')
strength = st.number_input('Input strength')
long_shots = st.number_input('Input long shots')
aggression = st.number_input('Input aggression')
interceptions = st.number_input('Input interceptions')
positioning = st.number_input('Input positioning')
marking = st.number_input('Input marking')
sliding_tackle = st.number_input('Input sliding tackle')

predict = ''

if st.button('Estimation value'):
    predict = tim.predict(
        [[potential,age,crossing,finishing,heading_accuracy,short_passing,dribbling,ball_control,freekick_accuracy,long_passing,acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,stamina,strength,long_shots,aggression,interceptions,positioning,marking,sliding_tackle]]
    )
    st.write('Estimation players value euro :', predict
    ) 