# CLASWP

## Function Signature

```fortran
CLASWP(N, A, LDA, K1, K2, IPIV, INCX)
```

## Description


 CLASWP performs a series of row interchanges on the matrix A.
 One row interchange is initiated for each of rows K1 through K2 of A.

## Parameters

### N (in)

N is INTEGER The number of columns of the matrix A.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the matrix of column dimension N to which the row interchanges will be applied. On exit, the permuted matrix.

### LDA (in)

LDA is INTEGER The leading dimension of the array A.

### K1 (in)

K1 is INTEGER The first element of IPIV for which a row interchange will be done.

### K2 (in)

K2 is INTEGER (K2-K1+1) is the number of elements of IPIV for which a row interchange will be done.

### IPIV (in)

IPIV is INTEGER array, dimension (K1+(K2-K1)*abs(INCX)) The vector of pivot indices. Only the elements in positions K1 through K1+(K2-K1)*abs(INCX) of IPIV are accessed. IPIV(K1+(K-K1)*abs(INCX)) = L implies rows K and L are to be interchanged.

### INCX (in)

INCX is INTEGER The increment between successive values of IPIV. If INCX is negative, the pivots are applied in reverse order.

