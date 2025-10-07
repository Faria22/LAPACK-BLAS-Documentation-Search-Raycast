# CLANSP

## Function Signature

```fortran
CLANSP(NORM, UPLO, N, AP, WORK)
```

## Description


 CLANSP  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 complex symmetric matrix A,  supplied in packed form.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in CLANSP as described above.

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the upper or lower triangular part of the symmetric matrix A is supplied. = 'U': Upper triangular part of A is supplied = 'L': Lower triangular part of A is supplied

### N (in)

N is INTEGER The order of the matrix A. N >= 0. When N = 0, CLANSP is set to zero.

### AP (in)

AP is COMPLEX array, dimension (N*(N+1)/2) The upper or lower triangle of the symmetric matrix A, packed columnwise in a linear array. The j-th column of A is stored in the array AP as follows: if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j; if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j<=i<=n.

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)), where LWORK >= N when NORM = 'I' or '1' or 'O'; otherwise, WORK is not referenced.

