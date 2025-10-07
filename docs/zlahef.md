# ZLAHEF

## Function Signature

```fortran
ZLAHEF(UPLO, N, NB, KB, A, LDA, IPIV, W, LDW, INFO)
```

## Description


 ZLAHEF computes a partial factorization of a complex Hermitian
 matrix A using the Bunch-Kaufman diagonal pivoting method. The
 partial factorization has the form:

 A  =  ( I  U12 ) ( A11  0  ) (  I      0     )  if UPLO = 'U', or:
       ( 0  U22 ) (  0   D  ) ( U12**H U22**H )

 A  =  ( L11  0 ) (  D   0  ) ( L11**H L21**H )  if UPLO = 'L'
       ( L21  I ) (  0  A22 ) (  0      I     )

 where the order of D is at most NB. The actual order is returned in
 the argument KB, and is either NB or NB-1, or N if N <= NB.
 Note that U**H denotes the conjugate transpose of U.

 ZLAHEF is an auxiliary routine called by ZHETRF. It uses blocked code
 (calling Level 3 BLAS) to update the submatrix A11 (if UPLO = 'U') or
 A22 (if UPLO = 'L').

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the upper or lower triangular part of the Hermitian matrix A is stored: = 'U': Upper triangular = 'L': Lower triangular

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NB (in)

NB is INTEGER The maximum number of columns of the matrix A that should be factored. NB should be at least 2 to allow for 2-by-2 pivot blocks.

### KB (out)

KB is INTEGER The number of columns of A that were actually factored. KB is either NB-1 or NB, or N if N <= NB.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the Hermitian matrix A. If UPLO = 'U', the leading n-by-n upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced. If UPLO = 'L', the leading n-by-n lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced. On exit, A contains details of the partial factorization.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### IPIV (out)

IPIV is INTEGER array, dimension (N) Details of the interchanges and the block structure of D. If UPLO = 'U': Only the last KB elements of IPIV are set. If IPIV(k) > 0, then rows and columns k and IPIV(k) were interchanged and D(k,k) is a 1-by-1 diagonal block. If IPIV(k) = IPIV(k-1) < 0, then rows and columns k-1 and -IPIV(k) were interchanged and D(k-1:k,k-1:k) is a 2-by-2 diagonal block. If UPLO = 'L': Only the first KB elements of IPIV are set. If IPIV(k) > 0, then rows and columns k and IPIV(k) were interchanged and D(k,k) is a 1-by-1 diagonal block. If IPIV(k) = IPIV(k+1) < 0, then rows and columns k+1 and -IPIV(k) were interchanged and D(k:k+1,k:k+1) is a 2-by-2 diagonal block.

### W (out)

W is COMPLEX*16 array, dimension (LDW,NB)

### LDW (in)

LDW is INTEGER The leading dimension of the array W. LDW >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit > 0: if INFO = k, D(k,k) is exactly zero. The factorization has been completed, but the block diagonal matrix D is exactly singular.

