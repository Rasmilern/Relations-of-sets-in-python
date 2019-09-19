from Relations import *

print('#'*30+'Testing Relation Initializing'+'#'*30)
Empty = set([])
relSample = set([])
rel = Relation(Empty, relSample)
print(rel)
try:
    relSample = {(1, 2), (2, 3)}
    rel = Relation(Empty, relSample)
except:
    print('A Non-Empty relation ' + str(relSample) + ' on Empty set')

setSample = {1, 2, 3}
relSample = set([])
rel = Relation(setSample, relSample)
print(rel)
relSample = {(1, 2), (2, 3)}
rel = Relation(setSample, relSample)
print(rel)
relSample = {(0, 1), (3, 4)}
try:
    rel = Relation(setSample, relSample)
except:
    print(str(relSample) + ' is not a relation on the given set ' + str(setSample))

A = set([1, 2, 3])
Smaller = {(1, 2), (1, 3), (2, 3)}
Greater = {(2, 1), (3, 1), (3, 2)}
Equal = {(1, 1), (2, 2), (3, 3)}
Smaller_Equal = {(1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3)}
Greater_Equal = {(1, 1), (2, 2), (3, 3), (2, 1), (3, 1), (3, 2)}
B = {"Alice1", "Alice2", "Bob1", "Bob2", "Chris1", "Chris2"}
isTwinOf = {("Alice1", "Alice2"), ("Alice2", "Alice1"),
            ("Bob1", "Bob2"), ("Bob2", "Bob1"),
            ("Chris1", "Chris2"), ("Chris2", "Chris1")}

print('\n'+'#' * 30 + 'Testing Reflexive' + '#' * 30)
print('Empty relations on Empty sets are reflexive: ', Relation(Empty, Empty).isReflexive())
print('Empty relations on Non-Empty sets are reflexive: ', Relation(setSample, Empty).isReflexive())
print("Smaller relations is reflexive:", Relation(A,Smaller).isReflexive())
print("Greater relations is reflexive:", Relation(A,Greater).isReflexive())
print("Equal relations is reflexive:", Relation(A,Equal).isReflexive())
print("Smaller_Equal relations is reflexive:", Relation(A,Smaller_Equal).isReflexive())
print("Greater_Equal relations is reflexive:", Relation(A,Greater_Equal).isReflexive())
print("isTwinOf relations is reflexive:", Relation(B,isTwinOf).isReflexive())

print('\n'+'#' * 30 + 'Testing Irreflexive' + '#' * 30)
print('Empty relations on Empty sets are irreflexive: ', Relation(Empty, Empty).isIrreflexive())
print('Empty relations on Non-Empty sets are irreflexive: ', Relation(setSample, Empty).isIrreflexive())
print("Smaller relations is irreflexive:", Relation(A, Smaller).isIrreflexive())
print("Greater relations is irreflexive:", Relation(A, Greater).isIrreflexive())
print("Equal relations is irreflexive:", Relation(A, Equal).isIrreflexive())
print("Smaller_Equal relations is irreflexive:", Relation(A, Smaller_Equal).isIrreflexive())
print("Greater_Equal relations is irreflexive:", Relation(A, Greater_Equal).isIrreflexive())
print("isTwinOf relations is irreflexive:", Relation(B, isTwinOf).isIrreflexive())

print('\n' + '#' * 30 + 'Testing Symmetric' + '#' * 30)
print('Empty relations on Empty sets are symmetric: ', Relation(Empty, Empty).isSymmetric())
print('Empty relations on Non-Empty sets are symmetric: ', Relation(setSample, Empty).isSymmetric())
print("Smaller relations is symmetric:", Relation(A, Smaller).isSymmetric())
print("Greater relations is symmetric:", Relation(A, Greater).isSymmetric())
print("Equal relations is symmetric:", Relation(A, Equal).isSymmetric())
print("Smaller_Equal relations is symmetric:", Relation(A, Smaller_Equal).isSymmetric())
print("Greater_Equal relations is symmetric:", Relation(A, Greater_Equal).isSymmetric())
print("isTwinOf relations is symmetric:", Relation(B, isTwinOf).isSymmetric())

print('\n' + '#' * 30 + 'Testing Asymmetric' + '#' * 30)
print('Empty relations on Empty sets are asymmetric: ', Relation(Empty, Empty).isAsymmetric())
print('Empty relations on Non-Empty sets are asymmetric: ', Relation(setSample, Empty).isAsymmetric())
print("Smaller relations is asymmetric:", Relation(A, Smaller).isAsymmetric())
print("Greater relations is asymmetric:", Relation(A, Greater).isAsymmetric())
print("Equal relations is asymmetric:", Relation(A, Equal).isAsymmetric())
print("Smaller_Equal relations is asymmetric:", Relation(A, Smaller_Equal).isAsymmetric())
print("Greater_Equal relations is asymmetric:", Relation(A, Greater_Equal).isAsymmetric())
print("isTwinOf relations is asymmetric:", Relation(B, isTwinOf).isAsymmetric())

print('\n' + '#' * 30 + 'Testing Antisymmetric' + '#' * 30)
print('Empty relations on Empty sets are antisymmetric: ', Relation(Empty, Empty).isAntiSymmetric())
print('Empty relations on Non-Empty sets are antisymmetric: ', Relation(setSample, Empty).isAntiSymmetric())
print("Smaller relations is antisymmetric:", Relation(A, Smaller).isAntiSymmetric())
print("Greater relations is antisymmetric:", Relation(A, Greater).isAntiSymmetric())
print("Equal relations is antisymmetric:", Relation(A, Equal).isAntiSymmetric())
print("Smaller_Equal relations is antisymmetric:", Relation(A, Smaller_Equal).isAntiSymmetric())
print("Greater_Equal relations is antisymmetric:", Relation(A, Greater_Equal).isAntiSymmetric())
print("isTwinOf relations is antisymmetric:", Relation(B, isTwinOf).isAntiSymmetric())

print('\n' + '#' * 30 + 'Testing Transitive' + '#' * 30)
print('Empty relations on Empty sets are transitive: ', Relation(Empty, Empty).isTransitive())
print('Empty relations on Non-Empty sets are transitive: ', Relation(setSample, Empty).isTransitive())
print("Smaller relations is transitive:", Relation(A, Smaller).isTransitive())
print("Greater relations is transitive:", Relation(A, Greater).isTransitive())
print("Equal relations is transitive:", Relation(A, Equal).isTransitive())
print("Smaller_Equal relations is transitive:", Relation(A, Smaller_Equal).isTransitive())
print("Greater_Equal relations is transitive:", Relation(A, Greater_Equal).isTransitive())
print("isTwinOf relations is transitive:", Relation(B, isTwinOf).isTransitive())

print('\n' + '#' * 30 + 'Testing Relation Operations' + '#' * 30)
print('Relation Composition: ')
R1 = frozenset([(1, 2), (1, 3), (2, 4), (3, 5)])
R2 = frozenset([(2, 4), (3, 5)])
rel1 = Relation({1, 2, 3, 4, 5}, R1)
rel2 = Relation({1, 2, 3, 4, 5}, R2)
print(rel2 * rel1)
print(rel1 * rel2)
print(Relation({1, 2, 3, 4, 5}, set([]))*rel1)

print(rel1**-1)
print(rel1**0)
print(rel1**1)
print(rel1**2)

print('Relation Union: ')
print(rel1 + rel2)

print('\n' + '#' * 30 + 'Testing Relation Composition Power' + '#' * 30)
rel3 = Relation({'a','b','c'},{('a','b'),('b','c'),('c','a')})
for i in range(-1, 5):
    print(rel3**i)

print('\n' + '#' * 30 + 'Testing Special Relation' + '#' * 30)
print('Equivalence Relation: ')
print(isEquivalenceRelation(Relation({1,2,3,4},{(1,1),(2,2), (3,3),(4,4),(1,3),(2,4),(3,1),(4,2)})))
print('Create partitions: ')
p = createPartition(Relation({1, 2, 3, 4}, {(1, 1), (2, 2), (3, 3), (4, 4), (1, 3), (2, 4), (3, 1), (4, 2)}))
print(p)
print(createEquivalenceRelation(p, {1, 2, 3, 4}))
print(createEquivalenceRelation({frozenset({2}), frozenset({4}), frozenset({1, 3})}, {1, 2, 3, 4}))
print('Partial Order Relation: ')
print(isPartialOrder(Relation({1, 2, 3}, {(1, 2), (2, 3)})))
print(isPartialOrder(Relation({1, 2, 3}, {(1, 2), (2, 3), (1, 3), (1, 1), (2, 2), (3, 3)})))
print('Quasi Order Relation: ')
print(isQuasiOrder(Relation({1, 2, 3}, {(1, 2), (2, 3)})))
print(isQuasiOrder(Relation({1, 2, 3}, {(1, 2)})))
print(isQuasiOrder(Relation({1, 2, 3, 4}, {(1, 2), (1, 4), (1, 3), (2, 4), (2, 3), (3, 4)})))
print('Linear Order: ')
print(isLinearOrder(Relation({1, 2, 3}, {(1, 2), (1, 3), (2, 3), (1, 1), (2, 2), (3, 3)})))
print(isLinearOrder(Relation({1, 2, 3, 4}, {(1, 2), (1, 3), (2, 3), (1, 1), (2, 2), (3, 3), (4, 4)})))

print('\n' + '#' * 30 + 'Testing Relation Closure' + '#' * 30)
print(Relation({1, 2, 3}, {(1, 2),(2, 3)}).reflexiveClosure())
print(Relation({1, 2, 3}, {(1, 2), (2, 3)}).symmetricClosure())
print(Relation({1, 2, 3}, {(1, 2), (2, 3)}).transitiveClosure())
print(Relation({1, 2, 3}, {(1, 2), (2, 3)}).transitiveClosure2())
print(Relation({1, 2, 3, 4}, {(1, 2), (2, 3), (3, 2), (3, 4), (4, 4)}).transitiveClosure())
print(Relation({1, 2, 3, 4}, {(1, 2), (2, 3), (3, 2), (3, 4), (4, 4)}).transitiveClosure2())

print('\n' + '#' * 30 + 'Testing Converting to Matrix' + '#' * 30)

def printMatrix(M):
    for i in range(len(M)):
        print(M[i])
    print('\n')

printMatrix(Relation({1, 2, 3}, {(1, 2), (2, 3)}).toMatrix())
printMatrix(Relation({1, 2, 3}, {(1, 2), (2, 3)}).reflexiveClosure().toMatrix())
printMatrix(Relation({1, 2, 3}, {(1, 2), (2, 3)}).symmetricClosure().toMatrix())
printMatrix(Relation({1, 2, 3, 4}, {(1, 2), (2, 3), (3, 2), (3, 4), (4, 4)}).transitiveClosure().toMatrix())
printMatrix(Relation({1, 2, 3, 4}, {(1, 2), (2, 3), (3, 2), (3, 4), (4, 4)}).transitiveClosure2().toMatrix())
printMatrix(Relation({1, 2, 3, 4}, {(1, 2), (2, 3), (3, 2), (3, 4), (4, 4)}).transitiveClosure3())

print('\n' + '#' * 30 + 'Testing Matrix Operations' + '#' * 30)
relation1 = Relation({1, 2, 3, 4}, {(1, 1), (2, 2), (3, 1), (3, 3), (4, 1), (4, 3)})
relation2 = Relation({1, 2, 3, 4}, {(1, 2), (1, 3), (2, 2), (2, 3), (3, 3), (3, 4), (4, 1), (4, 2)})
printMatrix(relation1.toMatrix())
printMatrix(relation2.toMatrix())
print('Join: ')
printMatrix(join(relation1, relation2))
print('Meet: ')
printMatrix(meet(relation1, relation2))
print('Boolean product: ')
print('relation1 compose relation2: ')
printMatrix(booleanProduct(relation1, relation2))
print('relation2 compose relation1: ')
printMatrix(booleanProduct(relation2, relation1))