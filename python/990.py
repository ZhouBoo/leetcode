class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        params_set_arr = []
        for equation in equations:
            params_0 = equation[0]
            params_1 = equation[3]
