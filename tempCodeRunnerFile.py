
# class Heap:
	
#     def __init__(self,max_size):
		
#         self.arr = []
#         self.heapsize = 0
#         self.max_size = max_size
		
#     def parent(self,i):
# 		return (i-1)//2

#     def lchild(self,i):
# 		return  (2*i) + 1
    
#     def rchild(self,i):
# 		return  (2*i) + 2
	


#     def insertelement(self,x):
		
#         if self.max_size == self.heapsize:
			
#             return "The stack is overflowed"
		
#         self.heapsize += i
		
#         i = self.heapsize - 1

#         while i!=0 and self.arr[self.parent(i)] < self.arr[i]:
			
#             temp = self.arr[i] 
# 			self.arr[i] = self.arr[self.parent(i)] 
# 			self.arr[self.parent(i)] = temp 
# 			i= self.