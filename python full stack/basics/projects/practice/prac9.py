# s=list(input().split())
# for i in s:
#     if i.isdigit():
#         int(i)
#     if isinstance(i,list):
#         for j in i:
#             if j.isdigit():
#                 int(j)
    
a=["1", "+", ["2", "*", "3"]]
if "*" in a:
    print(a.index("*"))
    print(1)