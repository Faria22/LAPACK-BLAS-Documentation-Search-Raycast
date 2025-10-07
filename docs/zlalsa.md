# ZLALSA

## Function Signature

```fortran
ZLALSA(ICOMPQ, SMLSIZ, N, NRHS, B, LDB, BX, LDBX, U,
*                          LDU, VT, K, DIFL, DIFR, Z, POLES, GIVPTR,
*                          GIVCOL, LDGCOL, PERM, GIVNUM, C, S, RWORK,
*                          IWORK, INFO)
```

## Description


 ZLALSA is an intermediate step in solving the least squares problem
 by computing the SVD of the coefficient matrix in compact form (The
 singular vectors are computed as products of simple orthogonal
 matrices.).

 If ICOMPQ = 0, ZLALSA applies the inverse of the left singular vector
 matrix of an upper bidiagonal matrix to the right hand side; and if
 ICOMPQ = 1, ZLALSA applies the right singular vector matrix to the
 right hand side. The singular vector matrices were generated in
 compact form by ZLALSA.

## Parameters

### ICOMPQ (in)

ICOMPQ is INTEGER Specifies whether the left or the right singular vector matrix is involved. = 0: Left singular vector matrix = 1: Right singular vector matrix

### SMLSIZ (in)

SMLSIZ is INTEGER The maximum size of the subproblems at the bottom of the computation tree.

### N (in)

N is INTEGER The row and column dimensions of the upper bidiagonal matrix.

### NRHS (in)

NRHS is INTEGER The number of columns of B and BX. NRHS must be at least 1.

### B (in,out)

B is COMPLEX*16 array, dimension ( LDB, NRHS ) On input, B contains the right hand sides of the least squares problem in rows 1 through M. On output, B contains the solution X in rows 1 through N.

### LDB (in)

LDB is INTEGER The leading dimension of B in the calling subprogram. LDB must be at least max(1,MAX( M, N ) ).

### BX (out)

BX is COMPLEX*16 array, dimension ( LDBX, NRHS ) On exit, the result of applying the left or right singular vector matrix to B.

### LDBX (in)

LDBX is INTEGER The leading dimension of BX.

### U (in)

U is DOUBLE PRECISION array, dimension ( LDU, SMLSIZ ). On entry, U contains the left singular vector matrices of all subproblems at the bottom level.

### LDU (in)

LDU is INTEGER, LDU = > N. The leading dimension of arrays U, VT, DIFL, DIFR, POLES, GIVNUM, and Z.

### VT (in)

VT is DOUBLE PRECISION array, dimension ( LDU, SMLSIZ+1 ). On entry, VT**H contains the right singular vector matrices of all subproblems at the bottom level.

### K (in)

K is INTEGER array, dimension ( N ).

### DIFL (in)

DIFL is DOUBLE PRECISION array, dimension ( LDU, NLVL ). where NLVL = INT(log_2 (N/(SMLSIZ+1))) + 1.

### DIFR (in)

DIFR is DOUBLE PRECISION array, dimension ( LDU, 2 * NLVL ). On entry, DIFL(*, I) and DIFR(*, 2 * I -1) record distances between singular values on the I-th level and singular values on the (I -1)-th level, and DIFR(*, 2 * I) record the normalizing factors of the right singular vectors matrices of subproblems on I-th level.

### Z (in)

Z is DOUBLE PRECISION array, dimension ( LDU, NLVL ). On entry, Z(1, I) contains the components of the deflation- adjusted updating row vector for subproblems on the I-th level.

### POLES (in)

POLES is DOUBLE PRECISION array, dimension ( LDU, 2 * NLVL ). On entry, POLES(*, 2 * I -1: 2 * I) contains the new and old singular values involved in the secular equations on the I-th level.

### GIVPTR (in)

GIVPTR is INTEGER array, dimension ( N ). On entry, GIVPTR( I ) records the number of Givens rotations performed on the I-th problem on the computation tree.

### GIVCOL (in)

GIVCOL is INTEGER array, dimension ( LDGCOL, 2 * NLVL ). On entry, for each I, GIVCOL(*, 2 * I - 1: 2 * I) records the locations of Givens rotations performed on the I-th level on the computation tree.

### LDGCOL (in)

LDGCOL is INTEGER, LDGCOL = > N. The leading dimension of arrays GIVCOL and PERM.

### PERM (in)

PERM is INTEGER array, dimension ( LDGCOL, NLVL ). On entry, PERM(*, I) records permutations done on the I-th level of the computation tree.

### GIVNUM (in)

GIVNUM is DOUBLE PRECISION array, dimension ( LDU, 2 * NLVL ). On entry, GIVNUM(*, 2 *I -1 : 2 * I) records the C- and S- values of Givens rotations performed on the I-th level on the computation tree.

### C (in)

C is DOUBLE PRECISION array, dimension ( N ). On entry, if the I-th subproblem is not square, C( I ) contains the C-value of a Givens rotation related to the right null space of the I-th subproblem.

### S (in)

S is DOUBLE PRECISION array, dimension ( N ). On entry, if the I-th subproblem is not square, S( I ) contains the S-value of a Givens rotation related to the right null space of the I-th subproblem.

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension at least MAX( (SMLSZ+1)*NRHS*3, N*(1+NRHS) + 2*NRHS ).

### IWORK (out)

IWORK is INTEGER array, dimension (3*N)

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

