from typing import List
class Solution:
    def __init__(self) -> None:
        self.output = []

    def generate(self, numRows: int) -> List[List[int]]:
        row = []
        answer = []
        for i in range(1,numRows+1):
            for j in range (i):
                print(f'value of i ={i} and j={j} is ')
                if j==0 or j==i-1:
                    print(f"Appending 1 becuase j is {j}")
                    row.append(1)
                else:
                    try:
                        row.append(answer[i-2][j-1]+answer[i-2][j])
                    except Exception as e:
                        print(answer)
                        print(f' pakda exception i = {i} aur j = {j}')
            answer.append(row)
            row=[]
        return answer




o = Solution()
print(o.generate(1))