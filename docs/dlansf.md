# DLANSF

## Function Signature

```fortran
DLANSF(NORM, TRANSR, UPLO, N, A, WORK)
```

## Description


 DLANSF returns the value of the one norm, or the Frobenius norm, or
 the infinity norm, or the element of largest absolute value of a
 real symmetric matrix A in RFP format.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in DLANSF as described above.

### TRANSR (in)

TRANSR is CHARACTER*1 Specifies whether the RFP format of A is normal or transposed format. = 'N': RFP format is Normal; = 'T': RFP format is Transpose.

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the RFP matrix A came from an upper or lower triangular matrix as follows: = 'U': RFP A came from an upper triangular matrix; = 'L': RFP A came from a lower triangular matrix.

### N (in)

N is INTEGER The order of the matrix A. N >= 0. When N = 0, DLANSF is set to zero.

### A (in)

A is DOUBLE PRECISION array, dimension ( N*(N+1)/2 ); On entry, the upper (if UPLO = 'U') or lower (if UPLO = 'L') part of the symmetric matrix A stored in RFP format. See the "Notes" below for more details. Unchanged on exit.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)), where LWORK >= N when NORM = 'I' or '1' or 'O'; otherwise, WORK is not referenced.

