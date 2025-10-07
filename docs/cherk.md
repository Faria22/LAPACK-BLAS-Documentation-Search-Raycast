# CHERK

## Function Signature

```fortran
CHERK(UPLO,TRANS,N,K,ALPHA,A,LDA,BETA,C,LDC)
```

## Description


 CHERK  performs one of the hermitian rank k operations

    C := alpha*A*A**H + beta*C,

 or

    C := alpha*A**H*A + beta*C,

 where  alpha and beta  are  real scalars,  C is an  n by n  hermitian
 matrix and  A  is an  n by k  matrix in the  first case and a  k by n
 matrix in the second case.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the upper or lower triangular part of the array C is to be referenced as follows: UPLO = 'U' or 'u' Only the upper triangular part of C is to be referenced. UPLO = 'L' or 'l' Only the lower triangular part of C is to be referenced.

### TRANS (in)

TRANS is CHARACTER*1 On entry, TRANS specifies the operation to be performed as follows: TRANS = 'N' or 'n' C := alpha*A*A**H + beta*C. TRANS = 'C' or 'c' C := alpha*A**H*A + beta*C.

### N (in)

N is INTEGER On entry, N specifies the order of the matrix C. N must be at least zero.

### K (in)

K is INTEGER On entry with TRANS = 'N' or 'n', K specifies the number of columns of the matrix A, and on entry with TRANS = 'C' or 'c', K specifies the number of rows of the matrix A. K must be at least zero.

### ALPHA (in)

ALPHA is REAL On entry, ALPHA specifies the scalar alpha.

### A (in)

A is COMPLEX array, dimension ( LDA, ka ), where ka is k when TRANS = 'N' or 'n', and is n otherwise. Before entry with TRANS = 'N' or 'n', the leading n by k part of the array A must contain the matrix A, otherwise the leading k by n part of the array A must contain the matrix A.

### LDA (in)

LDA is INTEGER On entry, LDA specifies the first dimension of A as declared in the calling (sub) program. When TRANS = 'N' or 'n' then LDA must be at least max( 1, n ), otherwise LDA must be at least max( 1, k ).

### BETA (in)

BETA is REAL On entry, BETA specifies the scalar beta.

### C (in,out)

C is COMPLEX array, dimension ( LDC, N ) Before entry with UPLO = 'U' or 'u', the leading n by n upper triangular part of the array C must contain the upper triangular part of the hermitian matrix and the strictly lower triangular part of C is not referenced. On exit, the upper triangular part of the array C is overwritten by the upper triangular part of the updated matrix. Before entry with UPLO = 'L' or 'l', the leading n by n lower triangular part of the array C must contain the lower triangular part of the hermitian matrix and the strictly upper triangular part of C is not referenced. On exit, the lower triangular part of the array C is overwritten by the lower triangular part of the updated matrix. Note that the imaginary parts of the diagonal elements need not be set, they are assumed to be zero, and on exit they are set to zero.

### LDC (in)

LDC is INTEGER On entry, LDC specifies the first dimension of C as declared in the calling (sub) program. LDC must be at least max( 1, n ).

