# SLANST

## Function Signature

```fortran
SLANST(NORM, N, D, E)
```

## Description


 SLANST  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 real symmetric tridiagonal matrix A.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in SLANST as described above.

### N (in)

N is INTEGER The order of the matrix A. N >= 0. When N = 0, SLANST is set to zero.

### D (in)

D is REAL array, dimension (N) The diagonal elements of A.

### E (in)

E is REAL array, dimension (N-1) The (n-1) sub-diagonal or super-diagonal elements of A.

