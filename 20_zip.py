
names = ['Aashiq', 'Suhail', 'Omar']
residences = ['Anantnag', 'Pulwama', 'Srinagar']
designations = ['AE', 'JE', 'SP']

for name, residence, designation in zip(names, residences, designations):
    print(f'{name} is from {residence} and is currently {designation}')
