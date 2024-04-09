from room import Room
from game import GameRunner

gold_room = Room("Gold Room", "You are in a room full of gold. There are exits to the north and east.")
danger_room = Room("Danger Room", "You are in a room with a ghost. The only exit is to the west.")


gold_room.add_paths({'north': danger_room})
danger_room.add_paths({'west': gold_room})


game = GameRunner(start_room=gold_room)
game.play()
