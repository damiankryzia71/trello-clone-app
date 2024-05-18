from django.db import models
from validators import validate_rgb

class Account(models.Model):
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField()

class Board(models.Model):
    name = models.CharField(max_length = 50)
    STATUS_CHOICES = {
        "active": "active",
        "archived": "archived"
    }
    status = models.CharField(choices = STATUS_CHOICES, default = "active")
    account = models.ForeignKey("Account", on_delete = models.CASCADE)

class Card(models.Model):
    name = models.CharField(max_length = 50)
    STATUS_CHOICES = {
        "active": "active",
        "archived": "archived"
    }
    status = models.CharField(choices = STATUS_CHOICES, default = "active")
    board = models.ForeignKey("Board", on_delete = models.CASCADE)

class ColorTag(models.Model):
    color = models.CharField(validators = [validate_rgb])
    card = models.ForeignKey("Card", on_delete = models.CASCADE)