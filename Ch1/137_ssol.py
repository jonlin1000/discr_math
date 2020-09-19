#Tokenizer of Expression
#Example Expression: ~(T & F) | T
def tokenize(expr):
    ac = ["T", "F", "(", ")", "~", "&", "|", " ", "\t"]
    ls = []
    for i in range(0, len(expr)):
        if expr[i] not in ac:
            raise Exception("invalid expression")
        if expr[i] != " ":
            ls.append(expr[i])
    return ls

"""
Test expressions:
(T & F)
~(T | T)
T & (~F | ~T)

A CFG for this grammar is:
E -> (E) | A
A -> E & A | O
O -> E|O | N
N -> ~ E | C
C -> T | F
"""

#Evaluation of Syntax Tree
#any expression is either true/false, an and expr, an or expr, or a not expr.
def evaluate(sTree):
    if sTree == True:
        return True
    elif sTree == False:
        return False
    elif sTree[0] == "and":
        assert len(sTree) == 3, "invalid syntax Tree"
        return evaluate(sTree[1]) and evaluate(sTree[2])
    elif sTree[0] == "or":
        assert len(sTree) == 3, "invalid syntax Tree"
        return evaluate(sTree[1]) or evaluate(sTree[2])
    elif sTree[0] == "not":
        assert len(sTree) == 2, "invalid syntax Tree"
        return not evaluate(sTree[1])
    else:
        raise Exception("invalid expression")


#Evaluator Tests
assert evaluate(True) == True, "something bad happened"
assert evaluate(["and", True, False]) == False, "unexpected and behavior"
assert evaluate(["and", ["not", False], ["or", False, True]]), "unexpected behavior"
