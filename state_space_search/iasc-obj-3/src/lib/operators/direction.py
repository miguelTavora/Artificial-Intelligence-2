from enum import Enum

class Direction(Enum):

    DOWN       = (0, 1)
    BACK       = (-1, 0)
    TOP        = (0, -1)
    FRONT      = (1, 0)
    TOP_FRONT  = (1, -1)
    TOP_BACK   = (-1, -1)
    DOWN_FRONT = (1 ,1)
    DOWN_BACK  = (-1 ,1)

    
    
     

    