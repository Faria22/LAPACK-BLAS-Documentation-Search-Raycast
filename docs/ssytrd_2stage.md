# SSYTRD_2STAGE

## Function Signature

```fortran
SSYTRD_2STAGE(VECT, UPLO, N, A, LDA, D, E, TAU,
*                                 HOUS2, LHOUS2, WORK, LWORK, INFO)
```

## Description


 SSYTRD_2STAGE reduces a real symmetric matrix A to real symmetric
 tridiagonal form T by a orthogonal similarity transformation:
 Q1**T Q2**T* A * Q2 * Q1 = T.

## Parameters

### VECT (in)

VECT is CHARACTER*1 = 'N': No need for the Housholder representation, in particular for the second stage (Band to tridiagonal) and thus LHOUS2 is of size max(1, 4*N); = 'V': the Householder representation is needed to either generate Q1 Q2 or to apply Q1 Q2, then LHOUS2 is to be queried and computed. (NOT AVAILABLE IN THIS RELEASE).

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is REAL array, dimension (LDA,N) On entry, the symmetric matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced. On exit, if UPLO = 'U', the band superdiagonal of A are overwritten by the corresponding elements of the internal band-diagonal matrix AB, and the elements above the KD superdiagonal, with the array TAU, represent the orthogonal matrix Q1 as a product of elementary reflectors; if UPLO = 'L', the diagonal and band subdiagonal of A are over- written by the corresponding elements of the internal band-diagonal matrix AB, and the elements below the KD subdiagonal, with the array TAU, represent the orthogonal matrix Q1 as a product of elementary reflectors. See Further Details.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### D (out)

D is REAL array, dimension (N) The diagonal elements of the tridiagonal matrix T.

### E (out)

E is REAL array, dimension (N-1) The off-diagonal elements of the tridiagonal matrix T.

### TAU (out)

TAU is REAL array, dimension (N-KD) The scalar factors of the elementary reflectors of the first stage (see Further Details).

### HOUS2 (out)

HOUS2 is REAL array, dimension (MAX(1,LHOUS2)) Stores the Householder representation of the stage2 band to tridiagonal.

### LHOUS2 (in)

LHOUS2 is INTEGER The dimension of the array HOUS2. LHOUS2 >= 1. If LWORK = -1, or LHOUS2 = -1, then a query is assumed; the routine only calculates the optimal size of the HOUS2 array, returns this value as the first entry of the HOUS2 array, and no error message related to LHOUS2 is issued by XERBLA. If VECT='N', LHOUS2 = max(1, 4*n); if VECT='V', option not yet available.

### WORK (out)

WORK is REAL array, dimension (LWORK)

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. If N = 0, LWORK >= 1, else LWORK = MAX(1, dimension). If LWORK = -1, or LHOUS2 = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA. LWORK = MAX(1, dimension) where dimension = max(stage1,stage2) + (KD+1)*N = N*KD + N*max(KD+1,FACTOPTNB) + max(2*KD*KD, KD*NTHREADS) + (KD+1)*N where KD is the blocking size of the reduction, FACTOPTNB is the blocking used by the QR or LQ algorithm, usually FACTOPTNB=128 is a good choice NTHREADS is the number of threads used when openMP compilation is enabled, otherwise =1.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

