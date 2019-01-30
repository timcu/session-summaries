'''
Challenge is to read csv file containing three columns
    'race' = the date of the race
    'runner' = the name of the runner running in the race
    'time' = the time in seconds the runner took to run 5 km.

Challenge:
    
1. Find the winner of each race
2. Find each runners fastest time
3. Show places for each runner in each race

@author: Tim

Example data structure for results

{   '2019-01-28': {
        1521: {'runners': ['Annie'], 'place': 1},
        1596: {'runners': ['Bennie'], 'place': 3},
        1752: {'runners': ['Can'], 'place': 7},
        1740: {'runners': ['David'], 'place': 6},
        1687: {'runners': ['Jeen'], 'place': 4},
        1760: {'runners': ['Liran'], 'place': 8},
        1525: {'runners': ['Nikki'], 'place': 2},
        1707: {'runners': ['Sam'], 'place': 5}
        },
    '2019-02-04': {
        1689: {'runners': ['Bennie'], 'place': 5},
        1765: {'runners': ['Can'], 'place': 7},
        1553: {'runners': ['Jeen'], 'place': 2},
        1556: {'runners': ['Jonathan'], 'place': 3},
        1666: {'runners': ['Liran'], 'place': 4},
        1519: {'runners': ['Nikki'], 'place': 1},
        1756: {'runners': ['Sam'], 'place': 6}
        },
    '2019-02-11': {1574: {'runners': ['Annie'], 'place': 2}, 1784: {'runners': ['Bennie'], 'place': 7}, 1695: {'runners': ['David'], 'place': 3}, 1518: {'runners': ['Jeen'], 'place': 1},
        1696: {'runners': ['Jonathan'], 'place': 4}, 1707: {'runners': ['Liran'], 'place': 5}, 1746: {'runners': ['Sam'], 'place': 6} },
    '2019-02-18': {1594: {'runners': ['Annie'], 'place': 3}, 1557: {'runners': ['Bennie'], 'place': 1}, 1658: {'runners': ['Can'], 'place': 8}, 1619: {'runners': ['David'], 'place': 5},
        1702: {'runners': ['Jeen'], 'place': 9}, 1623: {'runners': ['Jonathan'], 'place': 6}, 1656: {'runners': ['Liran'], 'place': 7}, 1606: {'runners': ['Nikki'], 'place': 4}, 1593: {'runners': ['Sam'], 'place': 2} },
    '2019-02-25': {1768: {'runners': ['Annie'], 'place': 9}, 1686: {'runners': ['Bennie', 'Liran'], 'place': 3}, 1565: {'runners': ['Can'], 'place': 1}, 1726: {'runners': ['David'], 'place': 7},
        1650: {'runners': ['Jeen'], 'place': 2}, 1734: {'runners': ['Jonathan'], 'place': 8}, 1687: {'runners': ['Nikki'], 'place': 5}, 1704: {'runners': ['Sam'], 'place': 6} },
    '2019-03-04': {1609: {'runners': ['Annie'], 'place': 3}, 1699: {'runners': ['Can'], 'place': 6}, 1554: {'runners': ['David'], 'place': 1}, 1619: {'runners': ['Jeen'], 'place': 4},
        1562: {'runners': ['Jonathan'], 'place': 2}, 1722: {'runners': ['Liran'], 'place': 7}, 1675: {'runners': ['Sam'], 'place': 5}},
    '2019-03-11': {1599: {'runners': ['Annie'], 'place': 3}, 1565: {'runners': ['Bennie'], 'place': 2}, 1777: {'runners': ['Can'], 'place': 9}, 1745: {'runners': ['David'], 'place': 7},
        1742: {'runners': ['Jeen'], 'place': 6}, 1756: {'runners': ['Jonathan'], 'place': 8}, 1534: {'runners': ['Liran'], 'place': 1}, 1652: {'runners': ['Nikki'], 'place': 5}, 1638: {'runners': ['Sam'], 'place': 4}},
    '2019-03-18': {1724: {'runners': ['Annie'], 'place': 9}, 1673: {'runners': ['Bennie'], 'place': 7}, 1583: {'runners': ['Can'], 'place': 4}, 1607: {'runners': ['David'], 'place': 5},
        1555: {'runners': ['Jeen'], 'place': 2}, 1547: {'runners': ['Jonathan'], 'place': 1}, 1564: {'runners': ['Liran'], 'place': 3}, 1712: {'runners': ['Nikki'], 'place': 8}, 1622: {'runners': ['Sam'], 'place': 6}},
    '2019-03-25': {1689: {'runners': ['Annie'], 'place': 7}, 1601: {'runners': ['Bennie'], 'place': 4}, 1578: {'runners': ['Can'], 'place': 3}, 1628: {'runners': ['David'], 'place': 5},
        1503: {'runners': ['Jeen'], 'place': 1}, 1671: {'runners': ['Liran'], 'place': 6}, 1552: {'runners': ['Nikki'], 'place': 2}, 1729: {'runners': ['Sam'], 'place': 8}},
    '2019-04-01': {1553: {'runners': ['Annie'], 'place': 3}, 1712: {'runners': ['Bennie'], 'place': 5}, 1790: {'runners': ['Can'], 'place': 8}, 1549: {'runners': ['David'], 'place': 2},
        1718: {'runners': ['Jeen'], 'place': 6}, 1544: {'runners': ['Liran'], 'place': 1}, 1648: {'runners': ['Nikki'], 'place': 4}, 1772: {'runners': ['Sam'], 'place': 7}
    }
}

Example data structure for fastest

{
    'Annie': {'time': 1521, 'race': '2019-01-28'},
    'Bennie': {'time': 1557, 'race': '2019-02-18'},
    'Can': {'time': 1565, 'race': '2019-02-25'},
    'David': {'time': 1549, 'race': '2019-04-01'},
    'Jeen': {'time': 1503, 'race': '2019-03-25'},
    'Liran': {'time': 1534, 'race': '2019-03-11'},
    'Nikki': {'time': 1519, 'race': '2019-02-04'},
    'Sam': {'time': 1593, 'race': '2019-02-18'},
    'Jonathan': {'time': 1547, 'race': '2019-03-18'}
}

'''

import csv

with open("run_results.csv", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    first_row = None   # stores the header row from csv file so we know which column has which data
    idx_race = None    # which column in csv file contains race dates
    idx_runner = None  # which column in csv file contains runner names
    idx_time = None    # which column in csv file contains times
    results = {}       # dict to store each runners place in each race
    fastest = {}       # dict to store fastest time of each runner
    for row in csv_reader:
        # if variable first_row exists then we must be now looking at second row or later
        if first_row:
            # capture race, runner and time into their own variables
            race = row[idx_race]
            runner = row[idx_runner]
            time = int(row[idx_time])
            if race not in results:
                # first result for this race so create a dict in results to store data
                results[race] = {}
            if time in results[race]:
                # a previous runner has the same time so store this runner in the list of runners with this time for this race
                results[race][time]['runners'].append(runner)
            else:
                # no other runners have this time for this race (yet) so create a new list for those runners
                results[race][time] = {'runners': [runner]}
            if runner not in fastest or fastest[runner]['time'] > time:
                # this is currently fastest time for this runner so save in fastest dict
                fastest[runner] = {'time': time, 'race': race}
        else:
            # first_row doesn't exist so we must be looking at it now
            first_row = row
            # loop through headings looking for 'race', 'runner' and 'time' and save their column numbers
            for i in range(len(first_row)):
                if first_row[i] == 'race':
                    idx_race = i
                elif first_row[i] == 'runner':
                    idx_runner = i
                elif first_row[i] == 'time':
                    idx_time = i
    # Loop through results to display places of each runner checking for ties
    for race, race_results in results.items():
        # sort results so we can see the order of the finishers
        times = sorted(race_results.keys())
        place = 1
        for time in times:
            # save the runners' place in case we need it later
            race_results[time]['place'] = place
            # print the results. note how we can refer to keys in a dict using the string format function {result[place]} and {result[runners]}
            print('Place {result[place]} of race {race} is {result[runners]} with a time of {minutes:02d}:{seconds:02d}'.format(result=race_results[time], race=race, minutes=(time // 60), seconds=(time % 60)))
            place += len(race_results[time]['runners'])
    # print fastest times and their race for each runner
    for runner, fastest_race in fastest.items():
        print('Fastest time for runner {0} was in race {1} with a time of {2:02d}:{3:02d}'.format(runner, fastest_race['race'], fastest_race['time'] // 60, fastest_race['time'] % 60))
