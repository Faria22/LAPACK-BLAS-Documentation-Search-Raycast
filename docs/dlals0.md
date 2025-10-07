# DLALS0

## Function Signature

```fortran
DLALS0(ICOMPQ, NL, NR, SQRE, NRHS, B, LDB, BX, LDBX,
*                          PERM, GIVPTR, GIVCOL, LDGCOL, GIVNUM, LDGNUM,
*                          POLES, DIFL, DIFR, Z, K, C, S, WORK, INFO)
```

## Description


 DLALS0 applies back the multiplying factors of either the left or the
 right singular vector matrix of a diagonal matrix appended by a row
 to the right hand side matrix B in solving the least squares problem
 using the divide-and-conquer SVD approach.

 For the left singular vector matrix, three types of orthogonal
 matrices are involved:

 (1L) Givens rotations: the number of such rotations is GIVPTR; the
      pairs of columns/rows they were applied to are stored in GIVCOL;
      and the C- and S-values of these rotations are stored in GIVNUM.

 (2L) Permutation. The (NL+1)-st row of B is to be moved to the first
      row, and for J=2:N, PERM(J)-th row of B is to be moved to the
      J-th row.

 (3L) The left singular vector matrix of the remaining matrix.

 For the right singular vector matrix, four types of orthogonal
 matrices are involved:

 (1R) The right singular vector matrix of the remaining matrix.

 (2R) If SQRE = 1, one extra Givens rotation to generate the right
      null space.

 (3R) The inverse transformation of (2L).

 (4R) The inverse transformation of (1L).

## Parameters

### ICOMPQ (in)

ICOMPQ is INTEGER Specifies whether singular vectors are to be computed in factored form: = 0: Left singular vector matrix. = 1: Right singular vector matrix.

### NL (in)

NL is INTEGER The row dimension of the upper block. NL >= 1.

### NR (in)

NR is INTEGER The row dimension of the lower block. NR >= 1.

### SQRE (in)

SQRE is INTEGER = 0: the lower block is an NR-by-NR square matrix. = 1: the lower block is an NR-by-(NR+1) rectangular matrix. The bidiagonal matrix has row dimension N = NL + NR + 1, and column dimension M = N + SQRE.

### NRHS (in)

NRHS is INTEGER The number of columns of B and BX. NRHS must be at least 1.

### B (in,out)

B is DOUBLE PRECISION array, dimension ( LDB, NRHS ) On input, B contains the right hand sides of the least squares problem in rows 1 through M. On output, B contains the solution X in rows 1 through N.

### LDB (in)

LDB is INTEGER The leading dimension of B. LDB must be at least max(1,MAX( M, N ) ).

### BX (out)

BX is DOUBLE PRECISION array, dimension ( LDBX, NRHS )

### LDBX (in)

LDBX is INTEGER The leading dimension of BX.

### PERM (in)

PERM is INTEGER array, dimension ( N ) The permutations (from deflation and sorting) applied to the two blocks.

### GIVPTR (in)

GIVPTR is INTEGER The number of Givens rotations which took place in this subproblem.

### GIVCOL (in)

GIVCOL is INTEGER array, dimension ( LDGCOL, 2 ) Each pair of numbers indicates a pair of rows/columns involved in a Givens rotation.

### LDGCOL (in)

LDGCOL is INTEGER The leading dimension of GIVCOL, must be at least N.

### GIVNUM (in)

GIVNUM is DOUBLE PRECISION array, dimension ( LDGNUM, 2 ) Each number indicates the C or S value used in the corresponding Givens rotation.

### LDGNUM (in)

LDGNUM is INTEGER The leading dimension of arrays DIFR, POLES and GIVNUM, must be at least K.

### POLES (in)

POLES is DOUBLE PRECISION array, dimension ( LDGNUM, 2 ) On entry, POLES(1:K, 1) contains the new singular values obtained from solving the secular equation, and POLES(1:K, 2) is an array containing the poles in the secular equation.

### DIFL (in)

DIFL is DOUBLE PRECISION array, dimension ( K ). On entry, DIFL(I) is the distance between I-th updated (undeflated) singular value and the I-th (undeflated) old singular value.

### DIFR (in)

DIFR is DOUBLE PRECISION array, dimension ( LDGNUM, 2 ). On entry, DIFR(I, 1) contains the distances between I-th updated (undeflated) singular value and the I+1-th (undeflated) old singular value. And DIFR(I, 2) is the normalizing factor for the I-th right singular vector.

### Z (in)

Z is DOUBLE PRECISION array, dimension ( K ) Contain the components of the deflation-adjusted updating row vector.

### K (in)

K is INTEGER Contains the dimension of the non-deflated matrix, This is the order of the related secular equation. 1 <= K <=N.

### C (in)

C is DOUBLE PRECISION C contains garbage if SQRE =0 and the C-value of a Givens rotation related to the right null space if SQRE = 1.

### S (in)

S is DOUBLE PRECISION S contains garbage if SQRE =0 and the S-value of a Givens rotation related to the right null space if SQRE = 1.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension ( K )

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

