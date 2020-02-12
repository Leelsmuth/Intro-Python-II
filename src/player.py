# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
      # attributes (name, categories)
    self.name = name
    self.current_room = current_room
  def __str__(self):
    return f"{self.name} is currently in {self.current_room}"