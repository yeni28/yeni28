def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0: #부모가 없으면 root
            return i

def preorder(n): #전위순회
    if n:
        print(n, end=" ") # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n): #중위순회
    if n:
        inorder(ch1[n])
        print(n, end=" ") # visit(n)
        inorder(ch2[n])


def postorder(n): #후위순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=" ") # visit(n)

V = int(input()) # 정점 개수, 마지막 정점번호 (주어진 것이 간선인지 정점 번호인지 확인)
arr = list(map(int, input().split()))
E = V - 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

# 자식을 인덱스로 부모 번호 저장
par = [0] * (V + 1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0: # 아직 자식이 없으면
        ch1[p] = c # 자식 1로 저장
    else:
        ch2[p] = c
        par[c] = p
root = find_root(V)
# print(root)
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
