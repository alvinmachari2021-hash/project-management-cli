import argparse
import storage
from models import User, Project, Task
from utils import pretty_print

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Add user
    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("--name", required=True)

    # Add project
    project_parser = subparsers.add_parser("add-project")
    project_parser.add_argument("--user", required=True)
    project_parser.add_argument("--title", required=True)

    # Add task
    task_parser = subparsers.add_parser("add-task")
    task_parser.add_argument("--project", required=True)
    task_parser.add_argument("--title", required=True)

    # List users
    subparsers.add_parser("list-users")

    # List projects
    project_list_parser = subparsers.add_parser("list-projects")
    project_list_parser.add_argument("--user", required=True)

    # List tasks
    task_list_parser = subparsers.add_parser("list-tasks")
    task_list_parser.add_argument("--project", required=True)

    args = parser.parse_args()
    data = storage.load_data()

    if args.command == "add-user":
        user = User(args.name)
        data["users"].append(user.to_dict())
        storage.save_data(data)
        pretty_print(f"User {args.name} added.")

    elif args.command == "add-project":
        for user in data["users"]:
            if user["name"] == args.user:
                project = Project(args.title)
                user["projects"].append(project.to_dict())
                storage.save_data(data)
                pretty_print(f"Project {args.title} added to user {args.user}.")
                break
        else:
            pretty_print(f"User {args.user} not found.")

    elif args.command == "add-task":
        for user in data["users"]:
            for project in user["projects"]:
                if project["title"] == args.project:
                    task = Task(args.title)
                    project["tasks"].append(task.to_dict())
                    storage.save_data(data)
                    pretty_print(f"Task {args.title} added to project {args.project}.")
                    return
        pretty_print(f"Project {args.project} not found.")

    elif args.command == "list-users":
        for user in data["users"]:
            pretty_print(user["name"])

    elif args.command == "list-projects":
        for user in data["users"]:
            if user["name"] == args.user:
                for project in user["projects"]:
                    pretty_print(project["title"])
                break
        else:
            pretty_print(f"User {args.user} not found.")

    elif args.command == "list-tasks":
        for user in data["users"]:
            for project in user["projects"]:
                if project["title"] == args.project:
                    for task in project["tasks"]:
                        status = "✅" if task["complete"] else "❌"
                        pretty_print(f"{task['title']} {status}")
                    return
        pretty_print(f"Project {args.project} not found.")

if __name__ == "__main__":
    main()