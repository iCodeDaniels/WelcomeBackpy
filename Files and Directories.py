# THIS IS TO CALL OUT A PATH IN THE DIRECTORY
# from pathlib import Path

# path = Path("Module.py")
# print(path.exists())


# THE MKDIR WHICH MEANS : TO MAKE DIRECTORY
# from pathlib import Path

# path = Path("Ecommerce")
# print(path.exists())


# from pathlib import Path
#
# path = Path("Ecommerce")
# print(path.mkdir())

# THE GLOB METHOD IS USED TO SEARCH FOR FILES THAT ARE ALREADY IN THE DIRECTORY

from pathlib import Path

path = Path()
for file in path.glob('*.py '):
    print(file)