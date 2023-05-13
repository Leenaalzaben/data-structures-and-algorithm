
matrix = [
[0, 1, 5], [-4, 7, 2], [-3, 12, 11]]
def summation(matrix):
    total_sum = []
    for row in matrix:
        row_sum = sum(row)
        total_sum.append(row_sum)
    return total_sum

sums = summation(matrix)
print(f" {matrix}        {sums}")  
