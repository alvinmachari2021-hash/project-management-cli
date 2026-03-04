import pytest
from models import User, Project, Task

def test_add_project():
    user = User("Alex")
    user.add_project("CLI Tool")
    assert user.projects[0].title == "CLI Tool"

def test_add_task():
    user = User("Alex")
    user.add_project("CLI Tool")
    project = user.projects[0]
    project.add_task("Implement add-task")
    assert project.tasks[0].title == "Implement add-task"
    assert project.tasks[0].complete is False

def test_mark_task_complete():
    task = Task("Write tests")
    assert task.complete is False
    task.mark_complete()
    assert task.complete is True