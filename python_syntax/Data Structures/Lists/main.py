balkan_countries = ["Albania", "Bosnia and Herzegovina", "Bulgaria", "Greece", "Kosovo", "Montenegro", "North Macedonia", "Romania", "Serbia", "Slovenia", "Croatia", "Turkey" ] # Note that only part of Turkey is in the Balkans

balkan_countries.append("Martin") # adding a new element in list
balkan_countries.extend(["Ristov", "King","Tractor"]) # adding a few elements in list
balkan_countries[0] = "Macedonia" # adding a new item in list on index 0
balkan_countries.remove("Kosovo") # removing element like "Kosovo"
balkan_countries.pop(3) # removing element in index 3
balkan_countries.insert(14,"Skopje") # Inserting new element in list
number_of_one_countries = balkan_countries.count("Macedonia") # counting of word "Macedonia"
print(balkan_countries)
print(number_of_one_countries)
balkan_countries.sort() # sorting list starts with alphabet a
print(balkan_countries)
balkan_countries.reverse() # sorting list on reverse
print(balkan_countries)
number_of_one_balkan_countries = len(balkan_countries)
print(number_of_one_balkan_countries)
balkan_countries.clear() # removing all elements of this list
print(balkan_countries)