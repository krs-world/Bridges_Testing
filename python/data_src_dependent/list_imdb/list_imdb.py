from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
from bridges.sl_element import *
import sys

class ListIMDB:
    args = sys.argv[1:]

    # create the Bridges object, set credentials

    bridges = Bridges(int(args[0]), args[1], args[2])

    if len(args) > 3:
        bridges.connector.set_server(args[3])

    #Set an assignment title
    bridges.set_title("ListIMDB Example")

    # get a List of ActorMovieIMDB objects from DataSource
    myList = get_actor_movie_imdb_data(1800)

    # Setup a prev and head element
    prev = SLelement()
    head = SLelement()

    # Read each actor movie pair and setup a new SLelement for each
    for i in range(len(myList)):

        # Create each new SLelement
        element = SLelement()

        # Set the element label equal to 'Actor = Movie' for each pair.(print it out for sanit Check)
        element.label = (myList[i].actor + " - " + myList[i].movie)

        # add 'next' pointer where appropriate
        if (i > 0):
            prev.next = element
        else:
            # Set head pointer
            head = element
        # update prev pointer
        prev = element

    # Pass head of the list to Bridges
    bridges.set_data_structure(head)

    # Visualize the list
    bridges.visualize()