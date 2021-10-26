from Classes_and_Objects.Exercises.To_do_List.project.task import Task


# from project.task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleared = 0
        for index in range(len(self.tasks) - 1, -1, -1):
            if self.tasks[index].completed:
                self.tasks.pop(index)
                cleared += 1
        return f"Cleared {cleared} tasks."

    def view_section(self):
        list_of_tasks = [f"Section {self.name}:"]
        for task in self.tasks:
            list_of_tasks.append(task.details())
        return "\n".join(list_of_tasks)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
