from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
from data_src_dependent.bst_shakespeare.BST import *
import sys

def main():
    args = sys.argv[1:]

    # create the Bridges object, set credentials

    bridges = Bridges(int(args[0]), args[1], args[2])

    if len(args) > 3:
        bridges.connector.set_server(args[3])

    bridges.set_title("Shakespeare Sonnets, Poems, PLays")

    shksp_list = get_shakespeare_data(textonly=True)

    bst = BST()

    for i in range(len(shksp_list)):
        bst.insert(shksp_list[i].get_title(), shksp_list[i])

    bridges.set_data_structure(bst.get_tree_root())
    bridges.visualize()

if __name__ == '__main__':
    main()