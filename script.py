from email.mime import image
from importlib.resources import path
from re import ASCII
from turtle import heading, width
import PIL.Image

#asciiii 
ASCII_CHARS = ["@" , "#" , "S", "%", "?" , "*", "+", ";", ":", "," , "."]

#resize
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int (new_width * ratio)
    resize_image = image.resize((new_width , new_height))
    return (resize_image)

#grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

# pixels to ASCII
def pixels_to_ascii(image): 
   pixels = image.getdata()
   characters = "".join([ASCII_CHARS[pixel //25]for pixel in pixels]) 
   return (characters)

def main(new_width= 100):
    path = input("enter a valis pathname to an image :\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid pathname to an image.")

    new_iamge_data = pixels_to_ascii(grayify(resize_image(image))) 

    pixel_count = len(new_iamge_data)
    ascii_image = "\n".join(new_iamge_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print (ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()