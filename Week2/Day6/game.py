from room import Room

class GameRunner:
    def __init__(self, start_room):
        self.current_room = start_room

    def play(self):
        while self.current_room:
            print("\n" + "-"*10)
            print(self.current_room.name)
            print(self.current_room.description)
            
            choice = input("Choose your path: ").lower()
            if choice == 'exit':
                print("Exiting game...")
                break
            
            next_room = self.current_room.next_room(choice)
            if next_room:
                self.current_room = next_room
            else:
                print("Invalid choice. Try again.")
