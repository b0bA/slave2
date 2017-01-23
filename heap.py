#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Description """

__version__ = "0.1"

__author__ = "Michael Brendel"
__copyright__ = "2017, Alere Technologies"


class Heap:
    def __init__(self):
        pass

    '''
    build heap
    :param nodelist - unordered list of nodes
    :type list
    :return heap nodelist ordered
    :type list
    '''
    def build(self, tree):
        for node_idx in xrange(1, len(tree)):
            self.check(tree, node_idx)
        return tree

    def check(self, tree, node_idx):
        #check parent
        if (node_idx - 1) / 2 >= 0:
            if tree[node_idx] < tree[(node_idx-1)/2]:
                self.swap(tree, node_idx, (node_idx-1)/2)
                self.check(tree, (node_idx-1)/2)
                self.check(tree, node_idx)

        #check childs
        if(not self.is_leaf(tree, node_idx)):
            childs = self.get_childs(tree, node_idx)
            min_idx_so_far = node_idx
            for i in childs:
                if tree[i] < tree[min_idx_so_far]:
                    min_idx_so_far = i
            if node_idx != min_idx_so_far:
                self.swap(tree, node_idx, min_idx_so_far)
                self.check(tree, min_idx_so_far)
                self.check(tree, node_idx)

        return

    def swap(self, tree, node_idx1, node2_idx):
        """
        swap nodes in list at index node_idx1 and node2_idx with each other
        :param tree: list containing the treestructure
        :param node_idx1: index of node 1
        :param node_idx2: index of node 2
        :type tree: list
        :type node_idx1: int
        :type node_idx1: int
        """
        _tmp = tree[node_idx1]
        tree[node_idx1] = tree[node2_idx]
        tree[node2_idx] = _tmp

    def get_root(self, tree):
        """
        return the minimum of the heap stored by design as root node
        :param tree: list containing the treestructure
        :type tree: list
        :return: root node
        :rtype: node
        """
        return tree[0]

    def insert_nodes(self, tree, nodes):
        """
        insert notes from list into the tree
        :param tree: list containing the treestructure
        :param nodes: list of nodes to be inserted into tree
        :type tree: list
        :type nodes: list
        ..todo:: check if node is of type node
        """
        for node in nodes:
            #if type(node) == Node:
            tree.append(node)
            self.check(tree, len(tree)-1)

    def insert_subtree(self, tree, subtree):
        #check if subtree is a valid binary tree
        pass

    '''
    remove the root of the tree and rebuild it
    '''
    def remove_root(self, tree):
        tree.pop(0)
        self.build(tree)

    '''
    remove node at index node_idx and rebuild the tree
    '''
    def remove_node_at_idx(self, tree, node_idx):
        tree.pop(node_idx)
        tree.insert(node_idx, tree.pop())
        self.check(tree, node_idx)
        #self.build(tree)

    '''
    removes first occurence of the given node in tree top-down from root to leafs
    and rebuilds the tree afterwards
    '''
    def remove_first_node(self, tree, node):
        for i in xrange(0, len(tree)):
            if tree[i] == node:
                tree.pop(i)
                self.build(tree)
                return


    '''
    removes all nodes of list nodes from the tree and rebuilds the tree afterwards
    '''
    def remove_all_nodes(self, tree, nodes):
        for i in xrange(len(tree)-1, -1, -1):
            #print i, tree[i]
            if tree[i] in nodes:
                tree.pop(i)
        self.build(tree)

    def remove_subtree(self, tree, subroot_idx):
        """
        remove subtree from tree at the given subroot index. rebuilt tree afterwards
        ..todo:: implement
        """
        if subroot_idx < len(tree):
            tree.pop(subroot_idx)
            self.remove_subtree(tree, 2 * subroot_idx + 1)
            self.remove_subtree(tree, 2 * subroot_idx)
        else:
            self.build(tree)
            return

    def get_subtree(self, tree, subroot_idx, subtree):
        """
        returns the subtree of tree at the given subroot
        ..todo:: implement
        """
        if subroot_idx < len(tree):
            subtree.append(tree[subroot_idx])
            self.get_subtree(tree, subroot_idx * 2 + 1, subtree)
            while subroot_idx < len(tree):
                subtree.append(tree[subroot_idx-1])
                subtree.append(tree[subroot_idx])
                subroot_idx = subroot_idx * 2 + 2
            return subtree
        return subtree

    def get_childs(self, tree, node_idx):
        """
        get a list of child_idx
        :param tree: list containing the treestructure
        :param node_idx: index of the node trying to find the childs of
        :type tree: list
        :type node_idx: int
        :return: - list of the childs_indizes [left_child_idx, right_child_idx]
                 - empty list [], if no child was found (node at node_idx is leaf)
        :rtype: list

        ..note:: if a node has child(s) it will always have a left child
        """
        childs = []
        if len(tree) > 2 * node_idx + 1:
            childs.append(2*node_idx + 1)   #append left child
        if len(tree) > 2 * node_idx + 2:
            childs.append(2 * node_idx + 2) #append right child
        return childs

    def get_parent(self, tree, node_idx):
        """
        get the parent of a node
        :param tree: list containing the treestructure
        :param node_idx: index of the node trying to find the parent of
        :type tree: list
        :type node_idx: int
        :return: - index of the parent, if parent is found
                 - None, otherwise (in a valid treestructure only root has no parent)
        :rtype: int
        """
        if node_idx == 0:
            return None #The root has no parent
        if len(tree) > node_idx:
            return (node_idx-1) / 2

    def get_sibling(self, tree, node_idx):
        """
        get the sibling of a node
        :param tree: list containing the treestructure
        :param node_idx: index of the node trying to find the sibling of
        :type tree: list
        :type node_idx: int
        :return: - index of the sibling, if sibling is found
                 - None, otherwise
        :rtype: int
        """
        if node_idx % 2 == 0:
            return node_idx - 1 #return left sibling (always exists, if there is a right sibling)
        elif len(tree) > node_idx + 1:
            return node_idx + 1 #return right sibling if one exists
        else:
            return None #return None if node is odd and the last in tree

    def get_rootpath(self, tree, node_idx):
        """
        get a list of indizes from the given node to the root
        :param tree: list containing the treestructure
        :param node_idx: index of the node starting bottom-up till root
        :type tree: list
        :type node_idx: int
        :return: list of indizes of nodes on the path from node_idx to root
                (node_idx is the first node of this list and the root is the last node of this list
        :rtype: list
        """
        path=[]
        path.append(node_idx)
        while self.get_parent(tree, node_idx) != None:
            node_idx = self.get_parent(tree, node_idx)
            path.append(node_idx)
        return path

    def is_leaf(self, tree, node_idx):
        """
        return if the node at the given index is a leaf or not 
        :param tree: list containing the treestructure
        :param node_idx: index of the node to check
        :type tree: list
        :type node_idx: int
        :return: true if node is leaf, otherwise false
        :rtype: bool
        """
        if node_idx > (len(tree)-1)/2:
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
    h = Heap()

    nodelist = []
    for node in tree:
        nodelist.append(Node(node))

    print "Heap structure: " + str(h.build(tree))
    h.insert_nodes(tree, [27, 3, 18, 1, 19])
    print "Inserted {27, 3, 18, 1, 19}: " + str(tree)
    h.remove_root(tree)
    print "Root removed: " + str(tree)
    h.remove_node_at_idx(tree, 0)
    print "Tree[0]=root removed: " + str(tree)
    h.remove_node_at_idx(tree, 2)
    print "Tree[2] removed: " + str(tree)
    h.remove_first_node(tree, 5)
    print "First Node with value=5 removed: " + str(tree)
    h.insert_nodes(tree, [5, 1, 0, 1, 5])
    print "Inserted {5, 1, 0, 1, 5}: " + str(tree)
    h.remove_all_nodes(tree, [1, 5])
    print "Removed all nodes with value 1 or 5 : " + str(tree)
    print "Check, if root is leaf : " + str(h.is_leaf(tree, 0))
    print "Check, if node at (treesize-1)/2 = " + str((len(tree)-1)/2) + " is leaf : " + str(h.is_leaf(tree, (len(tree)-1)/2))
    print "Check, if node at treesize/2 = " + str(len(tree)/2) + " is leaf : " + str(h.is_leaf(tree, len(tree)/2))
    print "Check, if last node = treesize-1 = " + str(len(tree)-1) + " is leaf : " + str(h.is_leaf(tree, len(tree)-1))
    p_i = h.get_rootpath(tree, len(tree)-1)
    print "Get path to root from last node = treesize-1 = " + str(len(tree)-1) + " : " + str(p_i)


    '''
    get_sibling
    get_parent
    get_childs

    #print h.get_subtree(tree, 2)
    #h.remove_subtree(tree, 2)
    print tree
    # for i in xrange(0, len(arr) - 1):
    #     if i == 0:
    #         continue
    #     print arr[i], arr[(i-1)/2]
    '''

