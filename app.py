import pandas as pd 
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import plotly

st.set_page_config(page_title='Dashboard', layout='wide')
st.title(":rainbow[CRICKET ANALYSIS]")
with st.sidebar:
    selected = option_menu(menu_title="Main Menu",options=["Data", "Visualization", "Bar Charts","Analysis"]
                       ,menu_icon="house",default_index=0)
df=pd.read_csv('C:/Users/user/OneDrive/Desktop/new/data.csv')

if selected=="Data":
    df
    st.subheader(":violet[Descrpition about the player]")
    selected_player = st.selectbox("Select Any Player", df['Player'].unique())
    st.write(f"## Information for {selected_player}")
    individual_data = df[df['Player'] == selected_player]
    if not individual_data.empty:
       st.write(individual_data)
    
if selected=="Visualization":
    st.subheader(':red[Top 10 players of the Season]')
    fig6 = px.bar(x=df['Player'].head(10),y=df['Runs'].head(10),
               width=350,labels=dict(x="Player", y="Runs"),color=df['Player'].head(10))
    st.plotly_chart(fig6, use_container_width=True)

    fig10 = px.bar(data_frame=df, x='Total runs', y='Team',
              color=df['Team'], width=350)
    st.plotly_chart(fig10, use_container_width=True)

    st.subheader(':red[Relation Between number of runs scored by each player with boundaries and without boundaries]')
    st.scatter_chart(data=df, x='total run by boundary', y='runs without boundaries',color='Player', width=350,use_container_width=True)
    st.subheader(':red[50s and 100s scored by each team]')
    fig = px.bar(df, x="Ipl Teams ", y=["50",'100'],
             color_discrete_sequence=['blue', 'orange'],barmode='group')
    st.plotly_chart(fig, use_container_width=True)

if selected=="Bar Charts":
    selected_team= st.selectbox("Select Any Team ", df['Ipl Teams '].unique())
    a= df[df['Ipl Teams '] == selected_team][['Player', '4s','6s','Runs','50','100']]
    col1,col2=st.columns(2)
    with col1:
        st.subheader(':red[Number of 4s by each player ]')
        fig6 = px.bar(data_frame=a, x='4s', y='Player',
              color_discrete_sequence=px.colors.qualitative.Antique,labels=dict(x="4s", y="Player"), width=350)
        st.plotly_chart(fig6, use_container_width=True)
    with col2:
        st.subheader(':red[Number of 6s by each player ]')
        fig7 = px.bar(data_frame=a, x='6s', y='Player',
              color_discrete_sequence=px.colors.qualitative.Antique,labels=dict(x="6s", y="Player"), width=350,)
        st.plotly_chart(fig7, use_container_width=True)

    st.subheader(':green[Runs contributed by players for their Team]')
    fig=px.pie( values=a['Runs'], names=a['Player'],color_discrete_sequence=px.colors.qualitative.Pastel,width=250)
    st.plotly_chart(fig, use_container_width=True)
    st.subheader(':green[50s and 100s scored by each player]')
    fig7 = px.bar(a,x='Player',y=['50','100'],barmode="group",color_discrete_sequence=px.colors.qualitative.Set2,width=200)
    st.plotly_chart(fig7, use_container_width=True)
    
if selected=="Analysis":
        st.markdown(":red[Highest Run Scorer::] Jos Buttler was the highest Run Scorer of the season with 863 runs")
        st.markdown("")
        st.markdown(":red[Most 50s by Team::] Gujarat Titans was the team who has most of 50s with 14 50s")
        st.markdown("")
        st.markdown(":red[Most 50s by Individual::] Jos Buttler with 4 Half Centuries")
        st.markdown("")
        st.markdown(":red[Most Run Scored by Team::] Rajasthan Royals was the highest Run Scorer of the season with 2683 runs")
        st.markdown("")