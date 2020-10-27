from django import template


register=template.Library()


def Lower(value):
    return value.lower()

@register.filter()
def replace_char(value,arg):
    return value.replace(arg,'b')


'''
    value=data,
    arg='h'
    replace_char('hai hello python','h')

'''
register.filter('low',Lower)
#register.filter('rep',replace_char)