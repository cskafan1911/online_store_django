from django import template

register = template.Library()


@register.simple_tag()
@register.filter()
def mediapath(val):
    if val:
        return f"/media/{val}"

    return ''


@register.filter()
def strip(val, num):
    if len(val) < num:
        return val
    return val[:(num-3)] + '...'
