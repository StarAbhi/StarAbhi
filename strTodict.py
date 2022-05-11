def city_info(city_string):
    city_string = city_string.split(',')
    for index in range(len(city_string)):
        city_string[1] = int(city_string[1])
        city_string[2] = float(city_string[2])
 
    return tuple(city_string)

def country_and_city_pop(a_string):
    new_list= []
    city_info = list(city_info(a_string))
    country_index = a_string.find(":")
    country = a_string[:country_index]
    for city in city_info:
        population = city_info[1]
        new_list.insert(0, country)
        new_list.insert(1, population)
    return tuple(new_list)
    
def country_and_city_pop(string):
    pass
string = ['India:Jaipur,5000000,467.1', 'India:Ajmer,415000,54.92', 'Italy:Milan,13520000,181.8']
countries  = country_and_city_pop(string)
print(type(countries))
print(type(countries['New Zealand']))
#print_dict_in_order(countries)