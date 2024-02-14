# import weather
# forecast=weather.forecast('Mumbai',unit=weather.CELSIUS)
# forecast.today['11:00'].temp

# weather.forecast('New york', unit=weather.CELSIUS)

import weather

forecast= weather.forecast('Mumbai',unit=weather.CELSIUS)

forecast.today['1:00'].temp

# forecast.tommorow['11:00'].precip # Get precipitation in New York at 11.00