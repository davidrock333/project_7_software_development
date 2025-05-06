"""Module providing lib from Streamlit to design our webpage and controller to logic procedures """
import streamlit as st
import controller.controller as c

''' This is a docstring that describes how app.py builds our webpage.
    url Define URL file origin
    df_vehicle Charge to df_vehicle the information from the URL file origin.
    st.header Initialize a header and write the definition of the title on the webpage.
    check_hist and check_dis: Check the status of the checkbox and execute the procedure to draw graphs.
    Initializing two checkboxes to define what kind of graph will be drawn
    If both checkboxes are activated, build 2 graphs.
    Setting all arguments required to draw both graphs
    If just one checkbox is activated, build a histogram or scatter
    If the histogram was activated, setting all arguments required to draw
If scatter was activated, setting all arguments required to draw'''
URL="proyects/project_7_software_development/files/vehicles_us.csv"

df_vehicle = c.charge_file(URL)

st.header('Venta de Vehiculos')
st.write('Grafico por checkbox')

check_hist = st.checkbox("Histograma")
check_dis = st.checkbox("Dispersion")

if (check_hist * check_dis) == 1:
    st.write('Creando un histograma y dispersion para los datos adjuntos')
    st.plotly_chart(c.draw_graph(df_vehicle,'hist','odometer'),use_container_width=True)
    st.plotly_chart(c.draw_graph(df_vehicle,'scat','odometer','odometer'),use_container_width=True)
elif (check_hist * check_dis) != 1:
    if check_hist:
        st.write('Creando un histograma para los datos adjuntos')
        st.plotly_chart(c.draw_graph(df_vehicle,'hist','odometer'),
                        use_container_width=True)
    elif check_dis:
        st.write('Creando la dispersion para los datos adjuntos')
        st.plotly_chart(c.draw_graph(df_vehicle,'scat','odometer','odometer'),
                        use_container_width=True)
