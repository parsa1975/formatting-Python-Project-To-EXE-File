import os
address = input("Address:")
def code(address):
  return "pyinstaller --onefile %s" % address
os.system(code(address))
