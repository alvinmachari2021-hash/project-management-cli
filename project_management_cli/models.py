class Task:
    def __init__(self, title):
        self.title = title
        self.complete = False

    def mark_complete(self):
        self.complete = True

    def to_dict(self):
        return {"title": self.title, "complete": self.complete}


class Project:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, task_title):
        task = Task(task_title)
        self.tasks.append(task)

    def to_dict(self):
        return {"title": self.title, "tasks": [t.to_dict() for t in self.tasks]}


class User:
    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, project_title):
        project = Project(project_title)
        self.projects.append(project)

    def to_dict(self):
        return {"name": self.name, "projects": [p.to_dict() for p in self.projects]}