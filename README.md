# Collage Creator
## Collage Creator is a simple GUI application to input picture and its copies into a selected frame.
Arrangement of copies inside a frame may be selected manually or be optimized by the programme to fit maximum quantity of pictures into the frame.<br>
Functionality of segment cutting out allows to crop desired picture from the collection to put it into the frame.<br>
Application has basic input validation functionality and informs user about invalid data input and infeasibility of images arrangement in a frame.

## Structure
- CollageCreator.py - main file with GUI app
- Functions.py - file containing functions used to crop and paste images and optimize arrangement in a frame
- Functions_tests.py - pytest test fucntions of the file above
- Automate_crop.pt - quick script to crop and save example images from collections
- Qt_designer_windows - Qt5 files with applied windows
- Pictures - example images and collections

## Requirements & Libraries
- python 3.11+
- PyQt5, Qt Designer
- cv2
- numpy, pandas
- pathlib
- pytest

## How to use
Clone the repo:<br>
git clone https://github.com/michal2124/Collage-Creator.git<br>
Run CollageCreator.py

## Screenshots
<img width="314" height="244" alt="Screenshot_main" src="https://github.com/user-attachments/assets/19a37401-e611-4c2f-9ced-44779fbe7ed8" />

<img width="318" height="246" alt="Screenshot_manual" src="https://github.com/user-attachments/assets/421c7a83-4604-4fdd-9fa1-6d5d1342f051" />

<img width="316" height="244" alt="Screenshot_cutout" src="https://github.com/user-attachments/assets/7c5a93dc-accd-4708-88c2-b83d26aed7ba" />

## Possible images arrangements in a frame
<img width="1481" height="842" alt="arrangement" src="https://github.com/user-attachments/assets/0d70f97e-01be-482b-9374-813887ea1d4b" />


## Status
The application is a learning project, not production-ready tool.<br>
The project is experimental and focused on understanding the basics of OOP and GUI apps.

## License
This repository is licensed under the MIT License
