'''

args-->(100,True,20,20.89,100,"java",90.90)

ans = {
    'int':[100,20,100],
    float:[],
    str:[]
    boolean:[True]
}
'''

# def group_by_type(*args):
#     data = {'int':[],'float':[],'bool':[],'str':[]}
#     for i in args:
#         t = type(i).__name__
#         data[t].append(i)
#     return data

def group_by_type(*args):
    return {t:[i for i in args if type(i).__name__ == t] for t in set(type(arg).__name__ for arg in args)}

print(group_by_type(10,30,90.89,"java",False))