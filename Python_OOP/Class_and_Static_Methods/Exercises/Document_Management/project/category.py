class Category:
    def __init__(self, cat_id: int, name: str):
        self.id = cat_id
        self.name = name

    def edit(self, new_name):
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"


