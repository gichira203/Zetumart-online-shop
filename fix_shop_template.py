#!/usr/bin/env python3

import re

# Read the file
with open('/home/ghost/Desktop/Zetumart-online-shop/zetumart_app/templates/shop.html', 'r') as f:
    content = f.read()

# Fix all static template tags
content = re.sub(r"{% static '([^']*)'%}", r"{% static '\1'%}", content)

# Write back to file
with open('/home/ghost/Desktop/Zetumart-online-shop/zetumart_app/templates/shop.html', 'w') as f:
    f.write(content)

print("Fixed Django template syntax errors in shop.html")
