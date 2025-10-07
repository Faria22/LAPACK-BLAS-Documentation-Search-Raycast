# ZSTEIN

## Function Signature

```fortran
ZSTEIN(N, D, E, M, W, IBLOCK, ISPLIT, Z, LDZ, WORK,
*                          IWORK, IFAIL, INFO)
```

## Description


 ZSTEIN computes the eigenvectors of a real symmetric tridiagonal
 matrix T corresponding to specified eigenvalues, using inverse
 iteration.

 The maximum number of iterations allowed for each eigenvector is
 specified by an internal parameter MAXITS (currently set to 5).

 Although the eigenvectors are real, they are stored in a complex
 array, which may be passed to ZUNMTR or ZUPMTR for back
 transformation to the eigenvectors of a complex Hermitian matrix
 which was reduced to tridiagonal form.


## Parameters

### N (in)

N is INTEGER The order of the matrix. N >= 0.

### D (in)

D is DOUBLE PRECISION array, dimension (N) The n diagonal elements of the tridiagonal matrix T.

### E (in)

E is DOUBLE PRECISION array, dimension (N-1) The (n-1) subdiagonal elements of the tridiagonal matrix T, stored in elements 1 to N-1.

### M (in)

M is INTEGER The number of eigenvectors to be found. 0 <= M <= N.

### W (in)

W is DOUBLE PRECISION array, dimension (N) The first M elements of W contain the eigenvalues for which eigenvectors are to be computed. The eigenvalues should be grouped by split-off block and ordered from smallest to largest within the block. ( The output array W from DSTEBZ with ORDER = 'B' is expected here. )

### IBLOCK (in)

IBLOCK is INTEGER array, dimension (N) The submatrix indices associated with the corresponding eigenvalues in W; IBLOCK(i)=1 if eigenvalue W(i) belongs to the first submatrix from the top, =2 if W(i) belongs to the second submatrix, etc. ( The output array IBLOCK from DSTEBZ is expected here. )

### ISPLIT (in)

ISPLIT is INTEGER array, dimension (N) The splitting points, at which T breaks up into submatrices. The first submatrix consists of rows/columns 1 to ISPLIT( 1 ), the second of rows/columns ISPLIT( 1 )+1 through ISPLIT( 2 ), etc. ( The output array ISPLIT from DSTEBZ is expected here. )

### Z (out)

Z is COMPLEX*16 array, dimension (LDZ, M) The computed eigenvectors. The eigenvector associated with the eigenvalue W(i) is stored in the i-th column of Z. Any vector which fails to converge is set to its current iterate after MAXITS iterations. The imaginary parts of the eigenvectors are set to zero.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= max(1,N).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (5*N)

### IWORK (out)

IWORK is INTEGER array, dimension (N)

### IFAIL (out)

IFAIL is INTEGER array, dimension (M) On normal exit, all elements of IFAIL are zero. If one or more eigenvectors fail to converge after MAXITS iterations, then their indices are stored in array IFAIL.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, then i eigenvectors failed to converge in MAXITS iterations. Their indices are stored in array IFAIL.

