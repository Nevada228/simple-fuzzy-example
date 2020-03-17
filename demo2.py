import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import skfuzzy as fuzz
from openpyxl import load_workbook
from skfuzzy import control as ctrl

plt.ioff()


class WorkClass(object):
    def __init__(self, class_name, rank_name, attributes):
        """Constructor"""
        self.class_name = class_name
        self.rank_name = rank_name
        self.attributes = attributes


class Employees(object):
    def __init__(self, name, class_n_rank_name, results):
        """Constructor"""
        self.name = name
        self.class_n_rank_name = class_n_rank_name
        self.results = results


def classifier(rqrmnts, data, rule, class_n_rank):
    # на вход подается строка с требованиями, строка с числовыми соответствиями, правило и должность+роль, для которой происходит проверка
    response_ctrl = ctrl.ControlSystem([rule])
    make_resp = ctrl.ControlSystemSimulation(response_ctrl)
    for x in rqrmnts:
        make_resp.input[rqrmnts] = float(data)
    make_resp.compute()
    if make_resp.output['response'] != 0:
        return class_n_rank


df = pd.read_excel('employees.xlsx')
df = df.rename(columns={'Unnamed: 0': 'FIO'})

emps = []
for idx, row in df.iterrows():
    emps.append(Employees(row.values[0],'class_n_rank_name', row.values[1:]))


df_req = pd.read_excel('requirements.xlsx')
df = df.rename(columns={'Unnamed: 0': 'POSITION'})