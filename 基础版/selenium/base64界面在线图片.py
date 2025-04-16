import requests
import base64

header, base64_data = data_url.split(',', 1)
image_data = base64.b64decode(base64_data)

with open(filename, 'wb') as f:
    f.write(image_data)