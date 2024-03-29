# Pathfinding

Made using Pygame library in Python to create an intuitive pathfinding algorithm visualisation.

Click where the start node and end node is. Draw the obstacles and create your own map.

**Keybinds** 

- Right Click to erase tile colour
- 'a' to start finding the shortest route using A* algorithm
- 'd' to start finding the shortest route using Dijkstra's algorithm
- 'c' to clear the board

**Colours** 
- Blue indicates points which the algorithm has searched
- Red indicates points that are in a queue to be searched next by the algorithm
- Green indicates the shortest path
- Orange indicates starting position
- Purple indicates ending point
- Black indicates a wall or obstruction that the algorithm will go around

### To do 
- [x] Add A* algorithm
- [x] Add Dijkstra's algorithm
- [ ] Create menu to show controls and available algorithms

### Installation
In the Pathfinding directory follow these commands to install:
    
    pip3 -r requirements.txt
    pip3 install -e .

### Screenshots
<img src="https://github.com/ADoor22/pathfinding/assets/101601277/aa83dbf4-718b-456f-89b0-eba74e846b25.gif" width="600" height="600" />
<img src="https://github.com/ADoor22/pathfinding/assets/101601277/a5381443-a9d8-4441-b171-2800f916fdfd.gif" width="600" height="600" />
<img width="802" alt="image" src="https://github.com/ADoor22/pathfinding/assets/101601277/a59d91f9-e8c5-4db9-a7d8-73e4d621b22c">
