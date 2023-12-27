###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Colin
# Collaborators:
# Time: 
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}, top_down=True):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    if top_down:
        #* top down (memoization)
        # recursive function that tries to hit target_weight
        if (egg_weights, target_weight) in memo:
            return memo[(egg_weights, target_weight)]
        if target_weight == 0:
            return 0
        if not egg_weights or egg_weights[0] > target_weight:
            # explore right branch only
            return float('inf')
        
        # explore left branch
        withEggs = 1 + dp_make_weight(
            egg_weights, target_weight - egg_weights[0], memo
        )
        # explore right branch
        withoutEggs = dp_make_weight(
            egg_weights[1:], target_weight, memo
        )
        # choose better branch
        result = min(withEggs, withoutEggs)
        # store in memo
        memo[(egg_weights, target_weight)] = result
        return result
    
    else:
        #* bottom up (tabulation)
        # initialize a table where index is target weight and all start an inf except 0, which would require 0 eggs
        countEggs = [float('inf')] * (target_weight + 1)
        countEggs[0] = 0

        # iterate through each target weight
        for i in range(1, target_weight + 1):
            # iterate through each egg weight
            for j in range(len(egg_weights)):
                # here tabulate the results, checking if adding the egg and its sub problem improves the count
                if egg_weights[j] <= i:
                    countEggs[i] = min(countEggs[i], 1 + countEggs[i - egg_weights[j]])
        # return the answer
        return countEggs[target_weight]

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    # eggCopy = tuple(sorted(egg_weights, reverse=True))
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n
                                           , top_down=False
                                           ))
    print()