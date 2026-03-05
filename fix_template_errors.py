#!/usr/bin/env python3

import re

# Read the file
with open('/home/ghost/Desktop/Zetumart-online-shop/zetumart_app/templates/index.html', 'r') as f:
    content = f.read()

# List of patterns to fix
patterns = [
    (r"{% static 'assets/img/favicon\.png'%}", r"{% static 'assets/img/favicon.png'%}"),
    (r"{% static 'assets/img/apple-touch-icon\.png'%}", r"{% static 'assets/img/apple-touch-icon.png'%}"),
    (r"{% static 'assets/vendor/bootstrap/css/bootstrap\.min\.css'%}", r"{% static 'assets/vendor/bootstrap/css/bootstrap.min.css'%}"),
    (r"{% static 'assets/vendor/bootstrap-icons/bootstrap-icons\.css'%}", r"{% static 'assets/vendor/bootstrap-icons/bootstrap-icons.css'%}"),
    (r"{% static 'assets/vendor/aos/aos\.css'%}", r"{% static 'assets/vendor/aos/aos.css'%}"),
    (r"{% static 'assets/vendor/fontawesome-free/css/all\.min\.css'%}", r"{% static 'assets/vendor/fontawesome-free/css/all.min.css'%}"),
    (r"{% static 'assets/vendor/glightbox/css/glightbox\.min\.css'%}", r"{% static 'assets/vendor/glightbox/css/glightbox.min.css'%}"),
    (r"{% static 'assets/vendor/swiper/swiper-bundle\.min\.css'%}", r"{% static 'assets/vendor/swiper/swiper-bundle.min.css'%}"),
    (r"{% static 'assets/css/main\.css'%}", r"{% static 'assets/css/main.css'%}"),
]

# Apply all fixes
for pattern, replacement in patterns:
    content = re.sub(pattern, replacement, content)

# Write back to file
with open('/home/ghost/Desktop/Zetumart-online-shop/zetumart_app/templates/index.html', 'w') as f:
    f.write(content)

print("Fixed all Django template syntax errors in index.html")
