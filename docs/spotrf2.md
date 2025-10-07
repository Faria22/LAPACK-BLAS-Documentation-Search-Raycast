# SPOTRF2

## Function Signature

```fortran
SPOTRF2(UPLO, N, A, LDA, INFO)
```

## Description


 SPOTRF2 computes the Cholesky factorization of a real symmetric
 positive definite matrix A using the recursive algorithm.

 The factorization has the form
    A = U**T * U,  if UPLO = 'U', or
    A = L  * L**T,  if UPLO = 'L',
 where U is an upper triangular matrix and L is lower triangular.

 This is the recursive version of the algorithm. It divides
 the matrix into four submatrices:

        [  A11 | A12  ]  where A11 is n1 by n1 and A22 is n2 by n2
    A = [ -----|----- ]  with n1 = n/2
        [  A21 | A22  ]       n2 = n-n1

 The subroutine calls itself to factor A11. Update and scale A21
 or A12, update A22 then call itself to factor A22.


## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in,out)

A is REAL array, dimension (LDA,N) On entry, the symmetric matrix A. If UPLO = 'U', the leading N-by-N upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading N-by-N lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced. On exit, if INFO = 0, the factor U or L from the Cholesky factorization A = U**T*U or A = L*L**T.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, the leading principal minor of order i is not positive, and the factorization could not be completed.

