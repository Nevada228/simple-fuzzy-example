import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

plt.ioff()

ran_resp = np.arange(-25, 126, 1)

# New Antecedent/Consequent objects hold universe variables and membership
# functions
rqrmnts = ['Java','Python','SQL','MSOffice']
antcdnt = [0,0,0,0]
k=0
for i in rqrmnts:
    antcdnt[k] = ctrl.Antecedent(np.arange(0, 121, 1), rqrmnts[k])
    k=k+1


k = 0
for i in antcdnt:
    antcdnt[k]['bad'] = fuzz.trapmf(antcdnt[k].universe, [0, 0, 40, 45])
    antcdnt[k]['nice'] = fuzz.trapmf(antcdnt[k].universe, [40, 45, 60, 65])
    antcdnt[k]['great'] = fuzz.trapmf(antcdnt[k].universe, [60, 65, 80, 85])
    antcdnt[k]['exclnt'] = fuzz.trapmf(antcdnt[k].universe, [80, 85, 100, 100])
    k = k+1

response = ctrl.Consequent(np.arange(-25, 126, 1), 'response')

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
response['YES'] = fuzz.trapmf(response.universe, [60, 75, 100, 100])
response['NO'] = fuzz.trapmf(response.universe, [-25, 0, 50, 65])


# You can see how these look with .view()
response.view()
antcdnt[0].view()


rule3 = ctrl.Rule(antcdnt[0]['nice'] & antcdnt[1]['exclnt'] & antcdnt[2]['great'] & antcdnt[3]['nice'], response['YES'])


rule3.view()


response_ctrl = ctrl.ControlSystem([rule3])
mamd = ctrl.ControlSystem([rule3])
make_resp = ctrl.ControlSystemSimulation(response_ctrl)

# Входные данные
make_resp.input[rqrmnts[0]] = 43.18
make_resp.input[rqrmnts[1]] = 91.54
make_resp.input[rqrmnts[2]] = 73.48
make_resp.input[rqrmnts[3]] = 50

# Crunch the numbers
make_resp.compute()
print('Response: ')
print(make_resp.output['response'])
response.view(sim=make_resp)

plt.show()

