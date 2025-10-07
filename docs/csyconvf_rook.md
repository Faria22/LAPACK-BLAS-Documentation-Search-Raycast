# CSYCONVF_ROOK

## Function Signature

```fortran
CSYCONVF_ROOK(UPLO, WAY, N, A, LDA, E, IPIV, INFO)
```

## Description

 If parameter WAY = 'C':
 CSYCONVF_ROOK converts the factorization output format used in
 CSYTRF_ROOK provided on entry in parameter A into the factorization
 output format used in CSYTRF_RK (or CSYTRF_BK) that is stored
 on exit in parameters A and E. IPIV format for CSYTRF_ROOK and
 CSYTRF_RK (or CSYTRF_BK) is the same and is not converted.

 If parameter WAY = 'R':
 CSYCONVF_ROOK performs the conversion in reverse direction, i.e.
 converts the factorization output format used in CSYTRF_RK
 (or CSYTRF_BK) provided on entry in parameters A and E into
 the factorization output format used in CSYTRF_ROOK that is stored
 on exit in parameter A. IPIV format for CSYTRF_ROOK and
 CSYTRF_RK (or CSYTRF_BK) is the same and is not converted.

 CSYCONVF_ROOK can also convert in Hermitian matrix case, i.e. between
 formats used in CHETRF_ROOK and CHETRF_RK (or CHETRF_BK).

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix A. = 'U': Upper triangular = 'L': Lower triangular

### WAY (in)

WAY is CHARACTER*1 = 'C': Convert = 'R': Revert

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) 1) If WAY ='C': On entry, contains factorization details in format used in CSYTRF_ROOK: a) all elements of the symmetric block diagonal matrix D on the diagonal of A and on superdiagonal (or subdiagonal) of A, and b) If UPLO = 'U': multipliers used to obtain factor U in the superdiagonal part of A. If UPLO = 'L': multipliers used to obtain factor L in the superdiagonal part of A. On exit, contains factorization details in format used in CSYTRF_RK or CSYTRF_BK: a) ONLY diagonal elements of the symmetric block diagonal matrix D on the diagonal of A, i.e. D(k,k) = A(k,k); (superdiagonal (or subdiagonal) elements of D are stored on exit in array E), and b) If UPLO = 'U': factor U in the superdiagonal part of A. If UPLO = 'L': factor L in the subdiagonal part of A. 2) If WAY = 'R': On entry, contains factorization details in format used in CSYTRF_RK or CSYTRF_BK: a) ONLY diagonal elements of the symmetric block diagonal matrix D on the diagonal of A, i.e. D(k,k) = A(k,k); (superdiagonal (or subdiagonal) elements of D are stored on exit in array E), and b) If UPLO = 'U': factor U in the superdiagonal part of A. If UPLO = 'L': factor L in the subdiagonal part of A. On exit, contains factorization details in format used in CSYTRF_ROOK: a) all elements of the symmetric block diagonal matrix D on the diagonal of A and on superdiagonal (or subdiagonal) of A, and b) If UPLO = 'U': multipliers used to obtain factor U in the superdiagonal part of A. If UPLO = 'L': multipliers used to obtain factor L in the superdiagonal part of A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### E (in,out)

E is COMPLEX array, dimension (N) 1) If WAY ='C': On entry, just a workspace. On exit, contains the superdiagonal (or subdiagonal) elements of the symmetric block diagonal matrix D with 1-by-1 or 2-by-2 diagonal blocks, where If UPLO = 'U': E(i) = D(i-1,i), i=2:N, E(1) is set to 0; If UPLO = 'L': E(i) = D(i+1,i), i=1:N-1, E(N) is set to 0. 2) If WAY = 'R': On entry, contains the superdiagonal (or subdiagonal) elements of the symmetric block diagonal matrix D with 1-by-1 or 2-by-2 diagonal blocks, where If UPLO = 'U': E(i) = D(i-1,i),i=2:N, E(1) not referenced; If UPLO = 'L': E(i) = D(i+1,i),i=1:N-1, E(N) not referenced. On exit, is not changed

### IPIV (in)

IPIV is INTEGER array, dimension (N) On entry, details of the interchanges and the block structure of D as determined: 1) by CSYTRF_ROOK, if WAY ='C'; 2) by CSYTRF_RK (or CSYTRF_BK), if WAY ='R'. The IPIV format is the same for all these routines. On exit, is not changed.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

