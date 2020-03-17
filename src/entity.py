from typing import List


class Requirement:
    def __init__(self, subject: str, value: str):
        self.subject = subject
        self.value = value


class WorkClass:
    def __init__(self, position, requirements: List[Requirement]):
        self.position = position
        self.requirements = requirements


class Employee:
    def __init__(self, name, position, results):
        """Constructor"""
        self.name = name
        self.position = position
        self.results = results
