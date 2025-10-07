# ZLAMSWLQ

## Function Signature

```fortran
ZLAMSWLQ(SIDE, TRANS, M, N, K, MB, NB, A, LDA, T,
*     $                LDT, C, LDC, WORK, LWORK, INFO)
```

## Description


    ZLAMSWLQ overwrites the general complex M-by-N matrix C with


                    SIDE = 'L'     SIDE = 'R'
    TRANS = 'N':      Q * C          C * Q
    TRANS = 'C':      Q**H * C       C * Q**H
    where Q is a complex unitary matrix defined as the product of blocked
    elementary reflectors computed by short wide LQ
    factorization (ZLASWLQ)

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply Q or Q**H from the Left; = 'R': apply Q or Q**H from the Right.

### TRANS (in)

TRANS is CHARACTER*1 = 'N': No transpose, apply Q; = 'C': Conjugate Transpose, apply Q**H.

### M (in)

M is INTEGER The number of rows of the matrix C. M >=0.

### N (in)

N is INTEGER The number of columns of the matrix C. N >= 0.

### K (in)

K is INTEGER The number of elementary reflectors whose product defines the matrix Q. M >= K >= 0;

### MB (in)

MB is INTEGER The row block size to be used in the blocked LQ. M >= MB >= 1

### NB (in)

NB is INTEGER The column block size to be used in the blocked LQ. NB > M.

### A (in)

A is COMPLEX*16 array, dimension (LDA,M) if SIDE = 'L', (LDA,N) if SIDE = 'R' The i-th row must contain the vector which defines the blocked elementary reflector H(i), for i = 1,2,...,k, as returned by ZLASWLQ in the first k rows of its array argument A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= MAX(1,K).

### T (in)

T is COMPLEX*16 array, dimension ( M * Number of blocks(CEIL(N-K/NB-K)), The blocked upper triangular block reflectors stored in compact form as a sequence of upper triangular blocks. See below for further details.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= MB.

### C (in,out)

C is COMPLEX*16 array, dimension (LDC,N) On entry, the M-by-N matrix C. On exit, C is overwritten by Q*C or Q**H*C or C*Q**H or C*Q.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

(workspace) COMPLEX*16 array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the minimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. If MIN(M,N,K) = 0, LWORK >= 1. If SIDE = 'L', LWORK >= max(1,NB*MB). If SIDE = 'R', LWORK >= max(1,M*MB). If LWORK = -1, then a workspace query is assumed; the routine only calculates the minimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

