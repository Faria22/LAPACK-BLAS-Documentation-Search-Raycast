# DSYCONV

## Function Signature

```fortran
DSYCONV(UPLO, WAY, N, A, LDA, IPIV, E, INFO)
```

## Description


 DSYCONV convert A given by TRF into L and D and vice-versa.
 Get Non-diag elements of D (returned in workspace) and
 apply or reverse permutation done in TRF.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix. = 'U': Upper triangular, form is A = U*D*U**T; = 'L': Lower triangular, form is A = L*D*L**T.

### WAY (in)

WAY is CHARACTER*1 = 'C': Convert = 'R': Revert

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is DOUBLE PRECISION array, dimension (LDA,N) The block diagonal matrix D and the multipliers used to obtain the factor U or L as computed by DSYTRF.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by DSYTRF.

### E (out)

E is DOUBLE PRECISION array, dimension (N) E stores the supdiagonal/subdiagonal of the symmetric 1-by-1 or 2-by-2 block diagonal matrix D in LDLT.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

