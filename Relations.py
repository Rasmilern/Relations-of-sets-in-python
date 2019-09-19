@@ -0,0 +1,303 @@
import functools

class Relation(object):
    def __init__(self, sets, rel):
        #rel为sets上的二元关系
        assert not(len(sets)==0 and len(rel) > 0) #不允许sets为空而rel不为空
        assert sets.issuperset(set([x[0] for x in rel]) | set([x[1] for x in rel])) #不允许rel中出现非sets中的元素
        self.rel = rel
        self.sets = sets

    def diagonalRelation(self):
        #返回代表IA的Relation对象
        #请删除pass后编程实现该方法功能
        R = frozenset([(x,x) for x in list(self.sets)])
        return Relation(self.sets,R)

    def __mul__(self, other):
        assert self.sets == other.sets
        #实现两个关系的合成，即self*other表示other合成self。请注意是先看other的序偶
        #返回合成的结果，为一个Relation对象
        # 请删除pass后编程实现该方法功能
        A = self.sets
        R1,R2 = self.rel , other.rel
        R = set([(x[0],y[1]) for x in R2 for y in R1 if x[1]==y[0]])
        return Relation(A,R)

    def __pow__(self, power, modulo=None):
        # 实现同一关系的多次合成，重载**运算符，即self*self*self=self**3
        # 在每个分支中返回对应的结果，结果是一个Relation对象
        # 请删除pass后编程实现该方法功能
        A = self.sets
        R0 = self.rel
        if power == -1:
            R = set([(x[1],x[0]) for x in R0])
            return Relation(A,R)
        elif power == 0:
            return self.diagonalRelation()
        else:
            t = Relation(A,R0)
            for i in range(power-1):
                t = self*t
            return t

    def __add__(self, other):
        assert self.sets == other.sets
        #实现两个关系的并运算，重载+运算符，即self+other表示self并other
        #请注意，是Relation对象rel成员的并
        #返回结果为一个Relation对象
        # 请删除pass后编程实现该方法功能
        return Relation(self.sets,self.rel | other.rel)

    def __str__(self):
        relstr = '{}'
        setstr = '{}'
        if len(self.rel) > 0:
            relstr = str(self.rel)
        if len(self.sets) > 0:
            setstr = str(self.sets)
        return 'Relation: ' + relstr + ' on Set: ' + setstr

    def __eq__(self, other):
        #判断两个Relation对象是否相等，关系及集合都要相等

        return self.sets == other.sets and self.rel == other.rel

    def toMatrix(self):
        #将序偶集合形式的关系转换为矩阵。
        #为保证矩阵的唯一性，需对self.sets中的元素先排序
        matrix = []
        elems = sorted(list(self.sets))
        line = [0]*len(self.sets)
        for elem in elems:
            #请在此处编写程序，实现转换为矩阵的功能
            for i in range(len(elems)):
                if (elem,elems[i]) in self.rel:
                    line[i] = 1
            matrix.append(line)
            line = [0]*len(self.sets)
            #请在上面编写程序，不要修改下面的代码
        return matrix

    def isReflexive(self):
        #判断self是否为自反关系，是则返回True，否则返回False
        # 请删除pass后编程实现该方法功能
        for a in self.sets:
            if (a,a) not in self.rel:
                return False
        return True


    def isIrreflexive(self):
        # 判断self是否为反自反关系，是则返回True，否则返回False
        # 请删除pass后编程实现该方法功能
        for a in self.sets:
            if (a,a) in self.rel:
                return False
        return True

    def isSymmetric(self):
        # 判断self是否为对称关系，是则返回True，否则返回False
        # 请删除pass后编程实现该方法功能
        for x in self.rel:
            if x[::-1] not in self.rel:
                return False
        return True

    def isAsymmetric(self):
        # 判断self是否为非对称关系，是则返回True，否则返回False
        # 请删除pass后编程实现该方法功能
        for x in self.rel:
            flag = x in self.rel and x[::-1] in self.rel
            if flag:
                return False
        return True
                

    def isAntiSymmetric(self):
        # 判断self是否为反对称关系，是则返回True，否则返回False
        # 请删除pass后编程实现该方法功能
        for x in self.rel:
            flag = x in self.rel and x[::-1] in self.rel and x[0]!=x[1]
            if flag:
                return False
        return True

    def isTransitive(self):
        # 判断self是否为传递关系，是则返回True，否则返回False
        # 请删除pass后编程实现该方法功能
        for x in self.rel:
            for y in self.rel:
                if x==y:
                    continue
                if x[1]==y[0] and (x[0],y[1]) not in self.rel:
                    return False
        return True

    def reflexiveClosure(self):
        #求self的自反闭包，注意使用前面已经重载过的运算符
        #返回一个Relation对象，为self的自反闭包
        # 请删除pass后编程实现该方法功能
        return self+self.diagonalRelation()

    def symmetricClosure(self):
        # 求self的对称闭包，注意使用前面已经重载过的运算符
        # 返回一个Relation对象，为self的对称闭包
        # 请删除pass后编程实现该方法功能
        return self+self**-1

    def transitiveClosure(self):
        closure = self
        while True:
            if closure == closure + self*closure:
                break
            closure = closure + self*closure
        return closure

    def transitiveClosure2(self):
        closure = self
        # 求self的传递闭包，注意使用前面已经重载过的运算符
        # 该方法实现的算法：严格按照传递闭包计算公式求传递闭包
        # 请删除pass后编程实现该方法功能
        for i in range(1,len(self.sets)):
            closure = closure + self**i
        # 请在上面编写程序，不要修改下面代码
        return closure

    def transitiveClosure3(self):
        #该方法利用Roy-Warshall计算传递闭包
        #现将关系转换为矩阵，再调用__warshall函数
        m = self.toMatrix()
        return self.__warshall(m)

    def __warshall(self, a):
        assert (len(row) == len(a) for row in a)
        n = len(a)
        #请在下面编程实现Roy-Warshall求传递闭包的算法
        #参数a：为一个关系矩阵
        # 请删除pass后编程实现该方法功能
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    a[i][j] = a[i][j] or (a[i][k] and a[k][j])
        # 请在上面编写程序，不要修改下面代码
        return a

def isEquivalenceRelation (rel):
    #该函数对给定的Relation对象rel，判断其是否为等价关系
    if rel.isReflexive() and rel.isSymmetric() and rel.isTransitive():
        return True
    else:
        return False

def createPartition(rel):
    #对给定的Relation对象rel，求其决定的rel.sets上的划分
    #如果rel不是等价关系，返回空集
    if not isEquivalenceRelation(rel):
        print("The given relation is not an Equivalence Relation")
        return set([])
    #如rel是等价关系，请编程实现求划分的程序
    partition = set([])
    # 请删除pass后编程实现该方法功能
    for a in rel.sets:
        t = [x[1] for x in rel.rel if x[0]==a]
        partition.add(frozenset(t))
    # 请在上面编写程序，不要修改下面代码
    return partition

def createEquivalenceRelation(partition, A):
    #对给定的集合A，以及A上的一个划分partition
    #生成由该划分决定的等价关系
    assert functools.reduce(lambda x, y: x.union(y), partition) == A
    return Relation(A, set([(a,b) for p in partition for a in p for b in p]))

def isPartialOrder(rel):
    # 该函数对给定的Relation对象rel，判断其是否为半序关系
    if rel.isReflexive() and rel.isAntiSymmetric and rel.isTransitive():
        return True
    else:
        return False

def isQuasiOrder (rel):
    # 该函数对给定的Relation对象rel，判断其是否为拟价关系
    if rel.isIrreflexive() and rel.isTransitive():
        return True
    else:
        return False
    
def isLinearOrder(rel):
    # 该函数对给定的Relation对象rel，判断其是否为全序关系 
    #是则返回True，否则返回False
    if not isPartialOrder(rel):
        return False
    else:
        # 请删除pass后编程实现该方法功能
        for x in rel.sets:
            for y in rel.sets:
                if not ((x,y) in rel.rel and (y,x) in rel.rel):
                    return False
        return True


def join(rel1, rel2):
    #对给定的关系rel1和rel2
    assert rel1.sets == rel2.sets
    #首先得到二者的矩阵
    M1 = rel1.toMatrix()
    M2 = rel2.toMatrix()

    m = len(M1)
    n = m
    M = []
    line = [0]*n
    # 请在此处编写代码，实现关系矩阵的join运算，结果存于M中
    for i in range(n):
        for j in range(n):
            line[j] = int(M1[i][j]+M2[i][j]>=1)
        M.append(line)
        line = [0]*n
    # 请在上面编写代码，实现关系矩阵的join运算
    return M

def meet(rel1, rel2):
    # 对给定的关系rel1和rel2
    assert rel1.sets == rel2.sets

    # 首先得到二者的矩阵
    M1 = rel1.toMatrix()
    M2 = rel2.toMatrix()

    m = len(M1)
    n = m
    M = []
    line = [0]*n
    # 请在此处编写代码，实现关系矩阵的meet运算，结果存于M中
    for i in range(n):
        for j in range(n):
            line[j] = int(M1[i][j]+M2[i][j]==2)
        M.append(line)
        line = [0]*n
    # 请在上面编写代码，实现关系矩阵的meet运算
    return M

def booleanProduct(rel1, rel2):
    # 对给定的关系rel1和rel2
    assert rel1.sets == rel2.sets

    # 首先得到二者的矩阵
    M1 = rel1.toMatrix()
    M2 = rel2.toMatrix()

    m = len(M1)
    n = m
    line = [0]*n
    M = []
    # 请在此处编写代码，实现关系矩阵的布尔乘积运算，结果存于M中
    for i in range(n):
        for j in range(n):
            t = [M2[k][j] and M1[i][k] for k in range(n)]
            line[j] = int(any(t))
        M.append(line)
        line = [0]*n
    # 请在上面编写代码，实现关系矩阵的布尔乘积运算
    return M