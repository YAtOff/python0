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
def add_task(tasks, title, deadline, priority, tags):
    """
    >>> tasks = []
    >>> add_task(tasks, 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> tasks == [{'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': False }]
    True
    """
    pass


@skip
def remove_task(tasks, index):
    """
    >>> tasks = []
    >>> add_task(tasks, 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> remove_task(tasks, 0)
    >>> tasks
    []
    """
    pass


@skip
def complete_task(tasks, index):
    """
    >>> tasks = []
    >>> add_task(tasks, 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> complete_task(tasks, 0)
    >>> tasks[0]['completed']
    True
    """
    pass


@skip
def uncomplete_task(tasks, index):
    """
    >>> tasks = []
    >>> add_task(tasks, 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> complete_task(tasks, 0)
    >>> uncomplete_task(tasks, 0)
    >>> tasks[0]['completed']
    False
    """
    pass


@skip
def get_completed(tasks):
    """
    >>> tasks = []
    >>> add_task(tasks, 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> add_task(tasks, 'Do your homework', '2016-04-30', 'normal', ['school'])
    >>> complete_task(tasks, 0)
    >>> get_completed(tasks) == [{'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': True}]
    True
    """
    pass


@skip
def get_uncompleted(tasks):
    """
    >>> tasks = []
    >>> add_task(tasks, 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> get_uncompleted(tasks) == [{'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': False}]
    True
    """
    pass


@skip
def clear_completed(tasks):
    """
    >>> tasks = []
    >>> add_task(tasks, 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> add_task(tasks, 'Do your homework', '2016-04-30', 'normal', ['school'])
    >>> complete_task(tasks, 0)
    >>> clear_completed(tasks)
    >>> tasks == [{'title': 'Do your homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': False}]
    True
    """
    pass


@skip
def filter_by_tag(tasks, tag):
    """
    >>> tasks = []
    >>> add_task(tasks, 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> add_task(tasks, 'Do your homework', '2016-04-30', 'normal', ['work'])
    >>> filter_by_tag(tasks, 'school') == [{'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': False}]
    True
    """
    pass


@skip
def filter_by_date_range(tasks, start_date, end_date):
    """
    >>> tasks = []
    >>> add_task(tasks, 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> add_task(tasks, 'Do your homework', '2016-05-10', 'normal', ['work'])
    >>> filter_by_date_range(tasks, '2016-04-20', '2016-05-01') == [{'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': False}]
    True
    """
    pass


@skip
def order_by_deadline(tasks):
    """
    >>> tasks = []
    >>> add_task(tasks, 'Do your homework', '2016-05-10', 'normal', ['work'])
    >>> add_task(tasks, 'Do my homework', '2016-04-30', 'normal', ['school'])
    >>> order_by_deadline(tasks) == [{'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'normal', 'tags': ['school'], 'completed': False}, {'title': 'Do your homework', 'deadline': '2016-05-10', 'priority': 'normal', 'tags': ['work'], 'completed': False}]
    True
    """
    pass


@skip
def order_by_priority(tasks):
    """
    >>> tasks = []
    >>> add_task(tasks, 'Do your homework', '2016-05-10', 'normal', ['work'])
    >>> add_task(tasks, 'Do my homework', '2016-04-30', 'urgent', ['school'])
    >>> order_by_deadline(tasks) == [{'title': 'Do my homework', 'deadline': '2016-04-30', 'priority': 'urgent', 'tags': ['school'], 'completed': False}, {'title': 'Do your homework', 'deadline': '2016-05-10', 'priority': 'normal', 'tags': ['work'], 'completed': False}]
    True
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
