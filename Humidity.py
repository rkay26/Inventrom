import requests
import numpy as np
from plotly.offline import init_notebook_mode, plot
import plotly.graph_objs as go

if __name__ == '__main__':

    # Input URL
#    url = 'http://beta.boltiot.com/fetchFromTable?fields=time_stamp,hum&duration=month&deviceName=BOLT1351489&from=&to='
    print('URL?')    
    url = input()
    # Request URL
    res = requests.get(url)
    
    # Retrieve JSON 
    data = res.json()
    
    # Extract time and Humidity Levels
    device_name = data['device name']
    time_stamp = list()
    humidity_value = list()
    for i in data['data']:
        time = i[0]
        time_stamp.append(time[4:])
        humidity_value.append(float(i[1]))
    
    print("Displaying information of {} sensor".format(device_name))

    # Creating Numpy arrays
    time_x = np.array(time_stamp)
    humidity_y = np.array(humidity_value)
 
   # Describe Layout of the graph
    plot_data = [trace0]
    init_notebook_mode(connected=True)
    title_Graph = 'Time-stamp v/s Humidity Level (' + device_name + ')'
    layout = go.Layout(
                title=title_Graph,
                showlegend=True,
                height=600,
                width=1350,
                yaxis = dict(
                            title='Humidity Level',
                            zeroline = False,
                            autorange=True,
                            ticks='outside',
                            tick0=0,
                            ticklen=8,
                            tickwidth=4,
                            tickcolor='#000',
                            titlefont = dict(
                                            size = 16        
                                        ),
                            tickfont = dict(
                                            size = 11
                                        )
                        ),
                xaxis = dict(
                            title='Time',
                            zeroline = False,
                            autorange=True,
                            ticks='outside',
                            tick0=0,
                            ticklen=8,
                            tickwidth=4,
                            tickcolor='#000',
                            titlefont = dict(
                                            size = 16       
                                        ),
                            tickfont = dict(
                                            size = 11
                                        ),
                            tickmode = 'auto',
                            tickangle = 90
                        ),
                font = dict(
                            family='Roboto', 
                            size=20, 
                            color='#5e2222'
                        ),
            )
    
    # Show graph
    fig = dict(data=plot_data, layout=layout )
    plot(fig)
    
