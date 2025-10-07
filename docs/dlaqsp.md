# DLAQSP

## Function Signature

```fortran
DLAQSP(UPLO, N, AP, S, SCOND, AMAX, EQUED)
```

## Description


 DLAQSP equilibrates a symmetric matrix A using the scaling factors
 in the vector S.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the upper or lower triangular part of the symmetric matrix A is stored. = 'U': Upper triangular = 'L': Lower triangular

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### AP (in,out)

AP is DOUBLE PRECISION array, dimension (N*(N+1)/2) On entry, the upper or lower triangle of the symmetric matrix A, packed columnwise in a linear array. The j-th column of A is stored in the array AP as follows: if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j<=i<=n. On exit, the equilibrated matrix: diag(S) * A * diag(S), in the same storage format as A.

### S (in)

S is DOUBLE PRECISION array, dimension (N) The scale factors for A.

### SCOND (in)

SCOND is DOUBLE PRECISION Ratio of the smallest S(i) to the largest S(i).

### AMAX (in)

AMAX is DOUBLE PRECISION Absolute value of largest matrix entry.

### EQUED (out)

EQUED is CHARACTER*1 Specifies whether or not equilibration was done. = 'N': No equilibration. = 'Y': Equilibration was done, i.e., A has been replaced by diag(S) * A * diag(S).

