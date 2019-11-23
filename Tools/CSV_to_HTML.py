# dependencies
import pandas as pd

# Import data from CSV to Panda Dataframe
CityWeather_df = pd.read_csv('../Resources/Cities_Weather.csv')
CityWeather_df["Date"] = pd.to_datetime(CityWeather_df["Date"],unit="s").dt.strftime("%m/%d/%Y %I:%M %p CDT")
# crushed_visitor.to_html()

with open('../Resources/Cities_Weather.html', 'w') as fo:
    fo.write(CityWeather_df.to_html())