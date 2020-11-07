"""
print("Hello WOrld")

counties = ["Arapahoe","Denver","Jefferson"]

my_list = list()

print(counties)

print(counties[0])

print (len(counties))

print(counties[0:2])

print(counties.append("El Paso"))

print(counties)

counties.insert(2, "El Paso")

print(counties)

counties.remove("El Paso")

print(counties)

counties.pop(3)

print(counties)

counties[2]="El Paso"

print(counties)

counties.remove("Arapahoe")

print(counties)

counties.insert(2, "Denver")

print(counties)

counties.pop(0)

print(counties)

counties.insert(1, "Jefferson")

print(counties)

my_typle =tuple()

counties_tuple = ("Arapahoe","Denver","Jefferson")

print(counties_tuple)

print(counties_tuple[1])

counties_dict = {}

counties_dict["Arapahoe"] = 422829

print(counties_dict)

counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict)

print(counties_dict.keys())

print(counties_dict.values())

print(counties_dict.get("Denver"))

voting_data=[]

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')


counties=["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


counties=["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


x = 0
while x <= 5:
    print(x)
    x = x + 1

counties = ["Arapahoe","Denver","Jefferson"]

for county in counties:

    print(county)


counties = ["Arapahoe","Denver","Jefferson"]

for i in range(len(counties)):
    print(counties[i])



counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for voters in counties_dict.values():
    print(voters)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(counties_dict[county])


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

"""
"""
voting_data = [``{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, registered_voters in voting_data.items():
    print(f"{county} county has {registered_voters:,} registered voters.")
"""
