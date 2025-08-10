from django import template

register = template.Library()

# Custom filter to get an item from a dictionary
@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)
