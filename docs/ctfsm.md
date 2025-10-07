# CTFSM

## Function Signature

```fortran
CTFSM(TRANSR, SIDE, UPLO, TRANS, DIAG, M, N, ALPHA, A,
*                         B, LDB)
```

## Description


 Level 3 BLAS like routine for A in RFP Format.

 CTFSM solves the matrix equation

    op( A )*X = alpha*B  or  X*op( A ) = alpha*B

 where alpha is a scalar, X and B are m by n matrices, A is a unit, or
 non-unit,  upper or lower triangular matrix  and  op( A )  is one  of

    op( A ) = A   or   op( A ) = A**H.

 A is in Rectangular Full Packed (RFP) Format.

 The matrix X is overwritten on B.

## Parameters

### TRANSR (in)

TRANSR is CHARACTER*1 = 'N': The Normal Form of RFP A is stored; = 'C': The Conjugate-transpose Form of RFP A is stored.

### SIDE (in)

SIDE is CHARACTER*1 On entry, SIDE specifies whether op( A ) appears on the left or right of X as follows: SIDE = 'L' or 'l' op( A )*X = alpha*B. SIDE = 'R' or 'r' X*op( A ) = alpha*B. Unchanged on exit.

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the RFP matrix A came from an upper or lower triangular matrix as follows: UPLO = 'U' or 'u' RFP A came from an upper triangular matrix UPLO = 'L' or 'l' RFP A came from a lower triangular matrix Unchanged on exit.

### TRANS (in)

TRANS is CHARACTER*1 On entry, TRANS specifies the form of op( A ) to be used in the matrix multiplication as follows: TRANS = 'N' or 'n' op( A ) = A. TRANS = 'C' or 'c' op( A ) = conjg( A' ). Unchanged on exit.

### DIAG (in)

DIAG is CHARACTER*1 On entry, DIAG specifies whether or not RFP A is unit triangular as follows: DIAG = 'U' or 'u' A is assumed to be unit triangular. DIAG = 'N' or 'n' A is not assumed to be unit triangular. Unchanged on exit.

### M (in)

M is INTEGER On entry, M specifies the number of rows of B. M must be at least zero. Unchanged on exit.

### N (in)

N is INTEGER On entry, N specifies the number of columns of B. N must be at least zero. Unchanged on exit.

### ALPHA (in)

ALPHA is COMPLEX On entry, ALPHA specifies the scalar alpha. When alpha is zero then A is not referenced and B need not be set before entry. Unchanged on exit.

### A (in)

A is COMPLEX array, dimension (NT) NT = N*(N+1)/2 if SIDE='R' and NT = M*(M+1)/2 otherwise. On entry, the matrix A in RFP Format. RFP Format is described by TRANSR, UPLO and N as follows: If TRANSR='N' then RFP A is (0:N,0:K-1) when N is even; K=N/2. RFP A is (0:N-1,0:K) when N is odd; K=N/2. If TRANSR = 'C' then RFP is the Conjugate-transpose of RFP A as defined when TRANSR = 'N'. The contents of RFP A are defined by UPLO as follows: If UPLO = 'U' the RFP A contains the NT elements of upper packed A either in normal or conjugate-transpose Format. If UPLO = 'L' the RFP A contains the NT elements of lower packed A either in normal or conjugate-transpose Format. The LDA of RFP A is (N+1)/2 when TRANSR = 'C'. When TRANSR is 'N' the LDA is N+1 when N is even and is N when is odd. See the Note below for more details. Unchanged on exit.

### B (in,out)

B is COMPLEX array, dimension (LDB,N) Before entry, the leading m by n part of the array B must contain the right-hand side matrix B, and on exit is overwritten by the solution matrix X.

### LDB (in)

LDB is INTEGER On entry, LDB specifies the first dimension of B as declared in the calling (sub) program. LDB must be at least max( 1, m ). Unchanged on exit.

