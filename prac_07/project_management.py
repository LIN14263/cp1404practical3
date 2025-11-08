"""Console app to manage projects (load/save/filter/update/display)."""
from __future__ import annotations
from datetime import datetime
import csv
from project import Project, DATE_FMT

MENU = """Menu:
(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate a project
(Q)uit
>>> """

DEFAULT_FILE = "projects.csv"  # use CSV with header:
# Name,Start Date,Priority,Cost Estimate,% Complete


def main() -> None:
    projects: list[Project] = []
    filename = DEFAULT_FILE
    print("Welcome to Project Management")

    while True:
        choice = input(MENU).strip().upper()
        if choice == "Q":
            print("Goodbye!")
            return
        if choice == "L":
            filename = input("File to load (default projects.csv): ").strip() or DEFAULT_FILE
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("File to save to (default projects.csv): ").strip() or DEFAULT_FILE
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_by_date(projects)
        elif choice == "A":
            projects.append(prompt_new_project())
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")


def load_projects(filename: str) -> list[Project]:
    projects: list[Project] = []
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)  # skip header
        for row in reader:
            if not row or all(not x.strip() for x in row):
                continue
            projects.append(Project.from_csv(row))
    return projects


def save_projects(filename: str, projects: list[Project]) -> None:
    with open(filename, "w", encoding="utf-8", newline=""):
        pass  # create/truncate first to avoid Windows locking
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "% Complete"])
        for p in projects:
            writer.writerow(p.to_csv())


def display_projects(projects: list[Project]) -> None:
    if not projects:
        print("No projects loaded")
        return
    incomplete = sorted([p for p in projects if not p.is_complete()], key=lambda p: p.priority)
    complete = sorted([p for p in projects if p.is_complete()], key=lambda p: p.priority)

    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")

    print("Complete projects:")
    for p in complete:
        print(f"  {p}")


def filter_by_date(projects: list[Project]) -> None:
    if not projects:
        print("No projects loaded")
        return
    date_text = input(f"Show projects that start after date ({DATE_FMT}): ")
    try:
        cutoff = datetime.strptime(date_text, DATE_FMT).date()
    except ValueError:
        print("Invalid date format")
        return
    for project in sorted([p for p in projects if p.start_date >= cutoff], key=lambda p: p.start_date):
        print(project)


def prompt_new_project() -> Project:
    name = input("Name: ").strip()
    start_text = input(f"Start date ({DATE_FMT}): ").strip()
    priority = _prompt_int("Priority: ")
    cost = _prompt_float("Cost estimate: $")
    percent = _prompt_int("Percent complete: ")
    start_date = datetime.strptime(start_text, DATE_FMT).date()
    return Project(name, start_date, priority, cost, percent)


def update_project(projects: list[Project]) -> None:
    if not projects:
        print("No projects loaded")
        return
    index = _choose_project(projects)
    project = projects[index]
    print(project)
    new_percent_text = input("New percentage (leave blank to keep current): ").strip()
    if new_percent_text:
        project.percent_complete = int(new_percent_text)
    new_priority_text = input("New priority (leave blank to keep current): ").strip()
    if new_priority_text:
        project.priority = int(new_priority_text)


def _choose_project(projects: list[Project]) -> int:
    for i, p in enumerate(projects):
        print(i, p)
    while True:
        try:
            idx = int(input("Project number: "))
            if 0 <= idx < len(projects):
                return idx
        except ValueError:
            pass
        print("Invalid index; try again.")


def _prompt_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer; try again.")


def _prompt_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number; try again.")


if __name__ == "__main__":
    main()
