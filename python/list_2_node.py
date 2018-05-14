# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def __str__(self):
    #     return "%d" % self.val

    # def __repr__(self):
    #     return "%d" % self.val

def list_2_node(l):
    read_count = 0
    line_count = 1
    length = len(l)
    # print(length)
    last_nodes = []
    root_node = None
    while read_count < length:
        tmp_nodes = [TreeNode(x) if x != None else None for x in l[read_count:read_count+line_count]]

        # print(tmp_nodes)
        if len(last_nodes) == 0:
            root_node = tmp_nodes[0]
        else:
            # for node in last_nodes:
            for i in range(0, len(last_nodes)):
                if last_nodes[i] == None:
                    continue
                if len(tmp_nodes) > i * 2:
                    last_nodes[i].left = tmp_nodes[i * 2]
                if len(tmp_nodes) > i * 2 + 1:
                    last_nodes[i].right = tmp_nodes[(i * 2) + 1]

        last_nodes = tmp_nodes

        read_count += line_count
        line_count *= 2
    # print(root_node)
    return root_node

# print(list_2_node([37,-34,-48,None,-100,-100,48,None,None,None,None,-54,None,-71,-22,None,None,None,8]))

# lists = [37,-34,-48,None,-100,-100,48,None,None,None,None,-54,None,-71,-22,None,None,None,8]
# print(list_2_node(lists))