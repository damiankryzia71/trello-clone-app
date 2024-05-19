from django.db import models
from . import validators

class Account(models.Model):
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField()

    def __str__(self):
        return f"#{self.id}: {self.username}"
    
    def create_board(self, board_name):
        board = Board(name = board_name, account = self)
        board.save()


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
    
    def create_card(self, card_name: str, color_tags: list[str]):
        card = Card(name = card_name, board = self)
        for i in color_tags:
            card.add_color_tag(i)
        card.save()


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
    
    def add_color_tag(self, color_rgb):
        color_tag = ColorTag(color=color_rgb, card = self)
        color_tag.save()
    
    def move_card(self, board_id):
        board = Board.objects.get(id = board_id)
        self.board = board
        self.save()

class ColorTag(models.Model):
    color = models.CharField(validators = [validators.validate_rgb])
    card = models.ForeignKey("Card", on_delete = models.CASCADE)

    def __str__(self):
        return f"Color tag {self.color} assigned to card {self.card}"