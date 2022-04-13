import pandas as pd

data = pd.read_csv("fase2\spotify_top50_2021.csv")

top10 = data.head(10)
df10 = pd.DataFrame({"artist": top10["artist_name"], "cancion" : top10["track_name"]})
df10.to_csv("fase2\top10.csv")

populares = data.sort_values(by="popularity")
populares = populares.head(10)
populares.to_csv("fase2\populares.csv")

danceability = data.sort_values(by="danceability")
danceability = danceability.head(10)
danceability.to_csv("fase2\danceability.csv")
