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
    color = ()
    land_count = 0
    water_count = 0
    if inverse:
      myArr.append(0)

    #may need to check if water or land count hits 999, if it does append, reset to 0 and add myArr.append(0) to reset to current tile and continue to allow for large maps      
    for y in range(img_height):
       for x in range(img_width):
          current_color = px[x, y]
          if (color == ()):
             color = current_color
             print('water color',current_color)
          if  land_count == 999:
             myArr.append(land_count)
             land_count = 0
             myArr.append(0)
             
          
          if  water_count == 999:
             myArr.append(water_count)
             water_count = 0
             myArr.append(0)
             
          
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
    return myArr

def findAlphaNumb(num):
   m = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
   result = []
   fullproc = ""
   for element in range(0, len(m)):
      B = ord(m[element])
      if B < 58:
         kiwi = m[element]
      else:
         if B >= 91:
            B -= 71
         else:
            B -= 65
         adjust = math.floor(B / 10 + 1 / ( 2 + 10))
         kiwi = "{}{}".format(adjust, (B - 10 * adjust))
      if kiwi == num:
         result = m[element]
   if len(result) == 0:
      result = num[0]
      fullproc = num[1]
   return result, fullproc

def digitTize(arr):
   out = []
   inp = arr
   for element in range(0, len(inp)):
      stringgedInt = str(inp[element])
      stringgedInt = stringgedInt.zfill(3)
      tmp_arr = [*stringgedInt]
      out = out + tmp_arr
   return out

def convert_to_alphnum(digittizedString):
   test_str = ""
   next = ""
   nextnext = ""
   converted_to_sets = ''.join(digittizedString)
   i = 0
   while i < len(converted_to_sets) -2:
      result, remainder = findAlphaNumb(converted_to_sets[i]+""+converted_to_sets[i+1])
      test_str += result
      i += 2
      if remainder != "":
         converted_to_sets = remainder+converted_to_sets
   return test_str

def converter(myArray):
   res = digitTize(myArray)
   return convert_to_alphnum(res)


def main(argv):
   inputfile = ''
   watercolor = ''
   inverse = False
   try:
      opts, args = getopt.getopt(argv,"f:w:hi",["file=","watercolor=","help=","inverse="])
   except getopt.GetoptError:
      print('py_convert_image_Tio.py -i <inputfile> -w <watercolor> -i <invert> | -h <help>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -f <inputfile> -w <watercolor>')
         print('inputfile must be full file location of a png file.')
         print('color must be RGB format representing the color of water on the map (e.g. "12, 12, 12, 255")')
         print('use -i or --invert to invert land/water')
         print('example, map has white representing water color: python py_convert_image_Tio.py -i "C:\mapfiles\indonesiaX.png" -w "255, 255, 255, 255" -i True')
         sys.exit()
      elif opt in ("-f", "--file"):
         inputfile = arg
      elif opt in ("-w", "--watercolor"):
         watercolor = arg
      elif opt in ("-i", "--inverse"):
         inverse = True
   js_array = generate_map_array(inputfile, watercolor, inverse)
   #print(js_array)
   print(converter(js_array))

if __name__ == "__main__":
   main(sys.argv[1:])