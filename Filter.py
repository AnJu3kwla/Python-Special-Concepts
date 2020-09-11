import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

filter(lambda x : x > avg, data)
print(filter)
print(list(filter(lambda x : x > avg, data)))
print(list(filter(lambda x : x < avg, data)))

#Remove missing data
countries = ["", "Argintina", "", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "", "", "Venezuela"]
print(list(filter(None,countries)))