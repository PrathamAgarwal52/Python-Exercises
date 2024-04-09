from room import Room
from game import GameRunner

gold_room = Room("Gold Room", "You are in a room full of gold. There are exits to the north and east.")
koi_pond_room = Room("Koi Pond Room", "You are in a room with a serene koi pond. The only exit is to the west.")


gold_room.add_paths({'north': koi_pond_room})
koi_pond_room.add_paths({'west': gold_room})


game = GameRunner(start_room=gold_room)
game.play()
