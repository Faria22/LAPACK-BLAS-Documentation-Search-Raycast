# ZLARSCL2

## Function Signature

```fortran
ZLARSCL2(M, N, D, X, LDX)
```

## Description


 ZLARSCL2 performs a reciprocal diagonal scaling on a matrix:
   x <-- inv(D) * x
 where the DOUBLE PRECISION diagonal matrix D is stored as a vector.

 Eventually to be replaced by BLAS_zge_diag_scale in the new BLAS
 standard.

## Parameters

### M (in)

M is INTEGER The number of rows of D and X. M >= 0.

### N (in)

N is INTEGER The number of columns of X. N >= 0.

### D (in)

D is DOUBLE PRECISION array, length M Diagonal matrix D, stored as a vector of length M.

### X (in,out)

X is COMPLEX*16 array, dimension (LDX,N) On entry, the matrix X to be scaled by D. On exit, the scaled matrix.

### LDX (in)

LDX is INTEGER The leading dimension of the matrix X. LDX >= M.

