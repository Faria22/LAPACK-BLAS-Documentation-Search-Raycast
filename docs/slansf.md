# SLANSF

## Function Signature

```fortran
SLANSF(NORM, TRANSR, UPLO, N, A, WORK)
```

## Description


 SLANSF returns the value of the one norm, or the Frobenius norm, or
 the infinity norm, or the element of largest absolute value of a
 real symmetric matrix A in RFP format.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in SLANSF as described above.

### TRANSR (in)

TRANSR is CHARACTER*1 Specifies whether the RFP format of A is normal or transposed format. = 'N': RFP format is Normal; = 'T': RFP format is Transpose.

### UPLO (in)

UPLO is CHARACTER*1 On entry, UPLO specifies whether the RFP matrix A came from an upper or lower triangular matrix as follows: = 'U': RFP A came from an upper triangular matrix; = 'L': RFP A came from a lower triangular matrix.

### N (in)

N is INTEGER The order of the matrix A. N >= 0. When N = 0, SLANSF is set to zero.

### A (in)

A is REAL array, dimension ( N*(N+1)/2 ); On entry, the upper (if UPLO = 'U') or lower (if UPLO = 'L') part of the symmetric matrix A stored in RFP format. See the "Notes" below for more details. Unchanged on exit.

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)), where LWORK >= N when NORM = 'I' or '1' or 'O'; otherwise, WORK is not referenced.

