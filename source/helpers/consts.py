
class Consts:
    SCREEN_TITLE = "Magic of Roz"

    SPRITE_IMAGE_SIZE = 128
    SPRITE_SCALING_PLAYER = 0.5
    SPRITE_SCALING_TILES = 0.5
    MAP_SCALING = 0.5

    SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * MAP_SCALING)

    SCREEN_GRID_WIDTH = 25
    SCREEN_GRID_HEIGHT = 15

    SCREEN_WIDTH = (SPRITE_SIZE * SCREEN_GRID_WIDTH) // 2
    SCREEN_HEIGHT = (SPRITE_SIZE * SCREEN_GRID_HEIGHT) // 2

    RIGHT_FACING = 0
    LEFT_FACING = 1

    PLAYER_START_X = 2
    PLAYER_START_Y = 10

    PLAYER_MOVEMENT_SPEED = 5

    PLAYER_ATTACK_SPEED = 15
    PLAYER_ATTACK_PARTICLE_SPEED = 12

    MAX_ENEMY_HEALTH = 100
    
    NORMAL_ATTACK_MANA_COST = 3
    SPECIAL_ATTACK_MANA_COST = 12
