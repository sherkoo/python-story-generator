import random

class Story:
  def __init__(self, setting, character, character_trait, arc, time_of_year):
    self.setting = setting
    self.character = character
    self.character_trait = character_trait
    self.arc = arc
    self.time_of_year = time_of_year

  def print_all(self):
    print("The story takes place in a " + self.setting + ". The main character is " + self.character + " " + self.character_trait + " with a " + self.arc + " The time of year is " + self.time_of_year)