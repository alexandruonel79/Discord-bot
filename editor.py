from PIL import Image,ImageFilter,ImageEnhance  
#Read image
im = Image.open('input.jpg')
   
def imageEditor(message):
        print(message)
        if len(message) != 11: 
                requirements = [message.split(' ')[1], message.split(' ')[2]]
                if requirements[0] == 'contrast':
                        enh = ImageEnhance.Contrast(im)  
                        return enh.enhance(1 + float(requirements[1]))
                if requirements[0] == 'color':
                        enh = ImageEnhance.Color(im)
                        return enh.enhance(1 + float(requirements[1]))
                if requirements[0] == 'brightness':
                        enh = ImageEnhance.Brightness(im)
                        return enh.enhance(1 + float(requirements[1]))
                if requirements[0] == 'sharpness':
                        enh = ImageEnhance.Color(im)
                        return enh.enhance(1 + float(requirements[1]))