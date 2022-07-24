import sys
import os
from pathlib import Path
from PIL import Image

# getting args using sys
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# path of new folder if exists

p = Path(sys.argv[2])


if not p.exists():
    os.makedirs(output_folder)

# loop through Pokedex and convert

direct = image_folder
pathlist = Path(direct).glob('*')
for path in pathlist:
    img = Image.open(f'{path}')
    print(path.stem)
    # clean_name = os.path.splittext(path.name)[0] if using os
    img.save(f'{output_folder}{path.stem}.png', 'png')
    print("all done!")
