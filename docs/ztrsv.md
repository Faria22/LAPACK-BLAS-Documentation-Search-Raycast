# ZTRSV

## Function Signature

```fortran
ZTRSV(UPLO,TRANS,DIAG,N,A,LDA,X,INCX)
```

## Description


 ZTRSV  solves one of the systems of equations

    A*x = b,   or   A**T*x = b,   or   A**H*x = b,

 where b and x are n element vectors and A is an n by n unit, or
 non-unit, upper or lower triangular matrix.

 No test for singularity or near-singularity is included in this
 routine. Such tests must be performed before calling this routine.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the matrix is an upper or lower triangular matrix as follows: UPLO = 'U' or 'u' A is an upper triangular matrix. UPLO = 'L' or 'l' A is a lower triangular matrix.

### TRANS (in)

TRANS is CHARACTER*1 On entry, TRANS specifies the equations to be solved as follows: TRANS = 'N' or 'n' A*x = b. TRANS = 'T' or 't' A**T*x = b. TRANS = 'C' or 'c' A**H*x = b.

### DIAG (in)

DIAG is CHARACTER*1 On entry, DIAG specifies whether or not A is unit triangular as follows: DIAG = 'U' or 'u' A is assumed to be unit triangular. DIAG = 'N' or 'n' A is not assumed to be unit triangular.

### N (in)

N is INTEGER On entry, N specifies the order of the matrix A. N must be at least zero.

### A (in)

A is COMPLEX*16 array, dimension ( LDA, N ) Before entry with UPLO = 'U' or 'u', the leading n by n upper triangular part of the array A must contain the upper triangular matrix and the strictly lower triangular part of A is not referenced. Before entry with UPLO = 'L' or 'l', the leading n by n lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced. Note that when DIAG = 'U' or 'u', the diagonal elements of A are not referenced either, but are assumed to be unity.

### LDA (in)

LDA is INTEGER On entry, LDA specifies the first dimension of A as declared in the calling (sub) program. LDA must be at least max( 1, n ).

### X (in,out)

X is COMPLEX*16 array, dimension at least ( 1 + ( n - 1 )*abs( INCX ) ). Before entry, the incremented array X must contain the n element right-hand side vector b. On exit, X is overwritten with the solution vector x.

### INCX (in)

INCX is INTEGER On entry, INCX specifies the increment for the elements of X. INCX must not be zero.

