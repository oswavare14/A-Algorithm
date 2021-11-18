a = [
    ['-','-','-','-','-'],
    ['-','-','-','D','-'],
    ['-','-','-','-','-'],
    ['-','>','-','O','-'],
    ['-','-','-','-','-']
    ]
start = (3,1)
end = (3,3)

def make_step(k):
  d = '>'
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == k:
        if (i>0 and m[i-1][j] == 0 and a[i-1][j] == '-') or (i>0 and m[i-1][j] == 0 and a[i-1][j] == 'D') or (i>0 and m[i-1][j] == 0 and a[i-1][j] == 'O')\
                or (i>0 and m[i-1][j] == 0 and a[i-1][j] == d):
          m[i-1][j] = k + 1
        if (j>0 and m[i][j-1] == 0 and a[i][j-1] == '-') or (j>0 and m[i][j-1] == 0 and a[i][j-1] == 'D') or (j>0 and m[i][j-1] == 0 and a[i][j-1] == 'O')\
                or (j>0 and m[i][j-1] == 0 and a[i][j-1] == d):
          m[i][j-1] = k + 1
        if (i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == '-') or (i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 'D') or (i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 'O')\
                or (i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == d):
          m[i+1][j] = k + 1
        if (j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == '-') or (j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 'D') or (j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 'O')\
                or (j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == d):
           m[i][j+1] = k + 1

m = []
for i in range(len(a)):
    m.append([])
    for j in range(len(a[i])):
        m[-1].append(0)
i,j = start
m[i][j] = 1
k = 0
while m[end[0]][end[1]] == 0:
    k += 1
    make_step(k)


i, j = end
k = m[i][j]
camino = [(i,j)]
while k > 1:
  if i > 0 and m[i - 1][j] == k-1:
    i, j = i-1, j
    camino.append((i, j))
    k-=1
  elif j > 0 and m[i][j - 1] == k-1:
    i, j = i, j-1
    camino.append((i, j))
    k-=1
  elif i < len(m) - 1 and m[i + 1][j] == k-1:
    i, j = i+1, j
    camino.append((i, j))
    k-=1
  elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
    i, j = i, j+1
    camino.append((i, j))
    k -= 1

print(camino)
