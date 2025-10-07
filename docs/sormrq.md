# SORMRQ

## Function Signature

```fortran
SORMRQ(SIDE, TRANS, M, N, K, A, LDA, TAU, C, LDC,
*                          WORK, LWORK, INFO)
```

## Description


 SORMRQ overwrites the general real M-by-N matrix C with

                 SIDE = 'L'     SIDE = 'R'
 TRANS = 'N':      Q * C          C * Q
 TRANS = 'T':      Q**T * C       C * Q**T

 where Q is a real orthogonal matrix defined as the product of k
 elementary reflectors

       Q = H(1) H(2) . . . H(k)

 as returned by SGERQF. Q is of order M if SIDE = 'L' and of order N
 if SIDE = 'R'.

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply Q or Q**T from the Left; = 'R': apply Q or Q**T from the Right.

### TRANS (in)

TRANS is CHARACTER*1 = 'N': No transpose, apply Q; = 'T': Transpose, apply Q**T.

### M (in)

M is INTEGER The number of rows of the matrix C. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix C. N >= 0.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. If SIDE = 'L', M >= K >= 0; if SIDE = 'R', N >= K >= 0.

### A (in)

A is REAL array, dimension (LDA,M) if SIDE = 'L', (LDA,N) if SIDE = 'R' The i-th row must contain the vector which defines the elementary reflector H(i), for i = 1,2,...,k, as returned by SGERQF in the last k rows of its array argument A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,K).

### TAU (in)

TAU is REAL array, dimension (K) TAU(i) must contain the scalar factor of the elementary reflector H(i), as returned by SGERQF.

### C (in,out)

C is REAL array, dimension (LDC,N) On entry, the M-by-N matrix C. On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. If SIDE = 'L', LWORK >= max(1,N); if SIDE = 'R', LWORK >= max(1,M). For good performance, LWORK should generally be larger. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

