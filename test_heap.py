#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Description """
from unittest import TestCase
from heap import Heap

__version__ = "0.1"

__author__ = "Michael Brendel"
__copyright__ = "2017, Alere Technologies"


class TestHeap(TestCase):
    arr = [7, 3, 9, 1, 8, 2, 6, 4, 5, 10]
    h1 = Heap()
    h2 = Heap(arr)

    def test_build(self):
        self.assertListEqual(self.h1.tree, [], "Heap is not empty list")
        self.assertListEqual(self.h2.tree, [1, 3, 2, 4, 8, 9, 6, 7, 5, 10], "Heap has unexpected Structure")
        self.assertIsInstance(self.h1, Heap, "Heap is not of type Heap")
        self.assertIsInstance(self.h2, Heap, "Heap is not of type Heap")

    def test_check(self):
        self.fail()

    def test_swap(self):
        self.fail()

    def test_get_root(self):
        self.fail()

    def test_insert_nodes(self):
        self.fail()

    def test_insert_subtree(self):
        self.fail()

    def test_remove_root(self):
        self.fail()

    def test_remove_node_at_idx(self):
        self.fail()

    def test_remove_first_node(self):
        self.fail()

    def test_remove_all_nodes(self):
        self.fail()

    def test_remove_subtree(self):
        self.fail()

    def test_get_subtree(self):
        self.fail()

    def test_get_childs(self):
        self.assertEqual(self.h2.get_childs(0), [1, 2], "Root has no Children")
        self.assertEqual(self.h2.get_childs(3), [7, 8], "Root has a Parent")
        self.assertEqual(self.h2.get_childs(4), [9], "Root has a Parent")
        self.assertEqual(self.h2.get_childs(len(self.h2.tree)-1), [], "Root has a Parent")

    def test_get_parent(self):
        self.assertEqual(self.h2.get_parent(0), None, "Root has a Parent")
        self.assertEqual(self.h2.get_parent(len(self.h2.tree)-1), 4, "Parent of the last node has not the index 3")
        self.assertEqual(self.h2.get_parent(1000), None, "Non-existing node has a parent")

    def test_get_sibling(self):
        self.assertEqual(self.h2.get_sibling(0), None, "Root has a sibling")
        self.assertEqual(self.h2.get_sibling(3), 4, "Wrong sibling")
        self.assertEqual(self.h2.get_sibling(len(self.h2.tree)-1), None, "Root has a sibling")

    def test_get_rootpath(self):
        self.assertEqual(self.h2.get_rootpath(0), [0], "Rootpath is wrong")
        self.assertEqual(self.h2.get_rootpath(len(self.h2.tree)-1), [9, 4, 1, 0], "Rootpath is wrong")

    def test_is_leaf(self):
        self.assertFalse(self.h2.is_leaf(0), "Root is a leaf")
        self.assertFalse(self.h2.is_leaf(4), "Inner node is a leaf")
        self.assertTrue(self.h2.is_leaf(5), "Leaf is not a leaf")
        self.assertTrue(self.h2.is_leaf(len(self.h2.tree)-1), "Last node is not a leaf")

    def test_get_height(self):
        self.assertEqual(0, self.h1.get_height(), "Empty Heap has not 0 height.")
        self.assertEqual(3, self.h2.get_height(), "Heap has not height of 3.")
