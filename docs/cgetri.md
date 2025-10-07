# CGETRI

## Function Signature

```fortran
CGETRI(N, A, LDA, IPIV, WORK, LWORK, INFO)
```

## Description


 CGETRI computes the inverse of a matrix using the LU factorization
 computed by CGETRF.

 This method inverts U and then computes inv(A) by solving the system
 inv(A)*L = inv(U) for inv(A).

## Parameters

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the factors L and U from the factorization A = P*L*U as computed by CGETRF. On exit, if INFO = 0, the inverse of the original matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices from CGETRF; for 1<=i<=N, row i of the matrix was interchanged with row IPIV(i).

### WORK (out)

WORK is COMPLEX array, dimension (MAX(1,LWORK)) On exit, if INFO=0, then WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= max(1,N). For optimal performance LWORK >= N*NB, where NB is the optimal blocksize returned by ILAENV. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, U(i,i) is exactly zero; the matrix is singular and its inverse could not be computed.

