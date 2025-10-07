# ZLANGT

## Function Signature

```fortran
ZLANGT(NORM, N, DL, D, DU)
```

## Description


 ZLANGT  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 complex tridiagonal matrix A.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in ZLANGT as described above.

### N (in)

N is INTEGER The order of the matrix A. N >= 0. When N = 0, ZLANGT is set to zero.

### DL (in)

DL is COMPLEX*16 array, dimension (N-1) The (n-1) sub-diagonal elements of A.

### D (in)

D is COMPLEX*16 array, dimension (N) The diagonal elements of A.

### DU (in)

DU is COMPLEX*16 array, dimension (N-1) The (n-1) super-diagonal elements of A.

