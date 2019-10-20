"""
Jose-Antonio Rubio
CS 325-400
HW 3
Shopping
"""

def runShopping():
    output = open('results.txt', 'w+')
    with open('shopping.txt', 'r') as file:
        # Read in the number of test cases and strip out un-needed elements
        T = int(file.readline())
        # Loop within the range of the test case
        for tc in range(T):
            # results will hold our items per family member; values will hold the value of each item (summed up at the end); w will hold our total total_weights
            
            r = [] # array to hold the results of items per family member
            total_weights = [] 
            v = [] # array to hold the values of accumilated items
            item_list = {} # object will hold the price as the key and the weight as the value
            items = int(file.readline())
            k = 1 # index marker for parsing through

            # parse through and extract the price and weight of each item
            for item in range(items):
                p, w = map(int, file.readline().split())
                item_list[p] = [w, k]
                k += 1

            # parse through each family member (f) and map the total weight they can carry
            total_fam = int(file.readline().strip())
            for f in range(total_fam):
                total_weights.append(int(file.readline().strip()))
            
            for w in total_weights:
                sorted_p = sorted(item_list.keys())[::-1]
                m = 0 # marker for max weight currently holding
                p = 0 # price
                temp = []

                # Get answer via greedy method. Max p is added to an array of values.
                # Item number will be added to results array
                for i in range(len(item_list)):
                    knapsack = []
                    s = 0
                    p = 0

                    if item_list[sorted_p[i]][0] <= w:
                        s = item_list[sorted_p[i]][0]
                        p = sorted_p[i]
                        knapsack += item_list[sorted_p[i]][1],

                    for j in range(i+1, len(item_list)):
                        if item_list[sorted_p[j]][0] + s <= w:
                            s += item_list[sorted_p[j]][0]
                            p += sorted_p[j]
                            knapsack += item_list[sorted_p[j]][1],

                    if m < p:
                        m = p
                        temp = knapsack

                temp.sort()
                r.append(temp)
                v.append(m)
            # Write results to our output.
            output.write("Test Case: %d\n" % (tc + 1))
            output.write("Total Price: %d\n" % (sum(v)))
            output.write("Member Items:\n")
            # Grab recorded items for each person from results[] and write to output
            for i in range(len(r)):
                output.write("%d: %s\n" % (i + 1, " ".join(map(str, r[i]))))
        output.write('\n')


runShopping()