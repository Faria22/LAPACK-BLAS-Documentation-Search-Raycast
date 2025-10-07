# SGEMM

## Function Signature

```fortran
SGEMM(TRANSA,TRANSB,M,N,K,ALPHA,A,LDA,B,LDB,BETA,C,LDC)
```

## Description


 SGEMM  performs one of the matrix-matrix operations

    C := alpha*op( A )*op( B ) + beta*C,

 where  op( X ) is one of

    op( X ) = X   or   op( X ) = X**T,

 alpha and beta are scalars, and A, B and C are matrices, with op( A )
 an m by k matrix,  op( B )  a  k by n matrix and  C an m by n matrix.

 Note: if alpha and/or beta is zero, some parts of the matrix-matrix
  operations are not performed. This results in the following NaN/Inf
  propagation quirks:

  1. If alpha is zero, NaNs or Infs in A or B do not affect the result.
  2. If both alpha and beta are zero, then a zero matrix is returned in C,
   irrespective of any NaNs or Infs in A, B or C.
  3. If only beta is zero, alpha*op( A )*op( B ) is returned, irrespective
   of any NaNs or Infs in C.

## Parameters

### TRANSA (in)

TRANSA is CHARACTER*1 On entry, TRANSA specifies the form of op( A ) to be used in the matrix multiplication as follows: TRANSA = 'N' or 'n', op( A ) = A. TRANSA = 'T' or 't', op( A ) = A**T. TRANSA = 'C' or 'c', op( A ) = A**T. Note: TRANSA = 'C' is supported for the sake of API consistency between all ?GEMM variants.

### TRANSB (in)

TRANSB is CHARACTER*1 On entry, TRANSB specifies the form of op( B ) to be used in the matrix multiplication as follows: TRANSB = 'N' or 'n', op( B ) = B. TRANSB = 'T' or 't', op( B ) = B**T. TRANSB = 'C' or 'c', op( B ) = B**T. Note: TRANSB = 'C' is supported for the sake of API consistency between all ?GEMM variants.

### M (in)

M is INTEGER On entry, M specifies the number of rows of the matrix op( A ) and of the matrix C. M must be at least zero.

### N (in)

N is INTEGER On entry, N specifies the number of columns of the matrix op( B ) and the number of columns of the matrix C. N must be at least zero.

### K (in)

K is INTEGER On entry, K specifies the number of columns of the matrix op( A ) and the number of rows of the matrix op( B ). K must be at least zero.

### ALPHA (in)

ALPHA is REAL On entry, ALPHA specifies the scalar alpha. If ALPHA is zero the values in A and B do not affect the result. This also means that NaN/Inf propagation from A and B is inhibited if ALPHA is zero.

### A (in)

A is REAL array, dimension ( LDA, ka ), where ka is k when TRANSA = 'N' or 'n', and is m otherwise. Before entry with TRANSA = 'N' or 'n', the leading m by k part of the array A must contain the matrix A, otherwise the leading k by m part of the array A must contain the matrix A, except if ALPHA is zero. If ALPHA is zero, none of the values in A affect the result, even if they are NaN/Inf. This also implies that if ALPHA is zero, the matrix elements of A need not be initialized by the caller.

### LDA (in)

LDA is INTEGER On entry, LDA specifies the first dimension of A as declared in the calling (sub) program. When TRANSA = 'N' or 'n' then LDA must be at least max( 1, m ), otherwise LDA must be at least max( 1, k ).

### B (in)

B is REAL array, dimension ( LDB, kb ), where kb is n when TRANSB = 'N' or 'n', and is k otherwise. Before entry with TRANSB = 'N' or 'n', the leading k by n part of the array B must contain the matrix B, otherwise the leading n by k part of the array B must contain the matrix B, except if ALPHA is zero. If ALPHA is zero, none of the values in B affect the result, even if they are NaN/Inf. This also implies that if ALPHA is zero, the matrix elements of B need not be initialized by the caller.

### LDB (in)

LDB is INTEGER On entry, LDB specifies the first dimension of B as declared in the calling (sub) program. When TRANSB = 'N' or 'n' then LDB must be at least max( 1, k ), otherwise LDB must be at least max( 1, n ).

### BETA (in)

BETA is REAL On entry, BETA specifies the scalar beta. If BETA is zero the values in C do not affect the result. This also means that NaN/Inf propagation from C is inhibited if BETA is zero.

### C (in,out)

C is REAL array, dimension ( LDC, N ) Before entry, the leading m by n part of the array C must contain the matrix C, except if beta is zero. If beta is zero, none of the values in C affect the result, even if they are NaN/Inf. This also implies that if beta is zero, the matrix elements of C need not be initialized by the caller. On exit, the array C is overwritten by the m by n matrix ( alpha*op( A )*op( B ) + beta*C ).

### LDC (in)

LDC is INTEGER On entry, LDC specifies the first dimension of C as declared in the calling (sub) program. LDC must be at least max( 1, m ).

