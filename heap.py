#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Description """

__version__ = "0.1"

__author__ = "Michael Brendel"
__copyright__ = "2017, Alere Technologies"


class Heap:
    def __init__(self, array=[]):
        self.tree = array
        self.build()

    '''
    build heap
    :param nodelist - unordered list of nodes
    :type list
    :return heap nodelist ordered
    :type list
    '''
    def build(self):
        for node_idx in xrange(1, len(self.tree)):
            self.check(node_idx)
        return tree

    def check(self, node_idx):
        #check parent
        if (node_idx - 1) / 2 >= 0:
            if self.tree[node_idx] < self.tree[(node_idx-1)/2]:
                self.swap(node_idx, (node_idx-1)/2)
                self.check((node_idx-1)/2)
                self.check(node_idx)

        #check childs
        if(not self.is_leaf(node_idx)):
            childs = self.get_childs(node_idx)
            min_idx_so_far = node_idx
            for i in childs:
                if self.tree[i] < self.tree[min_idx_so_far]:
                    min_idx_so_far = i
            if node_idx != min_idx_so_far:
                self.swap(node_idx, min_idx_so_far)
                self.check(min_idx_so_far)
                self.check(node_idx)
        return

    def swap(self, node_idx1, node2_idx):
        """
        swap nodes in list at index node_idx1 and node2_idx with each other
        :param node_idx1: index of node 1
        :param node_idx2: index of node 2
        :type node_idx1: int
        :type node_idx1: int
        """
        _tmp = self.tree[node_idx1]
        self.tree[node_idx1] = self.tree[node2_idx]
        self.tree[node2_idx] = _tmp

    def get_root(self):
        """
        return the minimum of the heap stored by design as root node
        :return: root node
        :rtype: node
        """
        return self.tree[0]

    def insert_nodes(self, nodes):
        """
        insert notes from list into the tree
        :param nodes: list of nodes to be inserted into tree
        :type nodes: list
        ..todo:: check if node is of type node
        """
        for node in nodes:
            #if type(node) == Node:
            self.tree.append(node)
            self.check(len(self.tree)-1)

    def insert_subtree(self, subtree):
        #check if subtree is a valid binary tree
        pass

    '''
    remove the root of the tree and rebuild it
    '''
    def remove_root(self):
        self.tree.pop(0)
        self.tree.insert(0, self.tree.pop())
        self.check(0)

    '''
    remove node at index node_idx and rebuild the tree
    '''
    def remove_node_at_idx(self, node_idx):
        self.tree.pop(node_idx)
        self.tree.insert(node_idx, self.tree.pop())
        self.check(node_idx)

    '''
    removes first occurence of the given node in tree top-down from root to leafs
    and rebuilds the tree afterwards
    '''
    def remove_first_node(self, node):
        for i in xrange(0, len(self.tree)):
            if self.tree[i] == node:
                self.tree.pop(i)
                self.tree.insert(i, self.tree.pop())
                self.check(i)
                return

    '''
    removes all nodes of list nodes from the tree and rebuilds the tree afterwards
    '''
    def remove_all_nodes(self, nodes):
        for i in xrange(len(self.tree)-1, -1, -1):
            if self.tree[i] in nodes:
                self.tree.pop(i)
        self.build()

    def remove_subtree(self, subroot_idx):
        """
        remove subtree from tree at the given subroot index. rebuilt tree afterwards
        ..todo:: implement
        """
        if subroot_idx < len(self.tree):
            self.tree.pop(subroot_idx)
            self.remove_subtree(2 * subroot_idx + 1)
            self.remove_subtree(2 * subroot_idx)
        else:
            self.build()
            return

    def get_subtree(self, subroot_idx):
        """
        returns the subtree of tree at the given subroot index
        :param subroot_idx: node with the root of the subtree
        :type subroot_idx: int
        :return subtree: list of subtree elements in heapstructure
        :param subtree: list
        """
        subtree = []
        h = 1
        if 0 <= subroot_idx < len(self.tree):
            subtree.append(self.tree[subroot_idx])
            left_child = 2 * subroot_idx + 1
            while len(self.tree) > left_child:
                subtree.append(left_child)
                right_child = self.get_sibling(left_child)
                if right_child:
                    subtree.append(right_child)
                subtree = self.get_subtree(left_child, subtree)
        return subtree

    def get_childs(self, node_idx):
        """
        get a list of child_idx
        :param node_idx: index of the node trying to find the childs of
        :type node_idx: int
        :return: - list of the childs_indizes [left_child_idx, right_child_idx]
                 - empty list [], if no child was found (node at node_idx is leaf)
        :rtype: list

        ..note:: if a node has child(s) it will always have a left child
        """
        childs = []
        if len(self.tree) > 2 * node_idx + 1:
            childs.append(2*node_idx + 1)   #append left child
        if len(self.tree) > 2 * node_idx + 2:
            childs.append(2 * node_idx + 2) #append right child
        return childs

    def get_parent(self, node_idx):
        """
        get the parent of a node
        :param node_idx: index of the node trying to find the parent of
        :type node_idx: int
        :return: - index of the parent, if parent is found
                 - None, otherwise (in a valid treestructure only root has no parent)
        :rtype: int
        """
        if node_idx == 0:
            return None #The root has no parent
        if len(self.tree) > node_idx:
            return (node_idx-1) / 2

    def get_sibling(self, node_idx):
        """
        get the sibling of a node
        :param node_idx: index of the node trying to find the sibling of
        :type node_idx: int
        :return: - index of the sibling, if sibling is found
                 - None, otherwise
        :rtype: int
        """
        if node_idx == 0:
            return None
        if node_idx % 2 == 0:
            return node_idx - 1 #return left sibling (always exists, if there is a right sibling)
        elif len(self.tree) > node_idx + 1:
            return node_idx + 1 #return right sibling if one exists
        else:
            return None #return None if node is odd and the last in tree

    def get_rootpath(self, node_idx):
        """
        get a list of indizes from the given node to the root
        :param node_idx: index of the node starting bottom-up till root
        :type node_idx: int
        :return: list of indizes of nodes on the path from node_idx to root
                (node_idx is the first node of this list and the root is the last node of this list
        :rtype: list
        """
        path=[]
        path.append(node_idx)
        while self.get_parent(node_idx) != None:
            node_idx = self.get_parent(node_idx)
            path.append(node_idx)
        return path

    def is_leaf(self, node_idx):
        """
        return if the node at the given index is a leaf or not
        :param node_idx: index of the node to check
        :type node_idx: int
        :return: true if node is leaf, otherwise false
        :rtype: bool
        """
        if node_idx > (len(self.tree)-1)/2:
            return True
        return False


class Node:
    """
    :param value - value of node e.g. 50 for type int
    :type object
    :param idx - index of node in tree structure
    :type int
    :param parent_idx - index of the parent node (-1 if node is root node)
    :type int
    :param childs_idx - index of child nodes (empty [] if the node is a leaf)
    :type list
    :param type - type of the node (values are: 0 -> root; 1 -> inner node; 2 -> leaf)
    :type int
    """
    def __init__(self, value=None, idx=None, parent_idx=None, childs_idx=None, type=None):
        self.value = value
        self.idx = idx
        self.parent_idx = parent_idx
        self.childs_idx = childs_idx
        self.type = type

if __name__ == '__main__':
    tree = [5, 12, 6, 9, 7, 2, 14, 8, 13, 1, 5, 16, 3, 10, 11, 4, 15]
    print "Input: " + str(tree)
    tree.reverse()
    print "Reverse: " + str(tree)
    h = Heap(tree)

    nodelist = []
    for node in tree:
        nodelist.append(Node(node))

    print "Heap structure: " + str(h.tree)
    h.insert_nodes([27, 3, 18, 1, 19])
    print "Inserted {27, 3, 18, 1, 19}: " + str(h.tree)
    h.remove_root()
    print "Root removed: " + str(h.tree)
    h.remove_node_at_idx(0)
    print "Tree[0]=root removed: " + str(h.tree)
    h.remove_node_at_idx(5)
    print "Tree[5] removed: " + str(h.tree)
    h.remove_first_node(5)
    print "First Node with value=5 removed: " + str(h.tree)
    h.insert_nodes([5, 1, 0, 1, 5])
    print "Inserted {5, 1, 0, 1, 5}: " + str(h.tree)
    h.remove_all_nodes([1, 5])
    print "Removed all nodes with value 1 or 5 : " + str(h.tree)
    print "Check, if root is leaf : " + str(h.is_leaf(0))
    print "Check, if node at (treesize-1)/2 = " + str((len(h.tree)-1)/2) + " is leaf : " + str(h.is_leaf((len(h.tree)-1)/2))
    print "Check, if node at treesize/2 = " + str(len(h.tree)/2) + " is leaf : " + str(h.is_leaf(len(h.tree)/2))
    print "Check, if last node = treesize-1 = " + str(len(h.tree)-1) + " is leaf : " + str(h.is_leaf(len(h.tree)-1))
    p_i = h.get_rootpath(len(h.tree)-1)
    print "Get path to root from last node = treesize-1 = " + str(len(h.tree)-1) + " : " + str(p_i)
    print "Get sibling of the root (should be empty): " + str(h.get_sibling(0))
    print "Get sibling of the 1st node (should be 2nd node): " + str(h.get_sibling(1))
    print "Get sibling of the 2nd node (should be 1st node): " + str(h.get_sibling(2))
    print "Get sibling of the last node (might be empty): " + str(h.get_sibling(len(h.tree)-1))
    print "Get parent of root (should be empty): " + str(h.get_parent(0))
    print "Get parent of 1st node (should be root = 0): " + str(h.get_parent(1))
    print "Get parent of 2st node (should be root = 0): " + str(h.get_parent(2))
    print "Get parent of the last node: " + str(h.get_parent(len(h.tree) - 1))
    print "Get childs of the root (should return [1, 2]): " + str(h.get_childs(0))
    print "Get childs of the parent of the last node (should return at least the last node): " + str(h.get_childs(h.get_parent(len(h.tree) - 1)))
    print "Get childs of the last node (should return []): " + str(h.get_childs(len(h.tree) - 1))
    print "Subtree at root (should return the whole heap): " + str(h.get_subtree(0))
    print "Subtree at index 3: " + str(h.get_subtree(3))
    print "Subtree at last node (should return the last node only): " + str(h.get_subtree(len(h.tree) - 1))

    '''
    #print h.get_subtree(tree, 2)
    #h.remove_subtree(tree, 2)
    print tree
    # for i in xrange(0, len(arr) - 1):
    #     if i == 0:
    #         continue
    #     print arr[i], arr[(i-1)/2]
    '''

