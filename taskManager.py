class TaskManager:
    tasks = []
    path="cash.csv"

    def __init__(self):
        self.load_data()

    def save_data(self):
        with open(self.path, "w", encoding="utf-8") as file:
            for i in self.tasks:
                file.write(f"{i['name']}:{i['description']}\n")

    def load_data(self):
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                contents = file.readlines()
                if contents=="":
                    return
                for i in contents:
                    values = i.split(':')
                    self.create_task(values[0], values[1])
        except FileNotFoundError:
            print("файл не найден")

    def create_task(self, name, description):
        self.tasks.append({'name': name, 'description': description})
        self.save_data()

    def get_str_tasks(self):
        if not self.tasks:
            return "нет задач"
        str_tasks = ""
        for i in self.tasks:
            str_tasks+=f"{i['name']}: {i['description']}\n"
        return str_tasks