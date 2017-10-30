import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))

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
    dictStates = {
        'AK': '19',
        'AL': '67',
        'AR': '75',
        'AZ': '15',
        'CA': '58',
        'CO': '64',
        'CT': '8',
        'DE': '3',
        'FL': '67',
        'GA': '159',
        'HI': '5',
        'IA': '99',
        'ID': '44',
        'IL': '102',
        'IN': '92',
        'KS': '105',
        'KY': '120',
        'LA': '64',
        'MA': '14',
        'MD': '24',
        'ME': '16',
        'MI': '83',
        'MN': '87',
        'MO': '114',
        'MS': '82',
        'MT': '56',
        'NC': '100',
        'ND': '53',
        'NE': '93',
        'NH': '10',
        'NJ': '21',
        'NM': '33',
        'NV': '16',
        'NY': '62',
        'OH': '88',
        'OK': '77',
        'OR': '36',
        'PA': '67',
        'RI': '5',
        'SC': '46',
        'SD': '66',
        'TN': '95',
        'TX': '254',
        'UT': '29',
        'VA': '95',
        'VT': '14',
        'WA': '39',
        'WI': '75',
        'WV': '55',
        'WY': '23'
}
    #Find the state in the dictionary with the most counties
	maximum = max(dictStates, key=dictStates.get)
    #Return the state with the most counties
	return (maximum, dictStates,[maximum])
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
	interFact = counties[0]["County"]
	for i in counties:
		if interFact > counties[0]:
			return interFact

if __name__ == '__main__':
    main()
