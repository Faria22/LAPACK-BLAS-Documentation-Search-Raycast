# CHETRS_3

## Function Signature

```fortran
CHETRS_3(UPLO, N, NRHS, A, LDA, E, IPIV, B, LDB,
*                            INFO)
```

## Description

 CHETRS_3 solves a system of linear equations A * X = B with a complex
 Hermitian matrix A using the factorization computed
 by CHETRF_RK or CHETRF_BK:

    A = P*U*D*(U**H)*(P**T) or A = P*L*D*(L**H)*(P**T),

 where U (or L) is unit upper (or lower) triangular matrix,
 U**H (or L**H) is the conjugate of U (or L), P is a permutation
 matrix, P**T is the transpose of P, and D is Hermitian and block
 diagonal with 1-by-1 and 2-by-2 diagonal blocks.

 This algorithm is using Level 3 BLAS.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix: = 'U': Upper triangular, form is A = P*U*D*(U**H)*(P**T); = 'L': Lower triangular, form is A = P*L*D*(L**H)*(P**T).

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### A (in)

A is COMPLEX array, dimension (LDA,N) Diagonal of the block diagonal matrix D and factors U or L as computed by CHETRF_RK and CHETRF_BK: a) ONLY diagonal elements of the Hermitian block diagonal matrix D on the diagonal of A, i.e. D(k,k) = A(k,k); (superdiagonal (or subdiagonal) elements of D should be provided on entry in array E), and b) If UPLO = 'U': factor U in the superdiagonal part of A. If UPLO = 'L': factor L in the subdiagonal part of A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### E (in)

E is COMPLEX array, dimension (N) On entry, contains the superdiagonal (or subdiagonal) elements of the Hermitian block diagonal matrix D with 1-by-1 or 2-by-2 diagonal blocks, where If UPLO = 'U': E(i) = D(i-1,i),i=2:N, E(1) not referenced; If UPLO = 'L': E(i) = D(i+1,i),i=1:N-1, E(N) not referenced. NOTE: For 1-by-1 diagonal block D(k), where 1 <= k <= N, the element E(k) is not referenced in both UPLO = 'U' or UPLO = 'L' cases.

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by CHETRF_RK or CHETRF_BK.

### B (in,out)

B is COMPLEX array, dimension (LDB,NRHS) On entry, the right hand side matrix B. On exit, the solution matrix X.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

