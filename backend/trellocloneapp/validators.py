import re
from django.core.exceptions import ValidationError

def validate_rgb(value):
    if not re.match(r'^#([A-Fa-f0-9]{6})$', value):
        raise ValidationError(f"{value} is not a valid RGB color code")