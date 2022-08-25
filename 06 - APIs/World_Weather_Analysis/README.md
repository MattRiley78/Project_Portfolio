# World_Weather_Analysis
## Project Overview
The PlanMyTrip app team is beta-testing a new feature on their app platform to help users plan their trips based on weather preferences using real-time weather data.  After initial beta-testing, it has been requested to create a way for users to identify potential travel destinations and hotels to plan a multi-city itinerary.  This should conveniently be displayed on easy-to-read maps and markers.

## Results

Three different deliverables were created in order to achieve the final result:

1. API request using api.openweathermap.org to retrieve real-time weather data from a broad source of up to 2,000 random locations in order to get a large cross-section of choices for the user.

### Example of DataFrame
![DataFrame_Example](https://user-images.githubusercontent.com/106561880/179436850-e9910c3d-6888-4ad4-a8db-21373e678a56.png)


2. A filtered list is generated based on temperature preferences as inputted by the user.  Using additional API requests, closest hotel choices are added for each preferred city.  An interactive Google map with markers is generated so the user can view possible locations.
![WeatherPy_vacation_map](https://user-images.githubusercontent.com/106561880/179436867-f15c73ba-06ec-41b1-bb39-a31550081b4c.png)

3. Once an itinerary is selected, final maps are created to show the travel route and current weather conditions in destination cities.
![WeatherPy_travel_map](https://user-images.githubusercontent.com/106561880/179436883-2e477458-ac7a-4574-a297-f27885be7b76.png)
![WeatherPy_travel_map_markers](https://user-images.githubusercontent.com/106561880/179436889-c40e8f68-e2a7-4323-8672-9660177c4a79.png)
