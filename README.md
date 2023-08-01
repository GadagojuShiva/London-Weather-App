# London Weather App

## Overview
London Weather App is a command-line program written in Python that allows users to get hourly weather forecasts for the city of London. It uses the OpenWeatherMap API to fetch weather data and provides the user with three options: getting weather details, wind speed, and pressure for a specific date.

## Prerequisites
Before running the London Weather App, ensure that you have the following installed:
- Python (version 3 or higher)
- Requests library (install using `pip install requests`)

## Getting Started
1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the "weather_app.py" file.

3. Run the program by executing the following command:

## How to Use
1. Upon running the program, you will be presented with the following menu:

2. To select an option, enter the corresponding number (1, 2, 3, or 0) and press Enter.

3. If you choose option 1, you will be prompted to enter a date in the format "YYYY-MM-DD HH:00:00". The program will then display the temperature for the given date.

4. If you choose option 2, you will be prompted to enter a date as well. The program will display the wind speed for the given date.

5. If you choose option 3, you will be prompted to enter a date. The program will display the pressure for the given date.

6. To exit the program, select option 0.

## Examples
Here's an example of how to use the London Weather App:

Enter your choice: 1
Enter the date (yyyy-mm-dd): 2019-03-30
Temperature on 2019-03-30: 284.921 K

Enter your choice: 2
Enter the date (yyyy-mm-dd): 2019-03-31
Wind Speed on 2019-03-31: 5.97 m/s

Enter your choice: 3
Enter the date (yyyy-mm-dd): 2019-03-30
Pressure on 2019-03-30: 1022.206 hPa

#Example: When you Select a worng choice
Enter your choice: 4
Invalid choice. Please try again.

#Example: When the date is not available
Enter your choice: 1
Enter the date (yyyy-mm-dd): 2023-07-31
Data not available for the given date.


## Note
- The weather data is fetched from the OpenWeatherMap API, and it may not have forecasts for all dates. If a date's data is not available, the program will display "Data not available for the given date."

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any issues or questions regarding the London Weather App, please contact Gadagoju Shiva (mailto:gadagojushiva00@gmail.com).

