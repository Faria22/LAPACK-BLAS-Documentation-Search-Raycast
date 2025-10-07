# DGELQT

## Function Signature

```fortran
DGELQT(M, N, MB, A, LDA, T, LDT, WORK, INFO)
```

## Description


 DGELQT computes a blocked LQ factorization of a real M-by-N matrix A
 using the compact WY representation of Q.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### MB (in)

MB is INTEGER The block size to be used in the blocked LQ. MIN(M,N) >= MB >= 1.

### A (in,out)

A is DOUBLE PRECISION array, dimension (LDA,N) On entry, the M-by-N matrix A. On exit, the elements on and below the diagonal of the array contain the M-by-MIN(M,N) lower trapezoidal matrix L (L is lower triangular if M <= N); the elements above the diagonal are the rows of V.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### T (out)

T is DOUBLE PRECISION array, dimension (LDT,MIN(M,N)) The upper triangular block reflectors stored in compact form as a sequence of upper triangular blocks. See below for further details.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= MB.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (MB*M). Note: A smaller workspace of MB*(M-MB) may also be sufficient, but that is yet to be proven. MB*M is a conservative estimate and the recommended value to use.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

