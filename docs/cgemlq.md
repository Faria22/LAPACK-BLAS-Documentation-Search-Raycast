# CGEMLQ

## Function Signature

```fortran
CGEMLQ(SIDE, TRANS, M, N, K, A, LDA, T,
*     $                   TSIZE, C, LDC, WORK, LWORK, INFO)
```

## Description


     CGEMLQ overwrites the general real M-by-N matrix C with

                      SIDE = 'L'     SIDE = 'R'
      TRANS = 'N':      Q * C          C * Q
      TRANS = 'C':      Q**H * C       C * Q**H
      where Q is a complex unitary matrix defined as the product
      of blocked elementary reflectors computed by short wide
      LQ factorization (CGELQ)


## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply Q or Q**H from the Left; = 'R': apply Q or Q**H from the Right.

### TRANS (in)

TRANS is CHARACTER*1 = 'N': No transpose, apply Q; = 'C': Conjugate transpose, apply Q**H.

### M (in)

M is INTEGER The number of rows of the matrix A. M >=0.

### N (in)

N is INTEGER The number of columns of the matrix C. N >= 0.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. If SIDE = 'L', M >= K >= 0; if SIDE = 'R', N >= K >= 0.

### A (in)

A is COMPLEX array, dimension (LDA,M) if SIDE = 'L', (LDA,N) if SIDE = 'R' Part of the data structure to represent Q as returned by CGELQ.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,K).

### T (in)

T is COMPLEX array, dimension (MAX(5,TSIZE)). Part of the data structure to represent Q as returned by CGELQ.

### TSIZE (in)

TSIZE is INTEGER The dimension of the array T. TSIZE >= 5.

### C (in,out)

C is COMPLEX array, dimension (LDC,N) On entry, the M-by-N matrix C. On exit, C is overwritten by Q*C or Q**H*C or C*Q**H or C*Q.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

(workspace) COMPLEX array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the minimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= 1. If LWORK = -1, then a workspace query is assumed. The routine only calculates the size of the WORK array, returns this value as WORK(1), and no error message related to WORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

