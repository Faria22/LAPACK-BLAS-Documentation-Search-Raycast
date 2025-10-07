# CGEMMTR

## Function Signature

```fortran
CGEMMTR(UPLO,TRANSA,TRANSB,N,K,ALPHA,A,LDA,B,LDB,BETA,
*                         C,LDC)
```

## Description


 CGEMMTR  performs one of the matrix-matrix operations

    C := alpha*op( A )*op( B ) + beta*C,

 where  op( X ) is one of

    op( X ) = X   or   op( X ) = X**T,

 alpha and beta are scalars, and A, B and C are matrices, with op( A )
 an n by k matrix,  op( B )  a  k by n matrix and  C an n by n matrix.
 Thereby, the routine only accesses and updates the upper or lower
 triangular part of the result matrix C. This behaviour can be used if
 the resulting matrix C is known to be Hermitian or symmetric.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the lower or the upper triangular part of C is access and updated. UPLO = 'L' or 'l', the lower triangular part of C is used. UPLO = 'U' or 'u', the upper triangular part of C is used.

### TRANSA (in)

TRANSA is CHARACTER*1 On entry, TRANSA specifies the form of op( A ) to be used in the matrix multiplication as follows: TRANSA = 'N' or 'n', op( A ) = A. TRANSA = 'T' or 't', op( A ) = A**T. TRANSA = 'C' or 'c', op( A ) = A**H.

### TRANSB (in)

TRANSB is CHARACTER*1 On entry, TRANSB specifies the form of op( B ) to be used in the matrix multiplication as follows: TRANSB = 'N' or 'n', op( B ) = B. TRANSB = 'T' or 't', op( B ) = B**T. TRANSB = 'C' or 'c', op( B ) = B**H.

### N (in)

N is INTEGER On entry, N specifies the number of rows and columns of the matrix C, the number of columns of op(B) and the number of rows of op(A). N must be at least zero.

### K (in)

K is INTEGER On entry, K specifies the number of columns of the matrix op( A ) and the number of rows of the matrix op( B ). K must be at least zero.

### ALPHA (in)

ALPHA is COMPLEX. On entry, ALPHA specifies the scalar alpha.

### A (in)

A is COMPLEX array, dimension ( LDA, ka ), where ka is k when TRANSA = 'N' or 'n', and is n otherwise. Before entry with TRANSA = 'N' or 'n', the leading n by k part of the array A must contain the matrix A, otherwise the leading k by m part of the array A must contain the matrix A.

### LDA (in)

LDA is INTEGER On entry, LDA specifies the first dimension of A as declared in the calling (sub) program. When TRANSA = 'N' or 'n' then LDA must be at least max( 1, n ), otherwise LDA must be at least max( 1, k ).

### B (in)

B is COMPLEX array, dimension ( LDB, kb ), where kb is n when TRANSB = 'N' or 'n', and is k otherwise. Before entry with TRANSB = 'N' or 'n', the leading k by n part of the array B must contain the matrix B, otherwise the leading n by k part of the array B must contain the matrix B.

### LDB (in)

LDB is INTEGER On entry, LDB specifies the first dimension of B as declared in the calling (sub) program. When TRANSB = 'N' or 'n' then LDB must be at least max( 1, k ), otherwise LDB must be at least max( 1, n ).

### BETA (in)

BETA is COMPLEX. On entry, BETA specifies the scalar beta. When BETA is supplied as zero then C need not be set on input.

### C (in,out)

C is COMPLEX array, dimension ( LDC, N ) Before entry, the leading n by n part of the array C must contain the matrix C, except when beta is zero, in which case C need not be set on entry. On exit, the upper or lower triangular part of the matrix C is overwritten by the n by n matrix ( alpha*op( A )*op( B ) + beta*C ).

### LDC (in)

LDC is INTEGER On entry, LDC specifies the first dimension of C as declared in the calling (sub) program. LDC must be at least max( 1, n ).

