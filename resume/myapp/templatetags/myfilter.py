from django import template
register = template.Library()


@register.filter(name='remove_special')
def remove_char(value,arg):
    print(arg)
    print("Value : " , value)
    for charter in arg:
        value = value.replace(charter , "")
        print(charter)
    return value
