from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
from data_src_dependent.bst_gutenburg.BST import *
import sys


class BST:
    def __init__(self):
        self.root = None
        self.node_count = 0

    def get_tree_root(self):
        return self.root

    def clear(self):
        self.root = None
        self.node_count = 0

    def insert(self, k, e):
        self.root = self.insert_help(self.root, k, e)
        self.node_count += 1

    def remove(self, k):
        temp = self.find_help(self.root, k)
        if temp is not None:
            self.root = self.remove_help(self.root, k)
            self.node_count -= 1
        return temp

    def find_help(self, rt, k):
        if rt is None:
            return None
        if rt.get_key() > 0:
            return self.find_help(rt.get_left(), k)
        elif rt.get_key() == 0:
            return rt.get_value()
        else:
            return self.find_help(rt.get_right(), k)

    def insert_help(self, rt, k, e):
        if rt is None:
            n = BSTElement(key=k, e=e)
            gb = n.value
            n.label = gb.title
            return n
        if rt.key > k:
            rt.left = self.insert_help(rt.left, k, e)
        else:
            rt.right = self.insert_help(rt.right, k, e)
        return rt

    def remove_help(self, rt, k):
        if rt is None:
            return None
        if rt.key > k:
            rt.left = self.remove_help(rt.get_left(), k)
        elif rt.key < k:
            rt.right = self.remove_help(rt.get_right(), k)
        else:
            if rt.left is None:
                return rt.right
            elif rt.right is None:
                return rt.left
            else:
                temp = self.get_min(rt.right)
                rt.value = temp.value
                rt.label = temp.key
                rt.key = temp.key
                rt.right = self.delete_min(rt.right)
        return rt

    def get_min(self, rt):
        if rt.left is None:
            return rt
        else:
            return self.get_min(rt.left)

    def delete_min(self, rt):
        if rt.left is None:
            return rt.right
        else:
            rt.left = self.delete_min(rt.left)
            return rt

def main():
    args = sys.argv[1:]

    # create the Bridges object, set credentials

    bridges = Bridges(int(args[0]), args[1], args[2])

    if len(args) > 3:
        bridges.connector.set_server(args[3])

    bridges.set_title("GutenBerg book collection(meta data only)")

    book_list = get_gutenberg_book_data()

    bst = BST()

    for i in range(len(book_list)):
        bst.insert(book_list[i].title, book_list[i])

    bridges.set_data_structure(bst.get_tree_root())
    bridges.visualize()


if __name__ == '__main__':
    main()