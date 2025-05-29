'''

args-->(100,True,20,20.89,100,"java",90.90)

ans = {
    'int':[100,20,100],
    float:[],
    str:[]
    boolean:[True]
}
'''
def classify_args(*args):
    result = {
        'int': [],
        'float': [],
        'str': [],
        'boolean': []
    }

    for item in args:
        if type(item) == 'bool':
            result('boolean').append(item)
        elif type(item) == int:
            result['int'].append(item)
        elif type(item) == float:
            result['float'].append(item)
        elif type(item) == str:
            result['str'].append(item)
    return result


ans = classify_args(100,True,39,90,89.90,False,"jainish","khunt","kunj","vidhi")
print(ans)