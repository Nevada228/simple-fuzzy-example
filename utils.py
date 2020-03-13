from skfuzzy import control as ctrl
from constants import *


class RuleBuilder:
    @staticmethod
    def build_rule(antecedents, consequent, response: ResponseEnum, req_quality: list):
        if len(req_quality) != len(REQUIREMENTS):
            raise Exception("Ээээ!")
        rule_body = None
        try:
            for ant, quality in zip(antecedents, req_quality):
                if rule_body is None:
                    rule_body = ant[quality.name]
                else:
                    rule_body = rule_body & ant[quality.name]
        except Exception:
            print('Это что ещё такое?')
        return ctrl.Rule(rule_body, consequent[response.name])
