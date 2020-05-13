#!/usr/bin/env python
"""Generate oreo cursors, just changing colours"""

import shutil
import os

colors = {
    "frost_1": "#8FBCBB",
    "frost_2": "#88C0D0",
    "frost_3": "#81A1C1",
    "frost_4": "#5E81AC",
    "nord_red": "#BF616A",
    "nord_orange": "#D08770",
    "nord_yellow": "#EBCB8B",
    "nord_green": "#A3BE8C",
    "nord_purple": "#B48EAD",
}

BASE_DIR = "oreo_base"
for (color, hex_val) in colors.items():
    COLOR_DIR = "src/oreo_" + color + "_cursors"

    # remove previous builds
    try:
        shutil.rmtree(COLOR_DIR)
    except FileNotFoundError:
        pass
    os.mkdir(COLOR_DIR)

    for file in os.listdir(BASE_DIR):
        orig_path = os.path.join(BASE_DIR, file)
        new_path = os.path.join(COLOR_DIR, file)

        # replace default color with new color
        with open(new_path, "w") as fout:
            with open(orig_path) as fin:
                for line in fin:
                    fout.write(line.replace("#4e81ed", hex_val))

        # update cursor title
        with open(os.path.join(COLOR_DIR, "index.theme"), "w") as f:
            NAME = " ".join([x.capitalize() for x in color.replace("_", " ").split()])
            f.write("[Icon Theme]\nName=Oreo " + NAME + " Cursors\nComment=design by varlesh")
