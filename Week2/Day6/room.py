class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def add_paths(self, paths):
        self.paths.update(paths)

    def next_room(self, choice):
        return self.paths.get(choice, None)
