<i>This project has been created as part of the 42 curriculum by ivgomez- and nacarvac</i>
# A-maze-ing

## Description
- This project creates and displays a maze based on the parameterso of the file specified in command line when executing.

### Proyect structure:

```text
.
├── a_maze_ing.py
├── __init__.py
├── Makefile
├── pyproject.toml
├── README.md
├── requirements.txt
└── test_input.txt

```

## Instructions
The program can be executed in two ways:

By using the makefile:
```ini
make run FILENAME=config.txt
```

By executing the program directly from the src/ directory:
```ini
cd src
python3.10 a_maze_ing.py config.txt 
```

## <b>Config file structure:</b> <i><small>config.txt</small></i>

```ini
WIDTH=<int>
HEIGHT=<int>
ENTRY=<int>, <int>
EXIT=<int>, <int>
OUTPUT_FILE=<string>
PERFECT=<boolean>
#optional
SEED=<int>
```

## Algoritm choice:
The maze of this project is generated via the <b>back tracking</b> maze generation algorithm,
this algorithm was chosen bacause we thought it was the best for generationg <b>PERFECT</b> mazes

## Code reusability:
Everything except the main method from our program can be reusable.

## Team projet management
- The roles of each team member: <br>
    *ivgomez-* was responsible for the maze generation algorithm (perfect and imperfect), parameters, and their control. <br>
    *ncaravac* was responsible for the visuals, menu, path algorithm, and minor adjustments.
    <br>
- Your anticipated planning and how it evolved until the end: <br>
    We divided the task according to each person's level, and we both did our part without conflict. <br>
- What worked well and what could be improved <br>
    All worked fine.
- Have you used any specific tools? Which ones?
    GitHub.

## Resources
- w3schools
- YouTube