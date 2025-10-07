# SLASDA

## Function Signature

```fortran
SLASDA(ICOMPQ, SMLSIZ, N, SQRE, D, E, U, LDU, VT, K,
*                          DIFL, DIFR, Z, POLES, GIVPTR, GIVCOL, LDGCOL,
*                          PERM, GIVNUM, C, S, WORK, IWORK, INFO)
```

## Description


 Using a divide and conquer approach, SLASDA computes the singular
 value decomposition (SVD) of a real upper bidiagonal N-by-M matrix
 B with diagonal D and offdiagonal E, where M = N + SQRE. The
 algorithm computes the singular values in the SVD B = U * S * VT.
 The orthogonal matrices U and VT are optionally computed in
 compact form.

 A related subroutine, SLASD0, computes the singular values and
 the singular vectors in explicit form.

## Parameters

### ICOMPQ (in)

ICOMPQ is INTEGER Specifies whether singular vectors are to be computed in compact form, as follows = 0: Compute singular values only. = 1: Compute singular vectors of upper bidiagonal matrix in compact form.

### SMLSIZ (in)

SMLSIZ is INTEGER The maximum size of the subproblems at the bottom of the computation tree.

### N (in)

N is INTEGER The row dimension of the upper bidiagonal matrix. This is also the dimension of the main diagonal array D.

### SQRE (in)

SQRE is INTEGER Specifies the column dimension of the bidiagonal matrix. = 0: The bidiagonal matrix has column dimension M = N; = 1: The bidiagonal matrix has column dimension M = N + 1.

### D (in,out)

D is REAL array, dimension ( N ) On entry D contains the main diagonal of the bidiagonal matrix. On exit D, if INFO = 0, contains its singular values.

### E (in)

E is REAL array, dimension ( M-1 ) Contains the subdiagonal entries of the bidiagonal matrix. On exit, E has been destroyed.

### U (out)

U is REAL array, dimension ( LDU, SMLSIZ ) if ICOMPQ = 1, and not referenced if ICOMPQ = 0. If ICOMPQ = 1, on exit, U contains the left singular vector matrices of all subproblems at the bottom level.

### LDU (in)

LDU is INTEGER, LDU = > N. The leading dimension of arrays U, VT, DIFL, DIFR, POLES, GIVNUM, and Z.

### VT (out)

VT is REAL array, dimension ( LDU, SMLSIZ+1 ) if ICOMPQ = 1, and not referenced if ICOMPQ = 0. If ICOMPQ = 1, on exit, VT**T contains the right singular vector matrices of all subproblems at the bottom level.

### K (out)

K is INTEGER array, dimension ( N ) if ICOMPQ = 1 and dimension 1 if ICOMPQ = 0. If ICOMPQ = 1, on exit, K(I) is the dimension of the I-th secular equation on the computation tree.

### DIFL (out)

DIFL is REAL array, dimension ( LDU, NLVL ), where NLVL = floor(log_2 (N/SMLSIZ))).

### DIFR (out)

DIFR is REAL array, dimension ( LDU, 2 * NLVL ) if ICOMPQ = 1 and dimension ( N ) if ICOMPQ = 0. If ICOMPQ = 1, on exit, DIFL(1:N, I) and DIFR(1:N, 2 * I - 1) record distances between singular values on the I-th level and singular values on the (I -1)-th level, and DIFR(1:N, 2 * I ) contains the normalizing factors for the right singular vector matrix. See SLASD8 for details.

### Z (out)

Z is REAL array, dimension ( LDU, NLVL ) if ICOMPQ = 1 and dimension ( N ) if ICOMPQ = 0. The first K elements of Z(1, I) contain the components of the deflation-adjusted updating row vector for subproblems on the I-th level.

### POLES (out)

POLES is REAL array, dimension ( LDU, 2 * NLVL ) if ICOMPQ = 1, and not referenced if ICOMPQ = 0. If ICOMPQ = 1, on exit, POLES(1, 2*I - 1) and POLES(1, 2*I) contain the new and old singular values involved in the secular equations on the I-th level.

### GIVPTR (out)

GIVPTR is INTEGER array, dimension ( N ) if ICOMPQ = 1, and not referenced if ICOMPQ = 0. If ICOMPQ = 1, on exit, GIVPTR( I ) records the number of Givens rotations performed on the I-th problem on the computation tree.

### GIVCOL (out)

GIVCOL is INTEGER array, dimension ( LDGCOL, 2 * NLVL ) if ICOMPQ = 1, and not referenced if ICOMPQ = 0. If ICOMPQ = 1, on exit, for each I, GIVCOL(1, 2 *I - 1) and GIVCOL(1, 2 *I) record the locations of Givens rotations performed on the I-th level on the computation tree.

### LDGCOL (in)

LDGCOL is INTEGER, LDGCOL = > N. The leading dimension of arrays GIVCOL and PERM.

### PERM (out)

PERM is INTEGER array, dimension ( LDGCOL, NLVL ) if ICOMPQ = 1, and not referenced if ICOMPQ = 0. If ICOMPQ = 1, on exit, PERM(1, I) records permutations done on the I-th level of the computation tree.

### GIVNUM (out)

GIVNUM is REAL array, dimension ( LDU, 2 * NLVL ) if ICOMPQ = 1, and not referenced if ICOMPQ = 0. If ICOMPQ = 1, on exit, for each I, GIVNUM(1, 2 *I - 1) and GIVNUM(1, 2 *I) record the C- and S- values of Givens rotations performed on the I-th level on the computation tree.

### C (out)

C is REAL array, dimension ( N ) if ICOMPQ = 1, and dimension 1 if ICOMPQ = 0. If ICOMPQ = 1 and the I-th subproblem is not square, on exit, C( I ) contains the C-value of a Givens rotation related to the right null space of the I-th subproblem.

### S (out)

S is REAL array, dimension ( N ) if ICOMPQ = 1, and dimension 1 if ICOMPQ = 0. If ICOMPQ = 1 and the I-th subproblem is not square, on exit, S( I ) contains the S-value of a Givens rotation related to the right null space of the I-th subproblem.

### WORK (out)

WORK is REAL array, dimension (6 * N + (SMLSIZ + 1)*(SMLSIZ + 1)).

### IWORK (out)

IWORK is INTEGER array, dimension (7*N).

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value. > 0: if INFO = 1, a singular value did not converge

