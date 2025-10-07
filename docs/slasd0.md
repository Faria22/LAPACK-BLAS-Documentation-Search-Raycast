# SLASD0

## Function Signature

```fortran
SLASD0(N, SQRE, D, E, U, LDU, VT, LDVT, SMLSIZ, IWORK,
*                          WORK, INFO)
```

## Description


 Using a divide and conquer approach, SLASD0 computes the singular
 value decomposition (SVD) of a real upper bidiagonal N-by-M
 matrix B with diagonal D and offdiagonal E, where M = N + SQRE.
 The algorithm computes orthogonal matrices U and VT such that
 B = U * S * VT. The singular values S are overwritten on D.

 A related subroutine, SLASDA, computes only the singular values,
 and optionally, the singular vectors in compact form.

## Parameters

### N (in)

N is INTEGER On entry, the row dimension of the upper bidiagonal matrix. This is also the dimension of the main diagonal array D.

### SQRE (in)

SQRE is INTEGER Specifies the column dimension of the bidiagonal matrix. = 0: The bidiagonal matrix has column dimension M = N; = 1: The bidiagonal matrix has column dimension M = N+1;

### D (in,out)

D is REAL array, dimension (N) On entry D contains the main diagonal of the bidiagonal matrix. On exit D, if INFO = 0, contains its singular values.

### E (in,out)

E is REAL array, dimension (M-1) Contains the subdiagonal entries of the bidiagonal matrix. On exit, E has been destroyed.

### U (in,out)

U is REAL array, dimension (LDU, N) On exit, U contains the left singular vectors, if U passed in as (N, N) Identity.

### LDU (in)

LDU is INTEGER On entry, leading dimension of U.

### VT (in,out)

VT is REAL array, dimension (LDVT, M) On exit, VT**T contains the right singular vectors, if VT passed in as (M, M) Identity.

### LDVT (in)

LDVT is INTEGER On entry, leading dimension of VT.

### SMLSIZ (in)

SMLSIZ is INTEGER On entry, maximum size of the subproblems at the bottom of the computation tree.

### IWORK (out)

IWORK is INTEGER array, dimension (8*N)

### WORK (out)

WORK is REAL array, dimension (3*M**2+2*M)

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value. > 0: if INFO = 1, a singular value did not converge

