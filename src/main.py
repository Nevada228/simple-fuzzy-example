import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from src.utils import DataLoader, Requirement, WorkClass

"""
a= b= c= d= e= f= g= h= j= l= m= n= o= p= q = 0
print("Введите границы лингвистического терма bad:\n")
a = input()
b = input()
c = input()
print("Введите границы лингвистического терма fair:")
d = input()
e = input()
f = input()
print("Введите границы лингвистического терма good:")
g = input()
h = input()
j = input()
print("Введите границы лингвистического терма great:")
l = input()
m = input()
n = input()
print("Введите границы лингвистического терма excellent:")
o = input()
p = input()
q = input()
"""


def rule_maker(work_class: WorkClass):

    antecedents = []
    for req in work_class.requirements:
        antecedents.append(ctrl.Antecedent(np.arange(0, 100, 1), req.subject))

    for item in antecedents:
        # print('Введите границы лингвистического терма bad:')
        # input(a, b, c, d)
        item['bad'] = fuzz.trimf(item.universe, [0, 15, 30])
        # print("Введите границы лингвистического терма bad:")
        # input(float(a), float(b), float(c))
        item['fair'] = fuzz.trimf(item.universe, [20, 35, 50])
        item['good'] = fuzz.trimf(item.universe, [40, 55, 70])
        item['great'] = fuzz.trimf(item.universe, [60, 75, 90])
        item['excellent'] = fuzz.trimf(item.universe, [80, 95, 100])

    response = ctrl.Consequent(np.arange(0, 120, 1), 'response')
    response[work_class.position] = fuzz.trimf(response.universe, [60, 75, 100])
    response.view()
    antecedents[0].view()

    rule_body = None
    for ant, req in zip(antecedents, work_class.requirements):
        if rule_body is None:
            rule_body = ant[req.value]
        else:
            rule_body = rule_body & ant[req.value]

    rule = ctrl.Rule(rule_body, response[work_class.position])
    rule.view()
    return rule


def classifier(requirements, data, rule, position):
    rqrmnts = [req.subject for req in requirements]

    # на вход подается строка с требованиями, строка с числовыми соответствиями, правило и должность+роль, для которой происходит проверка
    response_ctrl = ctrl.ControlSystem([rule])
    response_ctrl.view()
    make_resp = ctrl.ControlSystemSimulation(response_ctrl)

    k = 0
    for i in range(8):
        #print(data.results[i])
        make_resp.input[rqrmnts[i]] = data.results[i]
        k += 1
    make_resp.compute()
    if make_resp.output['response'] != 0:
        return position
    else:
        return "None"

# основная часть
plt.ioff()

employers = DataLoader.load_personal_data('../employees.xlsx')
attributes = DataLoader.load_requirements_data('../requirements.xlsx') # массив требований

for att in attributes:
    print(f'\n Позиция: {att.position}')
    for req in att.requirements:
        print(req.subject, req.value)

for emp in employers:
    for attr in attributes:
        rule = rule_maker(attr)
        emp.position = classifier(attr.requirements, emp, rule, attr.position)

for x in employers:
    print(x.position)

plt.show()