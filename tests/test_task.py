import unittest

from wa_backend import Task


class TaskTest(unittest.TestCase):
    def setUp(self):
        self.task = Task("Dummy task", False)

    def tearDown(self):
        # To be implemented if required
        pass

    def test_something(self):
        self.assertEqual(self.task.description, "Dummy task")
        self.assertEqual(self.task.completed, False)
