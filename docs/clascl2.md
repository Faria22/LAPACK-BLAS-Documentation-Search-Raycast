# CLASCL2

## Function Signature

```fortran
CLASCL2(M, N, D, X, LDX)
```

## Description


 CLASCL2 performs a diagonal scaling on a matrix:
   x <-- D * x
 where the diagonal REAL matrix D is stored as a matrix.

 Eventually to be replaced by BLAS_cge_diag_scale in the new BLAS
 standard.

## Parameters

### M (in)

M is INTEGER The number of rows of D and X. M >= 0.

### N (in)

N is INTEGER The number of columns of X. N >= 0.

### D (in)

D is REAL array, length M Diagonal matrix D, stored as a vector of length M.

### X (in,out)

X is COMPLEX array, dimension (LDX,N) On entry, the matrix X to be scaled by D. On exit, the scaled matrix.

### LDX (in)

LDX is INTEGER The leading dimension of the matrix X. LDX >= M.

