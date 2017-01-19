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
    :type array
    :return heap nodelist ordered
    :type array
    '''
    def build(self, tree):
        for elem_idx in xrange(1, len(tree)):
            self.check(tree, elem_idx)
        return tree

    def check(self, tree, elem_idx):
        #check parent
        if (elem_idx - 1) / 2 >= 0:
            if tree[elem_idx] < tree[(elem_idx-1)/2]:
                self.swap(tree, elem_idx, (elem_idx-1)/2)
                self.check(tree, (elem_idx-1)/2)

        #check childs
        if self.get_childs(tree, elem_idx) != []:
            childs = self.get_childs(tree, elem_idx)
            min_idx_so_far = elem_idx
            for i in childs:
                if tree[i] < tree[min_idx_so_far]:
                    min_idx_so_far = i
            if elem_idx != min_idx_so_far:
                self.swap(tree, elem_idx, min_idx_so_far)
                self.check(tree, min_idx_so_far)

        if elem_idx < 0:
            return
        '''
        #check left child
        if len(tree) > 2*elem_idx + 1:
            if tree[elem_idx] > tree[2*elem_idx+1]:
                self.swap(tree, elem_idx, 2*elem_idx+1)

        # check right child
        if len(tree) > 2*elem_idx + 2:
            if tree[elem_idx] > tree[2*elem_idx+2]:
                self.swap(tree, elem_idx, 2*elem_idx+2)
        '''
        return

    '''
    swap elements in array at index a and b with each other
    :param tree
    :type array
    :param elem_idx1
    :type int
    :param elem_idx2
    :type int
    '''
    def swap(self, tree, elem_idx1, elem2_idx):
        _tmp = tree[elem_idx1]
        tree[elem_idx1] = tree[elem2_idx]
        tree[elem2_idx] = _tmp

    '''
    return the minimum of the binary tree stored by design as root element
    '''
    def get_root(self, tree):
        return tree[0]

    '''
    insert a new element into the tree
    '''
    def insert_elem(self, tree, elem):
        tree.append(elem)
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
    remove element at index elem_idx and rebuild the tree
    '''
    def remove_elem_at_idx(self, tree, elem_idx):
        tree.pop(elem_idx)
        tree.insert(elem_idx, tree.pop())
        self.check(tree, elem_idx)
        #self.build(tree)

    '''
    removes first occurence of the given element in tree top-down from root to leafs
    and rebuilds the tree afterwards
    '''
    def remove_first_elem(self, tree, elem):
        for i in xrange(0, len(tree)):
            if tree[i] == elem:
                tree.pop(i)
                self.build(tree)
                return


    '''
    removes all elements of list elems from the tree and rebuilds the tree afterwards
    '''
    def remove_all_elements(self, tree, elements):
        for i in xrange(len(tree)-1, -1, -1):
            #print i, tree[i]
            if tree[i] in elements:
                tree.pop(i)
        self.build(tree)

    '''
    remove subtree from tree at the given subroot index. rebuilt tree afterwards
    '''
    def remove_subtree(self, tree, subroot_idx):
        if subroot_idx < len(tree):
            tree.pop(subroot_idx)
            self.remove_subtree(tree, 2 * subroot_idx + 1)
            self.remove_subtree(tree, 2 * subroot_idx)
        else:
            self.build(tree)
            return

    '''
    returns the subtree of tree at the given subroot
    '''
    def get_subtree(self, tree, subroot_idx, subtree):
        if subroot_idx < len(tree):
            subtree.append(tree[subroot_idx])
            self.get_subtree(tree, subroot_idx * 2 + 1, subtree)
            while subroot_idx < len(tree):
                subtree.append(tree[subroot_idx-1])
                subtree.append(tree[subroot_idx])
                subroot_idx = subroot_idx * 2 + 2
            return subtree
        return subtree

    '''
    get a list of child_idx
    :param tree
    :type array
    :param elem_idx
    :type int
    :return array of childs ([] -> no childs, [x] -> only left child index, [x,y] -> index of both childs)
    :rtype array
    '''
    def get_childs(self, tree, elem_idx):
        childs = []
        if len(tree) > 2 * elem_idx + 1:
            childs.append(2*elem_idx + 1)   #append left child
        if len(tree) > 2 * elem_idx + 2:
            childs.append(2 * elem_idx + 2) #append right child
        return childs

    '''
    get the parent of a element
    :param tree
    :type array
    :param elem_idx
    :type int
    :return parent
    :rtype int
    '''
    def get_parent(self, tree, elem_idx):
        if elem_idx == 0:
            return None #The root has no parent
        if len(tree) > elem_idx:
            return (elem_idx-1) / 2

    '''
    get the sibling of an element
    :param tree
    :type array
    :param elem_idx
    :type int
    :return sibling
    :rtype int
    '''
    def get_sibling(self, tree, elem_idx):
        if elem_idx % 2 == 0:
            return elem_idx - 1 #return left sibling (always exists, if there is a right sibling)
        elif len(tree) > elem_idx + 1:
            return elem_idx + 1 #return right sibling if one exists
        else:
            return None #return None if elem is odd and the last in tree

    '''
    get a list of indizes from the given element to the root
    :param tree
    :type array
    :param elem_idx
    :type int
    :return array of indizes
    :rtype array
    '''
    def get_rootpath(self, tree, elem_idx):
        path=[]
        path.append(elem_idx)
        while self.get_parent(tree, elem_idx) != None:
            elem_idx = self.get_parent(tree, elem_idx)
            path.append(elem_idx)
        return path


class Node:
    '''
    :param value - value of node e.g. 50 for type int
    :type object
    :param idx - index of node in tree structure
    :type int
    :param parent_idx - index of the parent node (-1 if node is root element)
    :type int
    :param childs_idx - index of child nodes (empty [] if the node is a leaf)
    :type array
    :param type - type of the node (values are: 0 -> root; 1 -> inner node; 2 -> leaf)
    :type int
    '''
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
    for elem in tree:
        nodelist.append(Node(elem))

    print "Heap structure: " + str(h.build(tree))
    h.insert_elem(tree, 27)
    h.insert_elem(tree, 3)
    h.insert_elem(tree, 18)
    h.insert_elem(tree, 1)
    h.insert_elem(tree, 19)
    print "Inserted {27, 3, 18, 1, 19}: " + str(tree)
    h.remove_root(tree)
    print "Root removed: " + str(tree)
    h.remove_elem_at_idx(tree, 0)
    print "Tree[0]=root removed: " + str(tree)
    '''

    #h.remove_elem_at_idx(tree, 0)
    #print tree
    h.remove_elem_at_idx(tree, 2)
    print tree
    #h.remove_first_elem(tree, 1)
    #print tree
    h.insert_elem(tree, 1)
    print tree
    h.remove_all_elements(tree, [1, 5])
    print tree
    #print h.get_subtree(tree, 2)
    #h.remove_subtree(tree, 2)
    print tree
    # for i in xrange(0, len(arr) - 1):
    #     if i == 0:
    #         continue
    #     print arr[i], arr[(i-1)/2]
    '''

