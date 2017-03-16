# Include a function that takes at least two user arguments from the command line
# Contain at least one if/else statement
# Perform a caclulation on a list
# Use at least one dictionary
# Have one try/except clause for every function
# Output something (write) to a file, using string formatting
# Must include docstrings telling us how to run your script.

# You can just run this from your command line
import csv

# Read in my file real_estate.tsv so I can mess around with that data
f = open("./real_estate.tsv",'rt')
reader = csv.reader(f, delimiter='\t') 

def read_in_tsv(my_file):
    # f = open(file_path)
    my_file = tsv.reader(f)
    return my_file

# Use a dictionary to count the number of cities in the file by tracking the city name and count per city.
# Use at least one if/else statement
# Create an empty dictionary
city_count = {}
for row in reader:
    city_name = row[1]
#For every row, check if city name is in the dictionary. Each time it appears, add another tally to the list for that city.
    if city_name in city_count:
        city_count[city_name] += 1
    else:
        city_count[city_name] = 1

print (city_count)

# Perform a caclulation on a list
# I want to calculate how many homes in Sacramento are in this list
try:
    reader = csv.reader(f)
    for row in reader:
        city_name = row[1]
        if row[1] == "SACRAMENTO":
            print (city_name)
        else:
            pass

#Find the average home price
for row in reader:
    home_price = row[9]
    avg = sum(home_price)/len(home_price)
    print(avg)

finally:
    f.close()

