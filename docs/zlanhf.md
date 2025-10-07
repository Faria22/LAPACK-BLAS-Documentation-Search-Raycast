# ZLANHF

## Function Signature

```fortran
ZLANHF(NORM, TRANSR, UPLO, N, A, WORK)
```

## Description


 ZLANHF  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 complex Hermitian matrix A in RFP format.

## Parameters

### NORM (in)

NORM is CHARACTER Specifies the value to be returned in ZLANHF as described above.

### TRANSR (in)

TRANSR is CHARACTER Specifies whether the RFP format of A is normal or conjugate-transposed format. = 'N': RFP format is Normal = 'C': RFP format is Conjugate-transposed

### UPLO (in)

UPLO is CHARACTER On entry, UPLO specifies whether the RFP matrix A came from an upper or lower triangular matrix as follows: UPLO = 'U' or 'u' RFP A came from an upper triangular matrix UPLO = 'L' or 'l' RFP A came from a lower triangular matrix

### N (in)

N is INTEGER The order of the matrix A. N >= 0. When N = 0, ZLANHF is set to zero.

### A (in)

A is COMPLEX*16 array, dimension ( N*(N+1)/2 ); On entry, the matrix A in RFP Format. RFP Format is described by TRANSR, UPLO and N as follows: If TRANSR='N' then RFP A is (0:N,0:K-1) when N is even; K=N/2. RFP A is (0:N-1,0:K) when N is odd; K=N/2. If TRANSR = 'C' then RFP is the Conjugate-transpose of RFP A as defined when TRANSR = 'N'. The contents of RFP A are defined by UPLO as follows: If UPLO = 'U' the RFP A contains the ( N*(N+1)/2 ) elements of upper packed A either in normal or conjugate-transpose Format. If UPLO = 'L' the RFP A contains the ( N*(N+1) /2 ) elements of lower packed A either in normal or conjugate-transpose Format. The LDA of RFP A is (N+1)/2 when TRANSR = 'C'. When TRANSR is 'N' the LDA is N+1 when N is even and is N when is odd. See the Note below for more details. Unchanged on exit.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (LWORK), where LWORK >= N when NORM = 'I' or '1' or 'O'; otherwise, WORK is not referenced.

