import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

from utils import *

plt.ioff()

ran_resp = np.arange(-25, 126, 1)

# New Antecedent/Consequent objects hold universe variables and membership
# functions

antecedents = []

for req in REQUIREMENTS:
    antecedents.append(ctrl.Antecedent(np.arange(0, 121, 1), req))

for ant in antecedents:
    for q in FuzzyQualityEnum:
        ant[q.name] = fuzz.trapmf(ant.universe, q.value)

response = ctrl.Consequent(np.arange(-25, 126, 1), 'response')

response[ResponseEnum.NO.name] = fuzz.trapmf(response.universe, ResponseEnum.NO.value)
response[ResponseEnum.YES.name] = fuzz.trapmf(response.universe, ResponseEnum.YES.value)

# You can see how these look with .view()
response.view()
antecedents[0].view()

rule_req_quality = [FuzzyQualityEnum.NICE,
                    FuzzyQualityEnum.EXCELLENT,
                    FuzzyQualityEnum.GREAT,
                    FuzzyQualityEnum.NICE]

rule3 = RuleBuilder.build_rule(antecedents, response, ResponseEnum.YES, rule_req_quality)

rule3.view()

response_ctrl = ctrl.ControlSystem([rule3])
mamd = ctrl.ControlSystem([rule3])
make_resp = ctrl.ControlSystemSimulation(response_ctrl)

# Входные данные
make_resp.input[REQUIREMENTS[0]] = 43.18
make_resp.input[REQUIREMENTS[1]] = 91.54
make_resp.input[REQUIREMENTS[2]] = 73.48
make_resp.input[REQUIREMENTS[3]] = 50

# Crunch the numbers
make_resp.compute()
print('Response: ')
print(make_resp.output['response'])
response.view(sim=make_resp)

plt.show()
