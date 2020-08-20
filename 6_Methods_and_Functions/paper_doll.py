"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""

def paper_doll(text):
    st = ''
    for x in text:
        st = st + x*3

    return st

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))