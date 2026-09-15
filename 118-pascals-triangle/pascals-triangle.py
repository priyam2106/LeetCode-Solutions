class Solution(object):
    def generate(self, numRows):
      
      tri =[[1]]
      for i in range(numRows-1):
        temp = [0]+tri[-1]+[0]
        row=[]
        for j in range(len(tri[-1])+1):
           row.append(temp[j]+temp[j+1])
        tri.append(row)

      return tri
           

        