freq_list = [800, 1200, 2000, 3500, 5800]       # MHz
gain_list = [12.3, 12.5, 12.1, 11.8, 11.2] 

data_list = list(zip(freq_list,gain_list))

for x,y in data_list:
    print(x,y)