class TaskManager:
    tasks = []
    def create_task(self, name, description):
        self.tasks.append({'name': name, 'description': description})

    def get_str_tasks(self):
        str_tasks = ""
        for i in self.tasks:
            str_tasks+=f"{i['name']}: {i['description']}\n"
        return str_tasks