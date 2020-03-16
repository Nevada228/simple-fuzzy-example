from constants import FuzzyQualityEnum
from typing import List


class Requirement:
    def __init__(self, subject, value: FuzzyQualityEnum):
        self.subject = subject
        self.value = value


class Position:
    def __init__(self, name, requirements: List[Requirement]):
        self.name = name
        self.requirements = requirements


sysadmin = Position("Сисадмин", [
    Requirement('Python', FuzzyQualityEnum.NICE),
    Requirement('Docker', FuzzyQualityEnum.EXCELLENT),
    Requirement('SQL', FuzzyQualityEnum.BAD),
])

proger = Position("Прогер", [
    Requirement('Java', FuzzyQualityEnum['EXCELLENT']),
    Requirement('Python', FuzzyQualityEnum['EXCELLENT']),
    Requirement('SQL', FuzzyQualityEnum['NICE']),
])

positions = [sysadmin, proger]

for pos in positions:
    print(f'\nПозиция: {pos.name}')

    for req in pos.requirements:
        print(f'Предмет: {req.subject}, Требуемое значение: {req.value.name}')


def build_from_excel() -> List[Position]:
    requirements = []
    #  TODO

    return requirements
