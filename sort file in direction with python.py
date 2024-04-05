import os , shutil

path = os.path.dirname(os.path.realpath(__file__))

for file in os.listdir(path):
    if file.endswith((".jpg")):
      if not os.path.exists("images"):
          os.mkdir("images")
          shutil.copy(file,'images')
          os.remove(file)
      else:
          shutil.copy(file,'images')
          os.remove(file)

print("Done!")
