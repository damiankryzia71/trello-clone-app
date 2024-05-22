from django.db import models
from . import validators as vd

class Account(models.Model):
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField()

    def __str__(self):
        return f"#{self.id}: {self.username}"
    
    def create_board(self, name: str):
        board = Board(name = name, account = self, status = "active")
        return board


class Board(models.Model):
    name = models.CharField(max_length = 50)
    STATUS_CHOICES = {
        "active": "active",
        "archived": "archived"
    }
    status = models.CharField(choices = STATUS_CHOICES, default = "active")
    account = models.ForeignKey("Account", on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.name}"

    def create_card(self, name: str):
        card = Card(name = name, board = self, status = "active")
        return card

class Card(models.Model):
    name = models.CharField(max_length = 50)
    STATUS_CHOICES = {
        "active": "active",
        "archived": "archived"
    }
    status = models.CharField(choices = STATUS_CHOICES, default = "active")
    board = models.ForeignKey("Board", on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.name}"
    
    def create_color_tag(self, color: str):
        color_tag = ColorTag(color = color, card = self)
        return color_tag
    

class ColorTag(models.Model):
    color = models.CharField(validators = [vd.validate_rgb])
    card = models.ForeignKey("Card", on_delete = models.CASCADE)

    def __str__(self):
        return f"Color tag {self.color} assigned to card {self.card}"