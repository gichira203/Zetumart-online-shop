from django import template

register = template.Library()

@register.filter
def filter_stock(products, stock_type):
    """Filter products by stock status"""
    if stock_type == 'in_stock':
        return [p for p in products if p.stock > 10]
    elif stock_type == 'low_stock':
        return [p for p in products if 0 < p.stock <= 10]
    elif stock_type == 'out_of_stock':
        return [p for p in products if p.stock == 0]
    return products
