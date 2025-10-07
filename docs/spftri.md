# SPFTRI

## Function Signature

```fortran
SPFTRI(TRANSR, UPLO, N, A, INFO)
```

## Description


 SPFTRI computes the inverse of a real (symmetric) positive definite
 matrix A using the Cholesky factorization A = U**T*U or A = L*L**T
 computed by SPFTRF.

## Parameters

### TRANSR (in)

TRANSR is CHARACTER*1 = 'N': The Normal TRANSR of RFP A is stored; = 'T': The Transpose TRANSR of RFP A is stored.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is REAL array, dimension ( N*(N+1)/2 ) On entry, the symmetric matrix A in RFP format. RFP format is described by TRANSR, UPLO, and N as follows: If TRANSR = 'N' then RFP A is (0:N,0:k-1) when N is even; k=N/2. RFP A is (0:N-1,0:k) when N is odd; k=N/2. IF TRANSR = 'T' then RFP is the transpose of RFP A as defined when TRANSR = 'N'. The contents of RFP A are defined by UPLO as follows: If UPLO = 'U' the RFP A contains the nt elements of upper packed A. If UPLO = 'L' the RFP A contains the elements of lower packed A. The LDA of RFP A is (N+1)/2 when TRANSR = 'T'. When TRANSR is 'N' the LDA is N+1 when N is even and N is odd. See the Note below for more details. On exit, the symmetric inverse of the original matrix, in the same storage format.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, the (i,i) element of the factor U or L is zero, and the inverse could not be computed.

