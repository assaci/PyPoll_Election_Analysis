counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if"Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if"Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties .")
if"Arapahoe" in counties and "El paso" not in counties:
    print("only Arapahoe is in the listof counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])
counties_tuple = ("Arapahoe","Denver","Jefferson")
for county in counties_tuple:
    print(county)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
for county, voters in counties_dict.items():
    print(county, voters)
voting_data= [{"county":"Arapahoe","registerd_voters":422829}, {"county":"Denver","registerd_voters":463353}, {"county":"Jefferson","registerd_voters":432438}]
for county_dict in voting_data:
    print(county_dict)

for i in range(len(counties_dict)):
    print(voting_data[i])
for county_dict in voting_data:
    for key, value in county_dict.items():
        print(value)
counties_dict = {"Arapahoe":369237, "Denver":413229, "Jefferson":390222}
for county, voters in counties_dict.items():
    print(county + " county has "+ str(voters) + " register voters. ")
#Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes =int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}."
    f"You received {candidate_votes/total_votes*100}% of the total votes.")
print(message_to_candidate)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county + " county has "+ str(voters) + " register voters. ")

