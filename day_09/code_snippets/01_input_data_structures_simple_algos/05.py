# get the keys and values of a dictionary using a for loop
laptop_mapping = {
    'boobalan': 'hp',
    'sadam': 'lenovo',
    'siraj': 'sony',
    'mohan': 'toshiba'
}


for key, value in laptop_mapping.items():
    print(f"{key} uses a {value} laptop.")
    # bad way. Using + operator
    print(key + " uses a " + value + " laptop.")
    # for those with windows 7 SP1 using python3.4
    print("{} uses a {} laptop.".format(key, value))


print("\n\nMethod 2\n\n")

for key in laptop_mapping.keys():
    print(f"{key} uses a {laptop_mapping[key]} laptop.")
