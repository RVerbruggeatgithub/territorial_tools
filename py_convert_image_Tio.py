from PIL import Image
import sys, getopt
import math

def generate_map_array(filename, watercolor, inverse):
    im = Image.open(r""+filename)
    watercolor = tuple(map(int, watercolor.split(', ')))
    img_width = im.size[0]
    img_height = im.size[1]
    px = im.load()
    myArr = []

    if img_width > 999:
       myArr.append(math.floor(img_width / 1000))
    else:
       myArr.append(0)

    myArr.append(img_width % 1000)

    if img_height > 999:
       myArr.append(math.floor(img_height / 1000))
    else:
       myArr.append(0)

    myArr.append(img_height % 1000)

    # top 1px margin
    # myArr.append(img_width % 1000 + 2)

    # Toggle land/water init, comment out next line.
    # myArr.append(0)
    color = ()
    land_count = 0
    water_count = 0

    for y in range(img_height):
       for x in range(img_width):
          if inverse == True:
             myArr.append(0)
             inverse = False
          current_color = px[x, y]
          if (color == ()):
             color = current_color
             print('water color',current_color)
          if (current_color == watercolor):
             if land_count > 0:
                myArr.append(land_count)
                land_count = 0
             water_count += 1
             if (x == img_width + 1):
                water_count += 1
          else:
             if water_count > 0:
                myArr.append(water_count)
                water_count = 0
             land_count += 1
             if (x == img_width + 1):
                land_count += 1

    if land_count > 0:
       myArr.append(land_count)
    if water_count > 0:
       myArr.append(water_count)
    myArr.append(img_width % 1000 + 2)
    print(myArr)


def main(argv):
   inputfile = ''
   watercolor = ''
   invert = False
   try:
      opts, args = getopt.getopt(argv,"f:w:i:h",["file=","watercolor=","invert=","help="])
   except getopt.GetoptError:
      print('py_convert_image_Tio.py -i <inputfile> -w <watercolor> -i <invert> | -h <help>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -f <inputfile> -w <watercolor>')
         print('inputfile must be full file location of a png file.')
         print('color must be RGB format representing the color of water on the map (e.g. "12, 12, 12, 255")')
         print('use -i or --invert to invert land/water True|False')
         print('example, map has white representing water color: python py_convert_image_Tio.py -i "C:\mapfiles\indonesiaX.png" -w "255, 255, 255, 255" -i True')
         sys.exit()
      elif opt in ("-f", "--file"):
         inputfile = arg
      elif opt in ("-w", "--watercolor"):
         watercolor = arg
      elif opt in ("-i", "--invert"):
         inverse = arg
   generate_map_array(inputfile, watercolor, inverse)

if __name__ == "__main__":
   main(sys.argv[1:])