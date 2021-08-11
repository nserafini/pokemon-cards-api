from enum import Enum


class CardExpansion(Enum):

    BASE_SET = "Base Set"
    JUNGLE = "Jungle"
    FOSSIL = "Fossil"
    BASE_SET_2 = "Base Set 2"


class CardType(Enum):

    WATER = "Water"
    FIRE = "Fire"
    GRASS = "Grass"
    ELECTRIC = "Electric"


class CardRarity(Enum):

    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
