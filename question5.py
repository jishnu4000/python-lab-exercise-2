# New York City Weather data from 1st August 2024 to 10th August 2024
nyc_weather_data = [
    {'Date': '2024-08-01', 'Max_Temp': 25.1, 'Min_Temp': 21.5, 'Humidity': 43},
    {'Date': '2024-08-02', 'Max_Temp': 34.5, 'Min_Temp': 22.4, 'Humidity': 57},
    {'Date': '2024-08-03', 'Max_Temp': 17.2, 'Min_Temp': 12.7, 'Humidity': 33},
    {'Date': '2024-08-04', 'Max_Temp': 20.3, 'Min_Temp': 24.0, 'Humidity': 80},
    {'Date': '2024-08-05', 'Max_Temp': 33.4, 'Min_Temp': 12.1, 'Humidity': 81},
    {'Date': '2024-08-06', 'Max_Temp': 34.7, 'Min_Temp': 13.5, 'Humidity': 53},
    {'Date': '2024-08-07', 'Max_Temp': 30.2, 'Min_Temp': 5.5, 'Humidity': 68},
    {'Date': '2024-08-08', 'Max_Temp': 16.5, 'Min_Temp': 6.5, 'Humidity': 65},
    {'Date': '2024-08-09', 'Max_Temp': 27.4, 'Min_Temp': 13.4, 'Humidity': 85},
    {'Date': '2024-08-10', 'Max_Temp': 24.3, 'Min_Temp': 10.8, 'Humidity': 70},
]

# function to find the highest and lowest temperatures recorded during the week.
def max_min_temperatures(data):
    # key function returns the max/min temps for the data 
    max_temp = max(data, key=lambda x: x['Max_Temp'])['Max_Temp']
    min_temp = min(data, key=lambda x: x['Min_Temp'])['Min_Temp']
    return max_temp, min_temp

# function to determine the number of days with temperatures above 30°C
def days_above_30(data):
    count = 0
    for day in data:
        if day['Max_Temp'] > 30:
            count += 1
    return count

# function to compute the average humidity over the specified period
def average_humidity(data):
    sum = 0
    for day in data:
        sum += day['Humidity']
    return sum / len(data)

if __name__ == '__main__':
    print(f'The highest and lowest temperatures recorded in (high, low) format: {max_min_temperatures(nyc_weather_data)}')
    print(f'Number of days with maximum temperature above 30 degrees Celsius: {days_above_30(nyc_weather_data)}')
    print(f'Average humidity percentage over the days: {average_humidity(nyc_weather_data)}%')