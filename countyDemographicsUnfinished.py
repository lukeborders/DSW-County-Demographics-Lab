import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))
    print(your_interesting_demographic_function(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first = counties[0]["County"]
    for c in counties:
        if c["County"] < first:
            first = c["County"]
    return first
def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    nameC = counties[0]["County"]
    nameS = counties[0]["State"]
    highest = counties[0]["Age"]["Percent Under 18 Years"]
    for a in counties:
        if a["Age"]["Percent Under 18 Years"] > highest:
            highest = a["Age"]["Percent Under 18 Years"]
            nameC = a["County"]
            nameS = a["State"]
    return nameC + "," + nameS
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    highest = counties[0]["Age"]["Percent Under 18 Years"]
    for age in counties:
        if age["Age"]["Percent Under 18 Years"] > highest:
            highest = age["Age"]["Percent Under 18 Years"]
        return highest
def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    countyName = counties[0]["County"]
    stateName = counties[0]["State"]
    highest = counties[0]["Age"]["Percent Under 18 Years"]
    for age in counties:
        if age["Age"]["Percent Under 18 Years"] > highest:
            highest = age["Age"]["Percent Under 18 Years"]
            countyName = age["County"]
            stateName = age["State"]
    return [countyName,stateName,highest]
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    dictStates = {}
    for d in counties:
        if d["State"] in dictStates:
            dictStates[d["State"]] += 1
        else:
            dictStates[d["State"]] = 1
    #Find the state in the dictionary with the most counties
    highest = dictStates["AL"]
    state = dictStates["AL"]
    for i, t in dictStates.items():
        if t > highest:
            highest = t
            state = i
    #Return the state with the most counties
    return state
    return (maximum, dictStates,[maximum])
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    for c in counties:
        if c["County"] == "Autauga County":
            return c["Miscellaneous"]["Percent Female"]
        

if __name__ == '__main__':
    main()
