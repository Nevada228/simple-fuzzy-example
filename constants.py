from enum import Enum

REQUIREMENTS = ['Java', 'Python', 'SQL', 'MSOffice']


class FuzzyQualityEnum(Enum):
    FAIR = [0, 0, 40, 45]
    GOOD = [40, 45, 60, 65]
    GREAT = [60, 65, 80, 85]
    EXCELLENT = [80, 85, 100, 100]


class ResponseEnum(Enum):
    YES = [60, 75, 100, 100]
    NO = [-25, 0, 50, 65]