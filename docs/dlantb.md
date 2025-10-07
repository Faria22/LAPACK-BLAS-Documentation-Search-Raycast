# DLANTB

## Function Signature

```fortran
DLANTB(NORM, UPLO, DIAG, N, K, AB,
*                        LDAB, WORK)
```

## Description


 DLANTB  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the element of  largest absolute value  of an
 n by n triangular band matrix A,  with ( k + 1 ) diagonals.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in DLANTB as described above.

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the matrix A is upper or lower triangular. = 'U': Upper triangular = 'L': Lower triangular

### DIAG (in)

DIAG is CHARACTER*1 Specifies whether or not the matrix A is unit triangular. = 'N': Non-unit triangular = 'U': Unit triangular

### N (in)

N is INTEGER The order of the matrix A. N >= 0. When N = 0, DLANTB is set to zero.

### K (in)

K is INTEGER The number of super-diagonals of the matrix A if UPLO = 'U', or the number of sub-diagonals of the matrix A if UPLO = 'L'. K >= 0.

### AB (in)

AB is DOUBLE PRECISION array, dimension (LDAB,N) The upper or lower triangular band matrix A, stored in the first k+1 rows of AB. The j-th column of A is stored in the j-th column of the array AB as follows: if UPLO = 'U', AB(k+1+i-j,j) = A(i,j) for max(1,j-k)<=i<=j; if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j<=i<=min(n,j+k). Note that when DIAG = 'U', the elements of the array AB corresponding to the diagonal elements of the matrix A are not referenced, but are assumed to be one.

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= K+1.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)), where LWORK >= N when NORM = 'I'; otherwise, WORK is not referenced.

