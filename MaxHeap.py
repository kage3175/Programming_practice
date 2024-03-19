import sys

class Heap:
  def __init__(self) -> None:
    self.heap = [0 for _ in range(10000)]
    self.size = 0
  def swap(self, a, b):
    tmp = self.heap[a]
    self.heap[a] = self.heap[b]
    self.heap[b] = tmp
  def insert(self, k):
    self.heap[self.size] = k
    self.size+=1
    index = self.size-1
    while(index > 0):
      parent = (index - 1) // 2
      if(self.heap[parent] < self.heap[index]):
        self.swap(parent, index)
        index = parent
      else:
        return
  def show(self):
    print("[", end="")
    for i in range(self.size):
      print(self.heap[i], end=", ")
    print("]")
  def delete_max(self):
    if(self.size==0):
      print("Empty heap.")
      return "err"
    else:
      max_ = self.heap[0]
      self.heap[0] = self.heap[self.size-1]
      self.size -=1
      self.siftDown(0)
      return max_
  def isLeaf(self, index):
    return (index >= self.size//2)
  def largerChild(self, index):
    if(self.heap[index*2+2] == 0):
      return index*2+1
    else:
      if(self.heap[index*2+2] > self.heap[index*2+1]):
        return index*2+2
      else:
        return index*2+1
  def siftDown(self, index):
    while(not self.isLeaf(index)):
      child = self.largerChild(index)
      if(self.heap[child] > self.heap[index]):
        self.swap(index, child)
        index = child
      else:
        return
      pass


heap = Heap()
while(True):
  x = input()
  if(x == 'q'):
    sys.exit(0)
  elif(x =='d'):
    max_ = heap.delete_max()
    if(max_ == "err"):
      continue
    print("최댓값: " + str(max_))
    heap.show()
  else:
    try:
      x = int(x)
    except:
      print("정수 또는 q가 아닙니다. 다시 입력해주세요.")
      continue
    heap.insert(x)
    heap.show()
