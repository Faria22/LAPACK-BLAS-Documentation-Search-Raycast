# ZLANHT

## Function Signature

```fortran
ZLANHT(NORM, N, D, E)
```

## Description


 ZLANHT  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 complex Hermitian tridiagonal matrix A.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in ZLANHT as described above.

### N (in)

N is INTEGER The order of the matrix A. N >= 0. When N = 0, ZLANHT is set to zero.

### D (in)

D is DOUBLE PRECISION array, dimension (N) The diagonal elements of A.

### E (in)

E is COMPLEX*16 array, dimension (N-1) The (n-1) sub-diagonal or super-diagonal elements of A.

