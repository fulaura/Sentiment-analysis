import os
from PIL import image 

output_dir = ''
source_dit = ''

for file in os.listdir(source_dit):
    if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
        image = image.open(os.path.join(source_dit,file))
        image_converted = image.convert('RGB')
        image_converted.save(os.path.join(output_dir, '{0}.pdf'.format(file.split('.')[-2])))