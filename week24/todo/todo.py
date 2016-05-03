# -*- coding: utf-8 -*-

TAGS = [
    'school',
    'home'
]

PRIORITIES = {
    'urgent': 1,
    'normal': 2
}


def skip(f):
    return None


@skip
def add_task(tasks, id, title, deadline, priority, tags):
    """
    >>> tasks = []
    >>> add_task(tasks, '1', 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> tasks == [{'id': '1', 'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': False }]
    True
    """
    pass


@skip
def find_task(tasks, id):
    """
    >>> tasks = []
    >>> add_task(tasks, '1', 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> add_task(tasks, '2', 'Do your homework', '2016-04-30', 'normal', ['school'])
    >>> find_task(tasks, '1')
    0
    """
    pass


@skip
def remove_task(tasks, id):
    """
    >>> tasks = []
    >>> add_task(tasks, '1', 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> remove_task(tasks, '1')
    >>> tasks
    []
    """
    pass


@skip
def complete_task(tasks, id):
    """
    >>> tasks = []
    >>> add_task(tasks, '1', 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> complete_task(tasks, '1')
    >>> tasks[0]['completed']
    True
    """
    pass


@skip
def uncomplete_task(tasks, id):
    """
    >>> tasks = []
    >>> add_task(tasks, '1', 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> complete_task(tasks, '1')
    >>> uncomplete_task(tasks, '1')
    >>> tasks[0]['completed']
    False
    """
    pass


@skip
def get_completed(tasks):
    """
    >>> tasks = []
    >>> add_task(tasks, '1', 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> add_task(tasks, '2', 'Do your homework', '2016-04-30', 'normal', ['school'])
    >>> complete_task(tasks, '1')
    >>> get_completed(tasks) == [{'id': '1', 'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': True}]
    True
    """
    pass


@skip
def get_uncompleted(tasks):
    """
    >>> tasks = []
    >>> add_task(tasks, '1', 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> get_uncompleted(tasks) == [{'id': '1', 'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': False}]
    True
    """
    pass


@skip
def clear_completed(tasks):
    """
    >>> tasks = []
    >>> add_task(tasks, '1', 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> add_task(tasks, '2', 'Do your homework', '2016-04-30', 'normal', ['school'])
    >>> complete_task(tasks, '1')
    >>> clear_completed(tasks)
    >>> tasks == [{'id': '2', 'title': 'Do your homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': False}]
    True
    """
    pass


@skip
def filter_by_tag(tasks, tag):
    """
    >>> tasks = []
    >>> add_task(tasks, '1', 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> add_task(tasks, '2', 'Do your homework', '2016-04-30', 'normal', ['work'])
    >>> filter_by_tag(tasks, 'school') == [{'id': '1', 'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': False}]
    True
    """
    pass


@skip
def filter_by_date_range(tasks, start_date, end_date):
    """
    >>> tasks = []
    >>> add_task(tasks, '1', 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> add_task(tasks, '2', 'Do your homework', '2016-05-10', 'normal', ['work'])
    >>> filter_by_date_range(tasks, '2016-04-20', '2016-05-01') == [{'id': '1', 'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': False}]
    True
    """
    pass


@skip
def order_by_deadline(tasks):
    """
    >>> tasks = []
    >>> add_task(tasks, '1', 'Do your homework', '2016-05-10', 'normal', ['work'])
    >>> add_task(tasks, '2', 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> order_by_deadline(tasks) == [{'id': '2', 'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': False}, {'id': '1', 'title': 'Do your homework', 'deadline': '2016-05-10', 'priority': 'normal', 'tags': ['work'], 'completed': False}]
    True
    """
    pass


@skip
def order_by_priority(tasks):
    """
    >>> tasks = []
    >>> add_task(tasks, '1', 'Do your homework', '2016-05-10', 'normal', ['work'])
    >>> add_task(tasks, '2', 'Do my homework', '2016-04-30', 'urgent', ['school'])
    >>> order_by_deadline(tasks) == [{'id': '2', 'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'urgent', 'tags': ['school'], 'completed': False}, {'id': '1', 'title': 'Do your homework', 'deadline': '2016-05-10', 'priority': 'normal', 'tags': ['work'], 'completed': False}]
    True
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
