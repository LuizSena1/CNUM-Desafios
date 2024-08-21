import numpy as np
def gauss_elimination(A, b):
  """
  Gauss elimination method [By Bottom Science].

  A - the coefficient matrix (an n x n matrix)
  b - the right-hand side column vector (an n x 1 matrix)

  """

  n = len(A)

  # Perform Gauss elimination
  for i in range(n):
    # Find the pivot element
    pivot = abs(A[i][i])
    pivot_row = i
    for j in range(i+1, n):
      if abs(A[j][i]) > pivot:
        pivot = abs(A[j][i])
        pivot_row = j

    # Swap the pivot row with the current row (if necessary)
    if pivot_row != i:
      A[i], A[pivot_row] = A[pivot_row], A[i]
      b[i], b[pivot_row] = b[pivot_row], b[i]

    # Eliminate the current variable from the other equations
    for j in range(i+1, n):
      factor = A[j][i] / A[i][i]
      for k in range(i, n):
        A[j][k] -= factor * A[i][k]
      b[j] -= factor * b[i]

  # Back-substitute to find the solution
  x = [0 for _ in range(n)]
  for i in range(n-1, -1, -1):
    x[i] = b[i]
    for j in range(i+1, n):
      x[i] -= A[i][j] * x[j]
    x[i] /= A[i][i]
    x[i] = round(x[i],8)
  return x

# A - Coefficient Matrix

A = [[2, 1, 4], [3, 7, 6], [5, 4, 3]]
b = [8, 9, 8]
x = gauss_elimination(A, b)
x = np.array(x)
print(x)  # Output: [1.0, 3.0, -2.0]