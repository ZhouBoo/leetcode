# 给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，
# 并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
# 只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

# 示例

# 输入：["a==b","b!=a"]
# 输出：false
# 解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。

from array import array

class Solution:

    def __init__(self):
        self.equation_dict = {}
        self.equation_tree = {}

    def union(self, eq1, eq2):
        eq1_f = self.find(eq1)
        eq2_f = self.find(eq2)
        if eq1_f == eq1 and eq2 == eq2_f and \
            self.equation_tree.get(eq1_f) == None \
                and self.equation_tree.get(eq2_f) == None:
            # 俩货都不存在
            self.equation_tree[eq1] = [eq1, eq2]
            self.equation_dict[eq2] = eq1
            self.equation_dict[eq1] = eq1
        else:
            # 俩货只要有存在于，需要合并
            if self.equation_tree.get(eq2_f) and self.equation_tree.get(eq1_f):
                if eq1_f == eq2_f:
                    return
                # print('remove %s origin %s, %s - %s' % (eq2_f, eq1_f, eq1, eq2))
                union_array = self.equation_tree[eq2_f]
                for u in union_array:
                    self.equation_dict[u] = eq1_f
                union_array += self.equation_tree[eq1_f]
                self.equation_tree[eq1_f] = union_array
                self.equation_tree.pop(eq2_f)
            elif self.equation_tree.get(eq2_f):
                self.equation_tree[eq2_f].append(eq1)
                self.equation_dict[eq1] = eq2_f
            elif self.equation_tree.get(eq1_f):
                self.equation_tree[eq1_f].append(eq2)
                self.equation_dict[eq2] = eq1_f
        # print(self.equation_dict, self.equation_tree)

    def find(self, x):
        if self.equation_dict.get(x):
            return self.equation_dict[x]
        return x

    def equationsPossible(self, equations):
        not_equation_list = []
        for eq in equations:
            if eq[0] == eq[3]:
                if eq[1] == '=':
                    continue
                else:
                    return False
            if eq[0] not in self.equation_dict:
                self.equation_dict[eq[0]] = eq[0]
            if eq[3] not in self.equation_dict:
                self.equation_dict[eq[3]] = eq[3]
            if eq[1] == '=':
                self.union(eq[0], eq[3])
            else:
                not_equation_list.append(eq)

        for neq in not_equation_list:
            if self.find(neq[0]) == self.find(neq[3]):
                return False
        return True


print(Solution().equationsPossible(["a==b", "b!=a"]))
print(Solution().equationsPossible(["a==b", "b==a"]))
print(Solution().equationsPossible(["a==b", "b==c", "c!=d", "c!=e", "d==e"]))
print(Solution().equationsPossible(["a==b", "b==c", "c!=d", "c!=e", "d==e", "c==h", "h!=e"]))
print(Solution().equationsPossible(["a==b", "e==c", "b==c", "a!=e"]))
print(Solution().equationsPossible(["c==b", "b==b", "f==b", "e==e"]))
print(Solution().equationsPossible(["b==q","d!=v","g!=b","m==o","f!=h","h!=q","b!=r","c==h","c==h","e==q","q!=o","t==e","c!=p","w==k","r==x","y!=o","t==b","m!=n","n!=t","d==j","j!=b","w!=v","p!=m","b!=r","f!=n","m!=p","m!=p","q==e","e!=l","b==q"]))
print(Solution().equationsPossible(["n!=i","d==i","n==m","n==g","j==b","k!=c","h==v","d!=a","v!=c","y!=c","g!=p","q!=b","h!=i","v!=j","c==f","y!=d","t==i","i!=u","k!=t","s!=h","s!=u","s!=n","a!=s","y!=n","e!=p","c!=e","u!=a","e!=b","i!=k","v!=b","w!=p","b!=d","m!=u","m!=l","t!=j","m!=k","s!=i","t==i","i!=l","p!=l","a!=w","m!=p","i==t","t!=f","m!=t","y==y","n!=d","p!=s","p!=f","i!=n","t!=a","b!=o","g!=p","k!=p","v!=c","x!=t","s!=b","e!=l","w!=l","j!=x","j==j","g!=b","e!=q","p!=f","i!=o","j!=p","f!=e","v!=w","o==r","c!=e","i!=x","j!=l","v!=f","p!=u","u!=w","n!=b","v!=g","r!=d","k!=h","d!=y","p!=x","q!=h","f!=i","p!=y","n!=u","c!=x","s!=x","v==h","t!=r","k!=u","h!=y","j!=v","g!=x","f!=w","w!=h","c!=j","g!=x","u!=l","n!=r","g!=m"]))
print(Solution().equationsPossible(["c==p","h!=b","j!=f","w==y","b==u","y==t","c==e","k==g","a==u","i==k","t==n","k!=a","y==n","c!=n","s!=l","p!=y","i!=y","e!=t","l!=u","y==t","u!=m","k!=d","p!=w","j!=y","n!=u","e!=x","w!=l","u!=f","u!=d","g!=q","k!=p","b!=o","f!=h","u!=s","q!=s","b!=c","f!=j","k!=t","j!=r","y!=f","j!=n","o!=d","q!=t","p!=l","p!=u","u!=i","f!=x","u!=o","y!=c","l!=m","r!=t","i==k","o!=s","x!=i","p!=j","l!=r","o!=s","c!=q","p!=f","v==e","p!=h","c!=r","r!=w","o!=v","y==y","f!=k","p!=u","i!=x","c!=u","n!=a","t!=c","y!=r","u==b","q!=c","p!=t","g!=x","b!=y","j!=k","i!=r","j!=n","w!=m","a!=e","o!=h","t!=p","u==a","w!=u","d!=l","q!=n","n!=v","g!=f","p!=m","b!=h","c!=h","l!=g","n!=j","r!=g","h!=f","i!=f","g!=o","n==v"]))
print(Solution().equationsPossible(["s==v","h!=j","o==s","y==r","r==q","m!=p","b!=f","s==c","i==i","f==f","y!=e","c!=a","e!=f","a!=w","s==c","b!=d","g==u","g!=r","u==u","l==s","b!=i","v!=u","t==d","d!=s","j!=i","n!=v","y!=b","m!=j","d==k","j!=x","e!=k","g!=a","m!=q","h!=e","e!=y","a!=m","s!=g","n!=j","i!=q","c!=k","r!=c","r!=m","y!=g","g!=b","k!=e","a!=h","o!=j","a!=l","m!=b","b!=u","l!=k","r==r","v!=h","v!=w","y!=a","r!=k","e!=k","w!=h","h!=o","f!=o","k!=q","g!=e","c!=i","u!=c","k!=w","m!=d","d!=b","f!=e","f!=g","e!=m","f!=e","j!=l","b!=q","e!=i","p!=v","v!=p","w!=g","j!=i","c!=e","r==r","t!=r","w==w","o!=e","x!=o","h!=s","r!=k","f!=n","e==e","m!=f","u!=n","n!=b","x!=c","k!=l","s!=m","f!=j","m!=j","d!=u","o!=w","f!=n","a!=c","m!=d","j!=d","j!=h","x!=l","v!=r","m!=k","x!=b","l!=x","w!=i","l!=i","m!=k","e!=t","r==q","i!=e","e!=c","p!=d","s!=e","m!=h","v==o","g!=k","j!=f","p!=d","n!=x","b!=u","w!=b","y!=n","f!=p","j!=d","v!=p","e!=b","o!=m","m==m","k!=m","l!=y","j!=m","c!=r","t!=u","e!=r","i!=r","j!=e","e!=y","i!=c","t==d","s!=j","d!=q","t!=c","t!=o","a!=p","k!=q","p!=i","f!=s","w!=n","w!=k","e!=c","w!=s","g!=p","m!=o","t!=r","t!=q","i!=v","f!=x","x!=r","d!=u","r!=s","l==l","p!=t","n!=j","f!=b","d==t","t!=r","e!=i","l!=m","b!=v","m!=u","q!=w","n!=p","l==v","b!=w","c!=q","c!=i","u!=d","v!=a","k!=f","o!=e","d!=i","i!=r","g!=k","a!=u","p!=d","m!=r","f!=b","e!=a","t!=o","n!=f","y==r","b!=v","v!=t","q==q","x==x","f!=p","l==v","k!=j","b!=f","a!=w","m!=r","p==p","l!=b","n!=v","s!=t","j!=q","d!=c","j!=g","i!=d","d!=x","q!=x","r!=x","n!=q","p!=n","o!=d","k!=j","n!=q","x!=j","r!=x","v!=n","g==g","h!=a","m!=u","s!=i","q!=b","t!=y","j!=f","r!=s","x!=m","r!=w","h!=d","e!=w","d!=w","c==c","t!=x","o!=y","w!=d","u!=a","x!=i","f!=o","d!=v","w!=b","c==l","l==s","i!=n","s!=p","a!=k","u!=v","r==y","k!=j","i!=j","s!=f","w!=t","b!=j","e!=l","l==c","o!=b","a!=p","a!=y","h!=r","w!=j","l!=m","t!=p","u!=y","n!=c","l!=p","v!=p","n!=g","y!=w","h!=u","o!=q","h!=w","o==o","t!=q","f!=r","s!=i","w==w","k!=q","q!=x","f!=u","t!=b","n!=k","w!=c","i!=t","r!=g","n!=m","y!=h","u!=n","w!=t","b!=r","r==y","s!=y","e!=g","j!=k","x!=o","o!=u","p!=s","g!=a","i!=j","u!=a","p!=q","t==k","p!=m","e!=h","r!=f","k==d","c==l","i!=g","s!=h","t!=o","l!=n","r!=u","e!=p","e!=b","r!=n","a!=e","v!=t","f!=x","j!=s","e!=t","c==s","c!=f","g!=j","k!=r","y!=x","q!=c","m!=i","q==y","h!=i","o!=i","p!=v","y!=m","e!=u","d==d","n!=d","b!=q","k!=s","h!=j","c!=e","b!=j","s!=a","a!=l","a!=b","n!=y","f!=b","g!=c","f!=g","q!=c","k!=p","f!=o","l!=x","m!=d","d!=r","i!=y","m!=p","u!=t","d!=s","e!=g","n!=p","e!=y","f!=x","e!=b","v==s","x!=c","m!=c","x!=i","w!=r","h!=w","q!=x","w!=o","t!=l","f!=n","d!=o","v!=p","c!=n","l!=j","g!=m","j!=f","q!=i","m!=p","b!=r","a!=s","w!=i","n!=f","q==r","g!=s","a!=d","o!=h","i!=b","h!=y","q!=d","m!=r","q!=b","q==r","b==b","u!=r","p!=q","v==s","n!=t","x!=e","p!=c","d!=a","k!=o","c!=k","h!=f","q!=x","k!=c","w!=v","g!=e","e!=m","g!=a","i!=n","m!=q","e!=y","t!=x","v==c","f!=l","b!=r","l==l","x!=w","e!=n","r!=j","r!=s","i!=k","g!=m","f!=h","f!=s","a!=d","i!=t","o!=j","h!=t","o!=u","k==k","n!=a","o==l","q!=f","s!=f","c!=u","s!=u","j!=r","x!=p","i!=y","o==s","f!=c","y!=e","q!=u","d!=y","t!=b","a!=s","l==o","i!=f","w!=s","e!=s","h!=x","o==c","w!=c","w!=j","n!=l","e!=t","j!=c","j!=v","y!=w","r!=f","a!=f","x!=j","p!=x","y!=a","o==c","p!=k","d!=f","f!=s","u!=q","e!=o","s!=w","q!=w","p!=j","m!=p","h!=a","b!=v","q!=n","y!=p","j!=n","u!=q","g!=n","f!=i","x!=c","g!=i","m!=l","p!=l","k==d","g!=r","v!=f","x!=j","g!=l","e!=j","r==c"]))
print(Solution().equationsPossible(["a==b","b!=c","c==a"])) # False
