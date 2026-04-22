# Board is 1000x1000 pixels
BOARD_SIZE = 1000

# Each edge has 11 cells (including corners)
CELLS_PER_EDGE = 11

# Size of each cell (approx)
CELL = BOARD_SIZE / CELLS_PER_EDGE


# List of all Monopoly properties in order
PROPERTIES = [
    "GO","Boardwalk","Luxury Tax","Park Place","Chance","Short Line",
    "Pennsylvania","Community Chest","North Carolina","Pacific",
    "Go To Jail",
    "Marvin Gardens","Water Works","Ventnor","Atlantic","B&O Railroad",
    "Illinois","Indiana","Chance","Kentucky",
    "Free Parking",
    "New York","Tennessee","Community Chest","St James","Penn Railroad",
    "Virginia","States","Electric Company","St Charles",
    "Jail",
    "Connecticut","Vermont","Chance","Oriental","Reading Railroad",
    "Income Tax","Baltic","Community Chest","Mediterranean"
]


# Convert (x,y) position → board property
def get_property_from_position(x, y):

    # Bottom edge
    if y > BOARD_SIZE - CELL:
        index = int(x // CELL)

    # Right edge
    elif x > BOARD_SIZE - CELL:
        index = int((BOARD_SIZE - y) // CELL) + 10

    # Top edge
    elif y < CELL:
        index = int((BOARD_SIZE - x) // CELL) + 20

    # Left edge
    elif x < CELL:
        index = int(y // CELL) + 30

    else:
        return None

    return PROPERTIES[index]

def get_cell_from_position(x, y):

    # LEFT column (GO = 0 → moving UP)
    if x < CELL:
        index = int((BOARD_SIZE - y) // CELL)

    # TOP row (10 → 19 moving RIGHT)
    elif y < CELL:
        index = int(x // CELL) + 10

    # RIGHT column (20 → 29 moving DOWN)
    elif x > BOARD_SIZE - CELL:
        index = int(y // CELL) + 20

    # BOTTOM row (30 → 39 moving LEFT back to GO)
    elif y > BOARD_SIZE - CELL:
        index = int((BOARD_SIZE - x) // CELL) + 30

    else:
        return None

    return index % 40
