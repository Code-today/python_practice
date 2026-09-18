#population estimate in an area
population = 307357870
deaths = (365*24*60*60)/13 # a death every 13 seconds
births = (365*24*60*60)/7 # a birth every 7 seconds
immigration = (365*24*60*60)/35 # an immigrant every 35 seconds
No_years = int(input("Enter the number of years to estimate population growth: "))
estimated_population = population + (No_years * (births - deaths + immigration))
rate_change = (estimated_population - population) / population * 100
print(f"Estimated population after {No_years} years: {estimated_population:,.0f}")
print(f"Rate of change in population: {rate_change:.2f}%")
