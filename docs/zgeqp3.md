# ZGEQP3

## Function Signature

```fortran
ZGEQP3(M, N, A, LDA, JPVT, TAU, WORK, LWORK, RWORK,
*                          INFO)
```

## Description


 ZGEQP3 computes a QR factorization with column pivoting of a
 matrix A:  A*P = Q*R  using Level 3 BLAS.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the M-by-N matrix A. On exit, the upper triangle of the array contains the min(M,N)-by-N upper trapezoidal matrix R; the elements below the diagonal, together with the array TAU, represent the unitary matrix Q as a product of min(M,N) elementary reflectors.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### JPVT (in,out)

JPVT is INTEGER array, dimension (N) On entry, if JPVT(J).ne.0, the J-th column of A is permuted to the front of A*P (a leading column); if JPVT(J)=0, the J-th column of A is a free column. On exit, if JPVT(J)=K, then the J-th column of A*P was the the K-th column of A.

### TAU (out)

TAU is COMPLEX*16 array, dimension (min(M,N)) The scalar factors of the elementary reflectors.

### WORK (out)

WORK is COMPLEX*16 array, dimension (MAX(1,LWORK)) On exit, if INFO=0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= N+1. For optimal performance LWORK >= ( N+1 )*NB, where NB is the optimal blocksize. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (2*N)

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

