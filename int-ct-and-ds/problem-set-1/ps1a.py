###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Colin
# Collaborators:
# Time: 12/20/2023

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    #* take in the name of data text file as a string
    #* read in its contents
    #* return dictionary that maps cow names to their weights

    cows = {}
    
    with open(filename) as f:
        mylist = f.read().splitlines()
        for line in mylist:
            x, y = line.split(",")
            cows[x] = y
    f.close
    
    return cows


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    
    cowsCopy = sorted(cows.items(), key=lambda item: item[1], reverse=True)

    result = []
    while cowsCopy:
        trip, totalWeight = [], 0
        i = 0
        while i < len(cowsCopy):
            if (totalWeight + int(cowsCopy[i][1]) <= limit):
                trip.append(cowsCopy[i][0])
                totalWeight += int(cowsCopy[i][1])
                cowsCopy.pop(i)
            else:
                i += 1
        if trip:
            result.append(trip)
        
    return result


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    cowsCopy = sorted(cows.items(), key=lambda item: item[1], reverse=True)
    bestVal = float('inf')
    bestSet = None
    for part in get_partitions(cowsCopy):
        #* get:
            # number of trips
            # the best set
        #* check
            # each trip <= limit
        numTrips = 0.0
        maxWeight = 0.0
        for trip in part:
            #* count number of trips
            numTrips += 1
            tripWeight = 0.0
            for item in trip:
                tripWeight += int(item[1])
            if tripWeight > maxWeight:
                maxWeight = tripWeight
        if maxWeight <= limit and numTrips < bestVal:
            bestVal = numTrips
            bestSet = part

    return bestSet


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here

    cows = load_cows('ps1_cow_data.txt')

    #* greedy
    start = time.time()
    greedy = greedy_cow_transport(cows)
    end = time.time()
    greedyTime = end - start

    #* brute force
    start = time.time()
    brute = brute_force_cow_transport(cows)
    end = time.time()
    bruteTime = end - start

    def countTrips(result):
        count = 0.0
        for i in result:
            count+=1
        return count
    
    greedyCount = countTrips(greedy)
    bruteCount = countTrips(brute)

    #* results
    def results(name, time, count):
        print('---------- ' + name + ' Algorithm ----------')
        print('Number of trips = ' + str(count))
        print(f'Runtime = {time:.5f} s')

    results('Greedy', greedyTime, greedyCount)
    print()
    results('Brute-Force', bruteTime, bruteCount)

compare_cow_transport_algorithms()