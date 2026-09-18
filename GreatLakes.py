# the great lakes are how big?
total_volume = 22_810  # in cubic kilometers
total_land_area = 9833520  # in square kilometers usa
# depth if water is spread evenly across the land area
depth = total_volume / total_land_area  # in kilometers
depth_meters = depth * 1000  # convert to meters
print(f"If the water from the Great Lakes were spread evenly across the land area of the\
       USA, it would cover the land to a depth of {depth:.6f} kilometers.")
print(f"This is equivalent to a depth of {depth_meters:.2f} meters.")
