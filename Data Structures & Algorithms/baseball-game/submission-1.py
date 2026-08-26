class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        result=0
        for i in range(len(operations)):    
            if operations[i]=='+':
                # find valid values
                rLength=len(record)
                record.append(record[rLength-1]+record[rLength-2])
            elif operations[i]=='C':
                record.pop()
            elif operations[i]=='D':
                rLength=len(record)
                record.append(2*record[rLength-1])
            else:
                record.append(int(operations[i]))
        for i in range(len(record)):
            result=result+record[i]
        return result