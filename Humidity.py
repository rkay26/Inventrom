import requests
import numpy as np

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
