# DLAQSY

## Function Signature

```fortran
DLAQSY(UPLO, N, A, LDA, S, SCOND, AMAX, EQUED)
```

## Description


 DLAQSY equilibrates a symmetric matrix A using the scaling factors
 in the vector S.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the upper or lower triangular part of the symmetric matrix A is stored. = 'U': Upper triangular = 'L': Lower triangular

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is DOUBLE PRECISION array, dimension (LDA,N) On entry, the symmetric matrix A. If UPLO = 'U', the leading n by n upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading n by n lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced. On exit, if EQUED = 'Y', the equilibrated matrix: diag(S) * A * diag(S).

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(N,1).

### S (in)

S is DOUBLE PRECISION array, dimension (N) The scale factors for A.

### SCOND (in)

SCOND is DOUBLE PRECISION Ratio of the smallest S(i) to the largest S(i).

### AMAX (in)

AMAX is DOUBLE PRECISION Absolute value of largest matrix entry.

### EQUED (out)

EQUED is CHARACTER*1 Specifies whether or not equilibration was done. = 'N': No equilibration. = 'Y': Equilibration was done, i.e., A has been replaced by diag(S) * A * diag(S).

