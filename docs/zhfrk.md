# ZHFRK

## Function Signature

```fortran
ZHFRK(TRANSR, UPLO, TRANS, N, K, ALPHA, A, LDA, BETA,
*                         C)
```

## Description


 Level 3 BLAS like routine for C in RFP Format.

 ZHFRK performs one of the Hermitian rank--k operations

    C := alpha*A*A**H + beta*C,

 or

    C := alpha*A**H*A + beta*C,

 where alpha and beta are real scalars, C is an n--by--n Hermitian
 matrix and A is an n--by--k matrix in the first case and a k--by--n
 matrix in the second case.

## Parameters

### TRANSR (in)

TRANSR is CHARACTER*1 = 'N': The Normal Form of RFP A is stored; = 'C': The Conjugate-transpose Form of RFP A is stored.

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the upper or lower triangular part of the array C is to be referenced as follows: UPLO = 'U' or 'u' Only the upper triangular part of C is to be referenced. UPLO = 'L' or 'l' Only the lower triangular part of C is to be referenced. Unchanged on exit.

### TRANS (in)

TRANS is CHARACTER*1 On entry, TRANS specifies the operation to be performed as follows: TRANS = 'N' or 'n' C := alpha*A*A**H + beta*C. TRANS = 'C' or 'c' C := alpha*A**H*A + beta*C. Unchanged on exit.

### N (in)

N is INTEGER On entry, N specifies the order of the matrix C. N must be at least zero. Unchanged on exit.

### K (in)

K is INTEGER On entry with TRANS = 'N' or 'n', K specifies the number of columns of the matrix A, and on entry with TRANS = 'C' or 'c', K specifies the number of rows of the matrix A. K must be at least zero. Unchanged on exit.

### ALPHA (in)

ALPHA is DOUBLE PRECISION On entry, ALPHA specifies the scalar alpha. Unchanged on exit.

### A (in)

A is COMPLEX*16 array, dimension (LDA,ka) where KA is K when TRANS = 'N' or 'n', and is N otherwise. Before entry with TRANS = 'N' or 'n', the leading N--by--K part of the array A must contain the matrix A, otherwise the leading K--by--N part of the array A must contain the matrix A. Unchanged on exit.

### LDA (in)

LDA is INTEGER On entry, LDA specifies the first dimension of A as declared in the calling (sub) program. When TRANS = 'N' or 'n' then LDA must be at least max( 1, n ), otherwise LDA must be at least max( 1, k ). Unchanged on exit.

### BETA (in)

BETA is DOUBLE PRECISION On entry, BETA specifies the scalar beta. Unchanged on exit.

### C (in,out)

C is COMPLEX*16 array, dimension (N*(N+1)/2) On entry, the matrix A in RFP Format. RFP Format is described by TRANSR, UPLO and N. Note that the imaginary parts of the diagonal elements need not be set, they are assumed to be zero, and on exit they are set to zero.

