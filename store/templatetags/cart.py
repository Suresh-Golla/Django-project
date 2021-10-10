from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;  


    #     try:
    #         a = int(id)
    #     except:
    #         if a == product.id:
    #             return cart.get(id)
    # return 0;
        