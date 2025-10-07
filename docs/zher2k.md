# ZHER2K

## Function Signature

```fortran
ZHER2K(UPLO,TRANS,N,K,ALPHA,A,LDA,B,LDB,BETA,C,LDC)
```

## Description


 ZHER2K  performs one of the hermitian rank 2k operations

    C := alpha*A*B**H + conjg( alpha )*B*A**H + beta*C,

 or

    C := alpha*A**H*B + conjg( alpha )*B**H*A + beta*C,

 where  alpha and beta  are scalars with  beta  real,  C is an  n by n
 hermitian matrix and  A and B  are  n by k matrices in the first case
 and  k by n  matrices in the second case.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the upper or lower triangular part of the array C is to be referenced as follows: UPLO = 'U' or 'u' Only the upper triangular part of C is to be referenced. UPLO = 'L' or 'l' Only the lower triangular part of C is to be referenced.

### TRANS (in)

TRANS is CHARACTER*1 On entry, TRANS specifies the operation to be performed as follows: TRANS = 'N' or 'n' C := alpha*A*B**H + conjg( alpha )*B*A**H + beta*C. TRANS = 'C' or 'c' C := alpha*A**H*B + conjg( alpha )*B**H*A + beta*C.

### N (in)

N is INTEGER On entry, N specifies the order of the matrix C. N must be at least zero.

### K (in)

K is INTEGER On entry with TRANS = 'N' or 'n', K specifies the number of columns of the matrices A and B, and on entry with TRANS = 'C' or 'c', K specifies the number of rows of the matrices A and B. K must be at least zero.

### ALPHA (in)

ALPHA is COMPLEX*16 . On entry, ALPHA specifies the scalar alpha.

### A (in)

A is COMPLEX*16 array, dimension ( LDA, ka ), where ka is k when TRANS = 'N' or 'n', and is n otherwise. Before entry with TRANS = 'N' or 'n', the leading n by k part of the array A must contain the matrix A, otherwise the leading k by n part of the array A must contain the matrix A.

### LDA (in)

LDA is INTEGER On entry, LDA specifies the first dimension of A as declared in the calling (sub) program. When TRANS = 'N' or 'n' then LDA must be at least max( 1, n ), otherwise LDA must be at least max( 1, k ).

### B (in)

B is COMPLEX*16 array, dimension ( LDB, kb ), where kb is k when TRANS = 'N' or 'n', and is n otherwise. Before entry with TRANS = 'N' or 'n', the leading n by k part of the array B must contain the matrix B, otherwise the leading k by n part of the array B must contain the matrix B.

### LDB (in)

LDB is INTEGER On entry, LDB specifies the first dimension of B as declared in the calling (sub) program. When TRANS = 'N' or 'n' then LDB must be at least max( 1, n ), otherwise LDB must be at least max( 1, k ). Unchanged on exit.

### BETA (in)

BETA is DOUBLE PRECISION . On entry, BETA specifies the scalar beta.

### C (in,out)

C is COMPLEX*16 array, dimension ( LDC, N ) Before entry with UPLO = 'U' or 'u', the leading n by n upper triangular part of the array C must contain the upper triangular part of the hermitian matrix and the strictly lower triangular part of C is not referenced. On exit, the upper triangular part of the array C is overwritten by the upper triangular part of the updated matrix. Before entry with UPLO = 'L' or 'l', the leading n by n lower triangular part of the array C must contain the lower triangular part of the hermitian matrix and the strictly upper triangular part of C is not referenced. On exit, the lower triangular part of the array C is overwritten by the lower triangular part of the updated matrix. Note that the imaginary parts of the diagonal elements need not be set, they are assumed to be zero, and on exit they are set to zero.

### LDC (in)

LDC is INTEGER On entry, LDC specifies the first dimension of C as declared in the calling (sub) program. LDC must be at least max( 1, n ).

