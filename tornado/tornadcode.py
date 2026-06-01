import matplotlib.pyplot as plt

import tropycal.tracks as tracks
import datetime as dt 


basin = tracks.TrackDataset(basin='north_atlantic',source='hurdat',include_btk=False)
season = basin.get_season(2024)
print(season)
storm = basin.get_storm(('milton',2024))
#print(storm.to_dict())
#print(storm.to_dataframe())
#print(storm.to_xarray()) 
#print(storm)
#.plot()
#.show()

storm.plot()
plt.show()


