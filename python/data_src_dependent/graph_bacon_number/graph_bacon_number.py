from bridges.bridges import *
from bridges.graph_adj_list import *
from bridges.data_src_dependent.data_source import *

class Link():

    def __init__(self, nextVal, it = None):
        self.element = it
        self.next = nextVal

    def __call__(self):
        return self.next, self.element

    def next(self):
        return self.next

    def setNext(self, nextVal):
        self.next = nextVal
        return self.next

    def element(self):
        return self.element

    def setElement(self, it):
        self.element = it
        return self.element

class LQueue:

    def __init__(self, size = None):
        self.front = self.rear = Link(nextVal=None)
        self.size = 0


    def clear(self):
        self.__init__()

    def enqueue(self, it):
        self.rear.setNext(Link(nextVal=None, it=it))
        self.rear = self.rear.next
        self.size += 1

    def dequeue(self):
        assert self.size != 0, "queue is empty"
        it = self.front.next.element
        self.front.setNext(self.front.next.next)
        if self.front.next is None:
            self.rear = self.front
        self.size -= 1
        return it

    def frontValue(self):
        assert self.size != 0, "queue is empty"
        return self.front.next().element()

    def length(self):
        return self.size


def get_bacon_number(gr, src_actor, dest_actor, mark, dist, parent):
    #need to use queue, as we are soing a BFS search
    lq = LQueue()

    #add soruce actor to the queue
    lq.enqueue(src_actor)

    #inits
    mark[src_actor] = "visited"
    dist[src_actor] = 0
    parent[src_actor] = "none"

    #BFS Traversal
    while lq.length() > 0: #non empty queue

        vertex = lq.dequeue()

        #get adjacencey list of vertex
        sl_list = gr.get_adjacency_list(vertex)
        sle = sl_list
        while(sle is not None):
            #get destination vertex
            w = sle.value.tov

            # if unvisited, mark it as visited and add to the queue,
            # increment distance and point parent back to vertex
            if(mark[w] == ("unvisited")):
                mark[w] = "visited"
                lq.enqueue(w)

                #update the distance and parent values
                dist[w] = dist.get(vertex) + 1
                parent[w] = vertex

                # if we found the destination actor, then we are done
                #we want to highlight the actor and the path to the source
                # actor; we use the parent links to retrace (not source actor's
                # parent is "none" for us to stop
                if(w == dest_actor):#found it
                    #highlight the actor and path using
                    #the parent values and the hashmap
                    #to trace back the sequence of nodes
                    #to the source

                    #highlight the nodes and the links in the path from the source
                    #to the destination actor
                    p = dest_actor
                    while(p is not "none"):

                        #color the nodes in the path
                        #example gr.getVisualizer(key-val).setColor("red")

                        gr.get_visualizer(p).color = "red"
                        gr.get_visualizer(p).size = 50
                        gr.get_visualizer(p).opacity = 1.0

                        # next, color the link but check the parent is not "none", else you will
                        # get an exception
                        # example: gr.getLinkVisualizer(src-key, dest-key).setColor("red")
                        par = parent[p]
                        if(par is not "none"):
                            gr.get_link_visualizer(p, par).color = "red"
                            gr.get_link_visualizer(p, par).thickness = 10

                        p = par

                    return dist[dest_actor]
            sle = sle.next


def main():
    args = sys.argv[1:]

    # create the Bridges object, set credentials

    bridges = Bridges(int(args[0]), args[1], args[2])

    if len(args) > 3:
        bridges.connector.set_server(args[3])

    # set title for visualization
    bridges.set_title("Bacon Number: IMDB Actor-Movie Data")

    # use an adjacency list based graph
    gr = GraphAdjList()

    actor_list = get_actor_movie_imdb_data(1814)

    for k in range(len(actor_list)):

        # get the actor movie names
        actor = actor_list[k].actor
        movie = actor_list[k].movie

        # our graph needs to have a unique set of actors and movies
        # so create the actor and movie vertices only if they dont already
        # exist use an STL map to check for that

        vertices = gr.vertices

        # add actor if does not exist
        if (actor not in vertices):
            gr.add_vertex(actor, actor)

        # add movie if does not exist
        if (movie not in vertices):
            gr.add_vertex(movie, movie)

        # create the edge -- assumes no duplicate edges
        # undirected graph, edges go both ways
        gr.add_edge(actor, movie, 1)
        gr.add_edge(movie, actor, 1)

        # TO DO : Highlight "Cate_Blanchett" node and the movie nodes she is
        # connected to in "red" and do the same for "Kevin_Bacon_(I)" in "green"
        # specify colors by their names, "red", for example
        if (actor == ("Cate_Blanchett")):
            gr.get_link_visualizer(actor, movie).color = "orange"
            gr.get_visualizer(actor).color = "orange"
            gr.get_visualizer(movie).color = "orange"
        if (actor == ("Kevin_Bacon_(I)")):
            gr.get_link_visualizer(actor, movie).color = "green"
            gr.get_visualizer(actor).color = "green"
            gr.get_visualizer(movie).color = "green"

    # set the data structure handle and visualize the input graph
    bridges.set_data_structure(gr)
    bridges.visualize()

    mark = dict()
    parent = dict()
    dist = dict()

    # init maps for bacon number algorithm
    items = list(gr.vertices.keys())
    for i in range(len(items)):
        mark[items[i]] = "unvisited"
        parent[items[i]] = "none"
        dist[items[i]] = 0

    d = get_bacon_number(gr, "Kevin_Bacon_(I)", "Cate_Blanchett", mark, dist, parent)

    print("Bacon Number[Kevin Bacon to Cate Blanchett]: " + str(d))

    bridges.set_data_structure(gr)
    bridges.visualize()


if __name__ == "__main__":
    main()