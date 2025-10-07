# ZTRSM

## Function Signature

```fortran
ZTRSM(SIDE,UPLO,TRANSA,DIAG,M,N,ALPHA,A,LDA,B,LDB)
```

## Description


 ZTRSM  solves one of the matrix equations

    op( A )*X = alpha*B,   or   X*op( A ) = alpha*B,

 where alpha is a scalar, X and B are m by n matrices, A is a unit, or
 non-unit,  upper or lower triangular matrix  and  op( A )  is one  of

    op( A ) = A   or   op( A ) = A**T   or   op( A ) = A**H.

 The matrix X is overwritten on B.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 On entry, SIDE specifies whether op( A ) appears on the left or right of X as follows: SIDE = 'L' or 'l' op( A )*X = alpha*B. SIDE = 'R' or 'r' X*op( A ) = alpha*B.

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the matrix A is an upper or lower triangular matrix as follows: UPLO = 'U' or 'u' A is an upper triangular matrix. UPLO = 'L' or 'l' A is a lower triangular matrix.

### TRANSA (in)

TRANSA is CHARACTER*1 On entry, TRANSA specifies the form of op( A ) to be used in the matrix multiplication as follows: TRANSA = 'N' or 'n' op( A ) = A. TRANSA = 'T' or 't' op( A ) = A**T. TRANSA = 'C' or 'c' op( A ) = A**H.

### DIAG (in)

DIAG is CHARACTER*1 On entry, DIAG specifies whether or not A is unit triangular as follows: DIAG = 'U' or 'u' A is assumed to be unit triangular. DIAG = 'N' or 'n' A is not assumed to be unit triangular.

### M (in)

M is INTEGER On entry, M specifies the number of rows of B. M must be at least zero.

### N (in)

N is INTEGER On entry, N specifies the number of columns of B. N must be at least zero.

### ALPHA (in)

ALPHA is COMPLEX*16 On entry, ALPHA specifies the scalar alpha. When alpha is zero then A is not referenced and B need not be set before entry.

### A (in)

A is COMPLEX*16 array, dimension ( LDA, k ), where k is m when SIDE = 'L' or 'l' and k is n when SIDE = 'R' or 'r'. Before entry with UPLO = 'U' or 'u', the leading k by k upper triangular part of the array A must contain the upper triangular matrix and the strictly lower triangular part of A is not referenced. Before entry with UPLO = 'L' or 'l', the leading k by k lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced. Note that when DIAG = 'U' or 'u', the diagonal elements of A are not referenced either, but are assumed to be unity.

### LDA (in)

LDA is INTEGER On entry, LDA specifies the first dimension of A as declared in the calling (sub) program. When SIDE = 'L' or 'l' then LDA must be at least max( 1, m ), when SIDE = 'R' or 'r' then LDA must be at least max( 1, n ).

### B (in,out)

B is COMPLEX*16 array, dimension ( LDB, N ) Before entry, the leading m by n part of the array B must contain the right-hand side matrix B, and on exit is overwritten by the solution matrix X.

### LDB (in)

LDB is INTEGER On entry, LDB specifies the first dimension of B as declared in the calling (sub) program. LDB must be at least max( 1, m ).

