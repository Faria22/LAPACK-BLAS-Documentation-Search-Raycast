# DGBTRF

## Function Signature

```fortran
DGBTRF(M, N, KL, KU, AB, LDAB, IPIV, INFO)
```

## Description


 DGBTRF computes an LU factorization of a real m-by-n band matrix A
 using partial pivoting with row interchanges.

 This is the blocked version of the algorithm, calling Level 3 BLAS.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### KL (in)

KL is INTEGER The number of subdiagonals within the band of A. KL >= 0.

### KU (in)

KU is INTEGER The number of superdiagonals within the band of A. KU >= 0.

### AB (in,out)

AB is DOUBLE PRECISION array, dimension (LDAB,N) On entry, the matrix A in band storage, in rows KL+1 to 2*KL+KU+1; rows 1 to KL of the array need not be set. The j-th column of A is stored in the j-th column of the array AB as follows: AB(kl+ku+1+i-j,j) = A(i,j) for max(1,j-ku)<=i<=min(m,j+kl) On exit, details of the factorization: U is stored as an upper triangular band matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and the multipliers used during the factorization are stored in rows KL+KU+2 to 2*KL+KU+1. See below for further details.

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= 2*KL+KU+1.

### IPIV (out)

IPIV is INTEGER array, dimension (min(M,N)) The pivot indices; for 1 <= i <= min(M,N), row i of the matrix was interchanged with row IPIV(i).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = +i, U(i,i) is exactly zero. The factorization has been completed, but the factor U is exactly singular, and division by zero will occur if it is used to solve a system of equations.

