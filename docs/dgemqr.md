# DGEMQR

## Function Signature

```fortran
DGEMQR(SIDE, TRANS, M, N, K, A, LDA, T,
*     $                   TSIZE, C, LDC, WORK, LWORK, INFO)
```

## Description


 DGEMQR overwrites the general real M-by-N matrix C with

                      SIDE = 'L'     SIDE = 'R'
      TRANS = 'N':      Q * C          C * Q
      TRANS = 'T':      Q**T * C       C * Q**T

 where Q is a real orthogonal matrix defined as the product
 of blocked elementary reflectors computed by tall skinny
 QR factorization (DGEQR)


## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply Q or Q**T from the Left; = 'R': apply Q or Q**T from the Right.

### TRANS (in)

TRANS is CHARACTER*1 = 'N': No transpose, apply Q; = 'T': Transpose, apply Q**T.

### M (in)

M is INTEGER The number of rows of the matrix A. M >=0.

### N (in)

N is INTEGER The number of columns of the matrix C. N >= 0.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. If SIDE = 'L', M >= K >= 0; if SIDE = 'R', N >= K >= 0.

### A (in)

A is DOUBLE PRECISION array, dimension (LDA,K) Part of the data structure to represent Q as returned by DGEQR.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. If SIDE = 'L', LDA >= max(1,M); if SIDE = 'R', LDA >= max(1,N).

### T (in)

T is DOUBLE PRECISION array, dimension (MAX(5,TSIZE)). Part of the data structure to represent Q as returned by DGEQR.

### TSIZE (in)

TSIZE is INTEGER The dimension of the array T. TSIZE >= 5.

### C (in,out)

C is DOUBLE PRECISION array, dimension (LDC,N) On entry, the M-by-N matrix C. On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

(workspace) DOUBLE PRECISION array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the minimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= 1. If LWORK = -1, then a workspace query is assumed. The routine only calculates the size of the WORK array, returns this value as WORK(1), and no error message related to WORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

