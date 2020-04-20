class Category:
    category_count = 0
    name = ""

    def __init__(self, name):
        self.name = name
        Category.category_count += 1
