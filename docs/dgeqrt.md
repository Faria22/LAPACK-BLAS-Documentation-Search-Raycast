# DGEQRT

## Function Signature

```fortran
DGEQRT(M, N, NB, A, LDA, T, LDT, WORK, INFO)
```

## Description


 DGEQRT computes a blocked QR factorization of a real M-by-N matrix A
 using the compact WY representation of Q.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### NB (in)

NB is INTEGER The block size to be used in the blocked QR. MIN(M,N) >= NB >= 1.

### A (in,out)

A is DOUBLE PRECISION array, dimension (LDA,N) On entry, the M-by-N matrix A. On exit, the elements on and above the diagonal of the array contain the min(M,N)-by-N upper trapezoidal matrix R (R is upper triangular if M >= N); the elements below the diagonal are the columns of V.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### T (out)

T is DOUBLE PRECISION array, dimension (LDT,MIN(M,N)) The upper triangular block reflectors stored in compact form as a sequence of upper triangular blocks. See below for further details.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= NB.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (NB*N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

