class Solution:
    def equationsPossible(self, equations):
        params_set_arr = []
        for equation in equations:
            params_0 = equation[0]
            params_1 = equation[3]
            params_op = equation[1]

            is_equal = params_op == '='

            for ps in params_set_arr:
                if params_0 is None and params_1 is None:
                    break
                if params_0 and params_0 in ps:
                    if is_equal:
                        ps.add(params_1)
                        params_0 = None
                    params_0 = None
                    
                if params_1 and params_1 in ps:
                    if is_equal:
                        ps.add(params_0)
                        params_0 = None
                    params_1 = None


