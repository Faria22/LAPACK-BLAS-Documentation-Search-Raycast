# ZLAQP2

## Function Signature

```fortran
ZLAQP2(M, N, OFFSET, A, LDA, JPVT, TAU, VN1, VN2,
*                          WORK)
```

## Description


 ZLAQP2 computes a QR factorization with column pivoting of
 the block A(OFFSET+1:M,1:N).
 The block A(1:OFFSET,1:N) is accordingly pivoted, but not factorized.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### OFFSET (in)

OFFSET is INTEGER The number of rows of the matrix A that must be pivoted but no factorized. OFFSET >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the M-by-N matrix A. On exit, the upper triangle of block A(OFFSET+1:M,1:N) is the triangular factor obtained; the elements in block A(OFFSET+1:M,1:N) below the diagonal, together with the array TAU, represent the orthogonal matrix Q as a product of elementary reflectors. Block A(1:OFFSET,1:N) has been accordingly pivoted, but no factorized.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### JPVT (in,out)

JPVT is INTEGER array, dimension (N) On entry, if JPVT(i) .ne. 0, the i-th column of A is permuted to the front of A*P (a leading column); if JPVT(i) = 0, the i-th column of A is a free column. On exit, if JPVT(i) = k, then the i-th column of A*P was the k-th column of A.

### TAU (out)

TAU is COMPLEX*16 array, dimension (min(M,N)) The scalar factors of the elementary reflectors.

### VN1 (in,out)

VN1 is DOUBLE PRECISION array, dimension (N) The vector with the partial column norms.

### VN2 (in,out)

VN2 is DOUBLE PRECISION array, dimension (N) The vector with the exact column norms.

### WORK (out)

WORK is COMPLEX*16 array, dimension (N)

