#  Hint:  You may not need all of these.  Remove the unused functions.


# Given a package with a weight limit limit and a list weights of item weights, implement a function get_indices_of_item_weights that finds two items whose sum of weights equals the weight limit limit. Your function will return an instance of an Answer tuple that has the following form:

# (zero, one)

# where each element represents the item weights of the two packages. The higher valued index should be placed in the zeroth index and the smaller index should be placed in the first index. If such a pair doesn’t exist for the given inputs, your function should return None.

# NOTE: When calling hash_table_retrieve with a key that doesn't exist in the hash table, hash_table_retrieve will return None.

# Your solution should run in linear time.

# Example:

# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21



from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    print(f"weights: {weights} length: {length} limit: {limit}")
    """
    YOUR CODE HERE
    """
    #i have a list of weights, and those weights have values that may or may not add up to the limit that is being passed. the idea is that i need to look through these in a hash table to find the values if they exist that add up and return their indices in the array/list.

    #lets stick them into my little hash table, we will pass in the value as key as well as the index of it. ht is expecting a key and value -> def hash_table_insert(hash_table, key, value):
    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)
    
    for i in range(0, length):
        print(f"limit: {limit} weights[i]: {weights[i]}")
        #lets begin a search for our values/keys
        target = limit - weights[i]
        # def hash_table_retrieve(hash_table, key):
        answer = hash_table_retrieve(ht, target)
        #if we find our answer and it exists in our ht, return it
        if answer:
            print(f"answer: {answer}, i: {i}")
            #tuple()
            return (answer, i)

    # print(f"ht: {ht}")
    return None

        # weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40] len: 9 lim: 7

        # self.assertTrue(answer_4[0] == 6)
        # self.assertTrue(answer_4[1] == 2)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# from hashtables import (HashTable,
#                         hash_table_insert,
#                         hash_table_remove,
#                         hash_table_retrieve,
#                         hash_table_resize)

# def integer_pairs(arr, sum):
#     ht = HashTable(16)

#     # Loop through the list and store each key value pair into a hash table
#     for i in range(len(arr)):
#         difference = hash_table_retrieve(ht, arr[i])
#         if difference is None:
#             hash_table_insert(ht, sum-arr[i], arr[i])
            
#         else:
#             return (arr[i], difference)
#     return None


# print(integer_pairs([9], 0)) # None
# print(integer_pairs([4, 4], 8)) # [4, 4]
# print(integer_pairs([4, 6, 10, 15, 16], 21)) # [15, 6]
# print(integer_pairs([12, 6, 7, 14, 19, 3, 0, 25, 40], 7)) # [0, 7]
# print(integer_pairs([4, 6, 10, 15, 16], 27)) # None