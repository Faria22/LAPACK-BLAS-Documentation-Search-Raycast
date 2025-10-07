# CHECON_3

## Function Signature

```fortran
CHECON_3(UPLO, N, A, LDA, E, IPIV, ANORM, RCOND,
*                            WORK, INFO)
```

## Description

 CHECON_3 estimates the reciprocal of the condition number (in the
 1-norm) of a complex Hermitian matrix A using the factorization
 computed by CHETRF_RK or CHETRF_BK:

    A = P*U*D*(U**H)*(P**T) or A = P*L*D*(L**H)*(P**T),

 where U (or L) is unit upper (or lower) triangular matrix,
 U**H (or L**H) is the conjugate of U (or L), P is a permutation
 matrix, P**T is the transpose of P, and D is Hermitian and block
 diagonal with 1-by-1 and 2-by-2 diagonal blocks.

 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).
 This routine uses BLAS3 solver CHETRS_3.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the details of the factorization are stored as an upper or lower triangular matrix: = 'U': Upper triangular, form is A = P*U*D*(U**H)*(P**T); = 'L': Lower triangular, form is A = P*L*D*(L**H)*(P**T).

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in)

A is COMPLEX array, dimension (LDA,N) Diagonal of the block diagonal matrix D and factors U or L as computed by CHETRF_RK and CHETRF_BK: a) ONLY diagonal elements of the Hermitian block diagonal matrix D on the diagonal of A, i.e. D(k,k) = A(k,k); (superdiagonal (or subdiagonal) elements of D should be provided on entry in array E), and b) If UPLO = 'U': factor U in the superdiagonal part of A. If UPLO = 'L': factor L in the subdiagonal part of A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### E (in)

E is COMPLEX array, dimension (N) On entry, contains the superdiagonal (or subdiagonal) elements of the Hermitian block diagonal matrix D with 1-by-1 or 2-by-2 diagonal blocks, where If UPLO = 'U': E(i) = D(i-1,i),i=2:N, E(1) not referenced; If UPLO = 'L': E(i) = D(i+1,i),i=1:N-1, E(N) not referenced. NOTE: For 1-by-1 diagonal block D(k), where 1 <= k <= N, the element E(k) is not referenced in both UPLO = 'U' or UPLO = 'L' cases.

### IPIV (in)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D as determined by CHETRF_RK or CHETRF_BK.

### ANORM (in)

ANORM is REAL The 1-norm of the original matrix A.

### RCOND (out)

RCOND is REAL The reciprocal of the condition number of the matrix A, computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an estimate of the 1-norm of inv(A) computed in this routine.

### WORK (out)

WORK is COMPLEX array, dimension (2*N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

