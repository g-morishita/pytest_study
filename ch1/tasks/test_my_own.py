from collections import namedtuple
from datetime import datetime

Task = namedtuple('Task', ['summary', 'deadline', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, datetime.today().strftime("%Y-%m-%d"), None, False, None)

def test_deadline():
    """default of deadline should be today"""
    task = Task()
    assert task.deadline == datetime.today().strftime("%Y-%m-%d")
