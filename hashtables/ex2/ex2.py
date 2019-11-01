#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

# where the source string represents the starting airport and the destination string represents the next airport along our trip. The ticket for your first flight has a destination with a source of NONE, and the ticket for your final flight has a source with a destination of NONE.

# The crux of this problem requires us to 'link' tickets together to reconstruct the entire trip. For example, if we have a ticket ('SJC', 'BOS') that has us flying from San Jose to Boston, then there exists another ticket where Boston is the starting location, ('BOS', 'JFK').

# We can hash each ticket such that the starting location is the key and the destination is the value. Then, when constructing the entire route, the ith location in the route can be found by checking the hash table for the i-1th location.

def reconstruct_trip(tickets, length):
    print(f"tickets: {tickets} length: {length}")
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # ticket_1 = Ticket("NONE", "PDX")
    # ticket_2 = Ticket("PDX", "DCA")
    # ticket_3 = Ticket("DCA", "NONE")

    #we need to insert the tickets and attach them to a starting location and a destination location. start: key, dest: value
    for i in range(0, length):
        print(f"tickets: {tickets[i]}")
    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)