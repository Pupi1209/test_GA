import osmnx as ox

place_name = "Яр-Сале, Ямало-Ненецкий автономный округ, Россия"
# pois_list = ["school", "kindergarten", "government", "hospital", "pharmacy", "fuel", "restaurant", "bank", "library",
#     "college", "university", "clinic", "dentist", "bus_station", "taxi", "supermarket", "mall",
#     "marketplace", "post_office", "sports_centre", "stadium", "theatre", "cinema", "police",
#     "fire_station", "atm"] Способ не выбран, так как многие POI не имеют типа, но их добавление имеет смысл для анализа. 15 записей против 75

# Загрузка POI
# tags = {"amenity": pois_list}  # Фильтр по категориям
# pois = ox.features_from_place(place_name, tags)

# Загрузка зданий и POI
pois = ox.features_from_place(place_name, {"name": True})
buildings = ox.features_from_place(place_name, {"building": True})

#Перевод полученной выгрузки в датафрейм
pois_df = pois[["name", "geometry", "amenity"]].reset_index()
pois_df = pois_df.rename(columns={"amenity": "type"})
pois_df["latitude"] = pois_df["geometry"].centroid.y
pois_df["longitude"] = pois_df["geometry"].centroid.x

# Сохранение данных
pois_df.to_csv("yar_sale_pois.csv", index=False)
buildings.to_file("yar_sale_buildings.geojson", driver="GeoJSON")
