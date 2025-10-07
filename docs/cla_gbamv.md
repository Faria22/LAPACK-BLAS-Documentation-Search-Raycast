# CLA_GBAMV

## Function Signature

```fortran
CLA_GBAMV(TRANS, M, N, KL, KU, ALPHA, AB, LDAB, X,
*                             INCX, BETA, Y, INCY)
```

## Description


 CLA_GBAMV  performs one of the matrix-vector operations

         y := alpha*abs(A)*abs(x) + beta*abs(y),
    or   y := alpha*abs(A)**T*abs(x) + beta*abs(y),

 where alpha and beta are scalars, x and y are vectors and A is an
 m by n matrix.

 This function is primarily used in calculating error bounds.
 To protect against underflow during evaluation, components in
 the resulting vector are perturbed away from zero by (N+1)
 times the underflow threshold.  To prevent unnecessarily large
 errors for block-structure embedded in general matrices,
 "symbolically" zero components are not perturbed.  A zero
 entry is considered "symbolic" if all multiplications involved
 in computing that entry have at least one zero multiplicand.

## Parameters

### TRANS (in)

TRANS is INTEGER On entry, TRANS specifies the operation to be performed as follows: BLAS_NO_TRANS y := alpha*abs(A)*abs(x) + beta*abs(y) BLAS_TRANS y := alpha*abs(A**T)*abs(x) + beta*abs(y) BLAS_CONJ_TRANS y := alpha*abs(A**T)*abs(x) + beta*abs(y) Unchanged on exit.

### M (in)

M is INTEGER On entry, M specifies the number of rows of the matrix A. M must be at least zero. Unchanged on exit.

### N (in)

N is INTEGER On entry, N specifies the number of columns of the matrix A. N must be at least zero. Unchanged on exit.

### KL (in)

KL is INTEGER The number of subdiagonals within the band of A. KL >= 0.

### KU (in)

KU is INTEGER The number of superdiagonals within the band of A. KU >= 0.

### ALPHA (in)

ALPHA is REAL On entry, ALPHA specifies the scalar alpha. Unchanged on exit.

### AB (in)

AB is COMPLEX array, dimension (LDAB,n) Before entry, the leading m by n part of the array AB must contain the matrix of coefficients. Unchanged on exit.

### LDAB (in)

LDAB is INTEGER On entry, LDAB specifies the first dimension of AB as declared in the calling (sub) program. LDAB must be at least max( 1, m ). Unchanged on exit.

### X (in)

X is COMPLEX array, dimension ( 1 + ( n - 1 )*abs( INCX ) ) when TRANS = 'N' or 'n' and at least ( 1 + ( m - 1 )*abs( INCX ) ) otherwise. Before entry, the incremented array X must contain the vector x. Unchanged on exit.

### INCX (in)

INCX is INTEGER On entry, INCX specifies the increment for the elements of X. INCX must not be zero. Unchanged on exit.

### BETA (in)

BETA is REAL On entry, BETA specifies the scalar beta. When BETA is supplied as zero then Y need not be set on input. Unchanged on exit.

### Y (in,out)

Y is REAL array, dimension ( 1 + ( m - 1 )*abs( INCY ) ) when TRANS = 'N' or 'n' and at least ( 1 + ( n - 1 )*abs( INCY ) ) otherwise. Before entry with BETA non-zero, the incremented array Y must contain the vector y. On exit, Y is overwritten by the updated vector y. If either m or n is zero, then Y not referenced and the function performs a quick return.

### INCY (in)

INCY is INTEGER On entry, INCY specifies the increment for the elements of Y. INCY must not be zero. Unchanged on exit. Level 2 Blas routine.

