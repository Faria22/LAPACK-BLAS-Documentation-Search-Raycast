# DORM22

## Function Signature

```fortran
DORM22(SIDE, TRANS, M, N, N1, N2, Q, LDQ, C, LDC,
*    $                   WORK, LWORK, INFO)
```

## Parameters

### SIDE (in)

SIDE is CHARACTER*1 = 'L': apply Q or Q**T from the Left; = 'R': apply Q or Q**T from the Right.

### TRANS (in)

TRANS is CHARACTER*1 = 'N': apply Q (No transpose); = 'C': apply Q**T (Conjugate transpose).

### M (in)

M is INTEGER The number of rows of the matrix C. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix C. N >= 0.

### N2 (in] N1
*> \param[in)

N1 is INTEGER N2 is INTEGER The dimension of Q12 and Q21, respectively. N1, N2 >= 0. The following requirement must be satisfied: N1 + N2 = M if SIDE = 'L' and N1 + N2 = N if SIDE = 'R'.

### Q (in)

Q is DOUBLE PRECISION array, dimension (LDQ,M) if SIDE = 'L' (LDQ,N) if SIDE = 'R'

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= max(1,M) if SIDE = 'L'; LDQ >= max(1,N) if SIDE = 'R'.

### C (in,out)

C is DOUBLE PRECISION array, dimension (LDC,N) On entry, the M-by-N matrix C. On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. If SIDE = 'L', LWORK >= max(1,N); if SIDE = 'R', LWORK >= max(1,M). For optimum performance LWORK >= M*N. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

