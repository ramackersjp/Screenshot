# Screenshot
 Simple PYscript with GUI to take a screenshot.

 ![Banner](header_screenshot.png)

 ## Requierments
- import numpy as np
- import cv2
- import pyautogui

## Pre-install:

```
git clone https://github.com/ramackersjp/Screenshot/station.git
cd Screenshot
./Take-Screenshot.sh
```
chmod +x app.py (in the src root)

## Run
1. Place the Take-Screenshot.desktop file on your desktop.
2. Go to your IDE en change the .desktop file to your own path. 
3. Take screenshots

```
python ./app.py
```
Quicklaunch (Single command): 

```
bash <(curl -L raw.githubusercontent.com/ramackersjp/Screenshot/main/src/app.py)
```

## Image save location:
The place where you can find your screenshot.
```
images are saved at the src map. Or select your own location.
```
## Contribute:
If you want to contribute to this project, please create a branch from the beta version and pull it there. When the beta branch is fully where we want we merging the beta branch to the main branch.
