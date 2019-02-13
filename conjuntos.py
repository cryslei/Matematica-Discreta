#pertinencia
a = {1,2,3,4,5}
b = {3,4,2.1}
1 in a

#subconjunto
contA = 0
a = {1,4,6,8}
b = {1,4,6,8,10}
for x in a:
    if x in b:
        contA += 1
if len(a) == contA:
    print("A esta contido em B.")

# continencia e igualdade
contA = 0
contB = 0
a = {1,4,6,8}
b = {1,4,6,8}
for x in a:
    if x in b:
        contA += 1
for y in b:
    if y in a:
        contB += 1
if len(a) == contA and len(b) == contB:
    print("A esta contido em B e B esta contido em A.")




