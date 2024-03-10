#!/usr/bin/python3
"""Unittests for console.py"""

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import os
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)
            self.assertTrue(output.isalnum())

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

            self.console.onecmd("show BaseModel 1234")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

            self.console.onecmd("destroy BaseModel 1234")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "[]")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

            self.console.onecmd("update BaseModel 1234")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

            self.console.onecmd("update BaseModel 1234 name")
            output = f.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    def test_update_with_dictionary(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create BaseModel')
            output = f.getvalue().strip()
            obj_id = output

            self.console.onecmd(
                    f"update BaseModel {obj_id} {{'name': 'test'}}")
            output = f.getvalue().strip()
            self.assertEqual(output, '')

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            self.console.onecmd("count User")
            output = f.getvalue().strip()
            self.assertEqual(output, "2")

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("quit"))

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_exit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("exit"))

    def test_invalid_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("hello")
            output = f.getvalue().strip()
            self.assertEqual(output, "*** Unknown syntax: hello")

    def test_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create InvalidClass")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")


if __name__ == "__main__":
    unittest.main()
