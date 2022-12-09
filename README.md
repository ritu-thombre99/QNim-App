# QNim-App
QNim game is a quantum version of classical Nim game. In QNim game, human/classical computer will play against quantum computer. Developed using pygame in python

This project is implemented under the guidance of James Weaver as part of QAMP (Qiskit Advocate Mentorship Program) Fall-22. Project description can be found [here](https://github.com/qiskit-advocate/qamp-fall-22/issues/29).

To see the strategy quantum computer uses to play against classical player (human/computer), see [QNim Checkpoint-1](https://github.com/ritu-thombre99/QNim/blob/main/QAMP%20Checkopint%201.ipynb)

# Steps to install QNim on you system
+ Download QNim-App repository
+ Open Anaconda terminal and ```cd``` to the location where QNim-App is downloaded
+ Type ```pip install -r requirements.txt``` to install required packages
+ To open game window, type ```python main.py```

# How to play QNim game
+ Select amount of bulbs you want in each of the four rows on the light board and who should play first on the configuration page and hit start.
+ You can switch off minimum of 1 bulb and maximum of as many bulbs as you can from any one of the row. 
+ You cannot switch off bulbs from multiple row at the same time.
+ Bulbs which you can flip during your turn will turn green.
+ When you are done with your turn, hit the quantum computer button for QC to play.
+ Player switching off the last bulb will lose

# QNim API
Rest API developed using Flask in python which takes in the board state and returns the QC move. To start API locally on http://127.0.0.1:5000/, use python qnim_api.py in [qnim_api folder](https://github.com/ritu-thombre99/QNim-App/tree/main/qnim_api).

Mathematical framwork:
![alt text](https://github.com/ritu-thombre99/QNim-App/blob/main/screenshots/mathematical%20framework.png)

Experiment result:
![alt text](https://github.com/ritu-thombre99/QNim-App/blob/main/screenshots/final_with_label.png)

# [Gameplay video link](https://youtu.be/vqE8HICiBqA)
# Screenshots
Home page:
![alt text](https://github.com/ritu-thombre99/QNim-App/blob/main/screenshots/home.png?raw=true)

Home page with current saved game:
![alt text](https://github.com/ritu-thombre99/QNim-App/blob/main/screenshots/home_with_continue.png?raw=true)

Configuration page
![alt text](https://github.com/ritu-thombre99/QNim-App/blob/main/screenshots/config.png?raw=true)

Player turn
![alt text](https://github.com/ritu-thombre99/QNim-App/blob/main/screenshots/game_player_turn.png?raw=true)

QC turn
![alt text](https://github.com/ritu-thombre99/QNim-App/blob/main/screenshots/game_qc_turn.png?raw=true)

Player won
![alt text](https://github.com/ritu-thombre99/QNim-App/blob/main/screenshots/game_won.png?raw=true)

QC won
![alt text](https://github.com/ritu-thombre99/QNim-App/blob/main/screenshots/game_lost.png?raw=true)

# Happy playing :)
