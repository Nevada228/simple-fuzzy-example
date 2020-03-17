import pandas as pd
from src.entity import *  # поменять потом


class DataLoader:
    @staticmethod
    def load_personal_data(file_path: str) -> List[Employee]:
        df = pd.read_excel(file_path).rename(columns={'Unnamed: 0': 'FIO'})
        employers = []
        for idx, row in df.iterrows():
            employers.append(
                Employee(
                    row.values[0],
                    'position',
                    row.values[1:].astype(float))
            )
        return employers

    @staticmethod
    def load_requirements_data(file_path: str) -> List[WorkClass]:
        df = pd.read_excel(file_path).rename(columns={'Unnamed: 0': 'POSITION'})
        requirements = []
        for idx, row in df.iterrows():
            requirements.append(
                WorkClass(row.values[0],
                          [Requirement(col, value) for col, value in zip(df.columns.values[1:],
                                                                         row.values[1:])]))
        return requirements
