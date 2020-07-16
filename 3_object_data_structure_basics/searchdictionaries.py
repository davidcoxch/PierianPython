# In this question, we display hello from dictionaries
# of varying complexity

d = {'simple_key':'hello'}
print("Find hello in 'simple_key':'hello'")
print(d['simple_key'])
print()

e = {'k1':{'k2':'hello'}}
print("Find hello in 'k1':{'k2':'hello'")
print(e['k1']['k2'])
print()

f = {'k1':[{'nest_key':['this is deep',['hello']]}]}


print("Find hello in 'k1':[{'nest_key':['this is deep',['hello']]}]")
print(f['k1'][0]['nest_key'][1][0])
print()

print("Find hello in 'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]")
g = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(g['k1'][2]['k2'][1]['tough'][2][0])
