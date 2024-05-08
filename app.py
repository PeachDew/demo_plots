import streamlit as st
import plotly.express as px

sales = [1200,1100,1300,1500,1400,1700,1900,2100]
fig = px.line(sales)
fig.update_layout(width = 500, height = 275)

b1,b2 = st.columns([1,2])
with b1:
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("## Beautiful")
with b2:
    st.plotly_chart(fig)

st.divider()

i1,i2 = st.columns([2,1])
with i1:
    st.plotly_chart(fig)
with i2:
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("## Interactive")

st.divider()

c1,c2 = st.columns([1,2])
with c1:
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.markdown("## Clear")
with c2:
    st.plotly_chart(fig)