# CLAQPS

## Function Signature

```fortran
CLAQPS(M, N, OFFSET, NB, KB, A, LDA, JPVT, TAU, VN1,
*                          VN2, AUXV, F, LDF)
```

## Description


 CLAQPS computes a step of QR factorization with column pivoting
 of a complex M-by-N matrix A by using Blas-3.  It tries to factorize
 NB columns from A starting from the row OFFSET+1, and updates all
 of the matrix with Blas-3 xGEMM.

 In some cases, due to catastrophic cancellations, it cannot
 factorize NB columns.  Hence, the actual number of factorized
 columns is returned in KB.

 Block A(1:OFFSET,1:N) is accordingly pivoted, but not factorized.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0

### OFFSET (in)

OFFSET is INTEGER The number of rows of A that have been factorized in previous steps.

### NB (in)

NB is INTEGER The number of columns to factorize.

### KB (out)

KB is INTEGER The number of columns actually factorized.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the M-by-N matrix A. On exit, block A(OFFSET+1:M,1:KB) is the triangular factor obtained and block A(1:OFFSET,1:N) has been accordingly pivoted, but no factorized. The rest of the matrix, block A(OFFSET+1:M,KB+1:N) has been updated.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### JPVT (in,out)

JPVT is INTEGER array, dimension (N) JPVT(I) = K <==> Column K of the full matrix A has been permuted into position I in AP.

### TAU (out)

TAU is COMPLEX array, dimension (KB) The scalar factors of the elementary reflectors.

### VN1 (in,out)

VN1 is REAL array, dimension (N) The vector with the partial column norms.

### VN2 (in,out)

VN2 is REAL array, dimension (N) The vector with the exact column norms.

### AUXV (in,out)

AUXV is COMPLEX array, dimension (NB) Auxiliary vector.

### F (in,out)

F is COMPLEX array, dimension (LDF,NB) Matrix F**H = L * Y**H * A.

### LDF (in)

LDF is INTEGER The leading dimension of the array F. LDF >= max(1,N).

