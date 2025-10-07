# DLASD7

## Function Signature

```fortran
DLASD7(ICOMPQ, NL, NR, SQRE, K, D, Z, ZW, VF, VFW, VL,
*                          VLW, ALPHA, BETA, DSIGMA, IDX, IDXP, IDXQ,
*                          PERM, GIVPTR, GIVCOL, LDGCOL, GIVNUM, LDGNUM,
*                          C, S, INFO)
```

## Description


 DLASD7 merges the two sets of singular values together into a single
 sorted set. Then it tries to deflate the size of the problem. There
 are two ways in which deflation can occur:  when two or more singular
 values are close together or if there is a tiny entry in the Z
 vector. For each such occurrence the order of the related
 secular equation problem is reduced by one.

 DLASD7 is called from DLASD6.

## Parameters

### ICOMPQ (in)

ICOMPQ is INTEGER Specifies whether singular vectors are to be computed in compact form, as follows: = 0: Compute singular values only. = 1: Compute singular vectors of upper bidiagonal matrix in compact form.

### NL (in)

NL is INTEGER The row dimension of the upper block. NL >= 1.

### NR (in)

NR is INTEGER The row dimension of the lower block. NR >= 1.

### SQRE (in)

SQRE is INTEGER = 0: the lower block is an NR-by-NR square matrix. = 1: the lower block is an NR-by-(NR+1) rectangular matrix. The bidiagonal matrix has N = NL + NR + 1 rows and M = N + SQRE >= N columns.

### K (out)

K is INTEGER Contains the dimension of the non-deflated matrix, this is the order of the related secular equation. 1 <= K <=N.

### D (in,out)

D is DOUBLE PRECISION array, dimension ( N ) On entry D contains the singular values of the two submatrices to be combined. On exit D contains the trailing (N-K) updated singular values (those which were deflated) sorted into increasing order.

### Z (out)

Z is DOUBLE PRECISION array, dimension ( M ) On exit Z contains the updating row vector in the secular equation.

### ZW (out)

ZW is DOUBLE PRECISION array, dimension ( M ) Workspace for Z.

### VF (in,out)

VF is DOUBLE PRECISION array, dimension ( M ) On entry, VF(1:NL+1) contains the first components of all right singular vectors of the upper block; and VF(NL+2:M) contains the first components of all right singular vectors of the lower block. On exit, VF contains the first components of all right singular vectors of the bidiagonal matrix.

### VFW (out)

VFW is DOUBLE PRECISION array, dimension ( M ) Workspace for VF.

### VL (in,out)

VL is DOUBLE PRECISION array, dimension ( M ) On entry, VL(1:NL+1) contains the last components of all right singular vectors of the upper block; and VL(NL+2:M) contains the last components of all right singular vectors of the lower block. On exit, VL contains the last components of all right singular vectors of the bidiagonal matrix.

### VLW (out)

VLW is DOUBLE PRECISION array, dimension ( M ) Workspace for VL.

### ALPHA (in)

ALPHA is DOUBLE PRECISION Contains the diagonal element associated with the added row.

### BETA (in)

BETA is DOUBLE PRECISION Contains the off-diagonal element associated with the added row.

### DSIGMA (out)

DSIGMA is DOUBLE PRECISION array, dimension ( N ) Contains a copy of the diagonal elements (K-1 singular values and one zero) in the secular equation.

### IDX (out)

IDX is INTEGER array, dimension ( N ) This will contain the permutation used to sort the contents of D into ascending order.

### IDXP (out)

IDXP is INTEGER array, dimension ( N ) This will contain the permutation used to place deflated values of D at the end of the array. On output IDXP(2:K) points to the nondeflated D-values and IDXP(K+1:N) points to the deflated singular values.

### IDXQ (in)

IDXQ is INTEGER array, dimension ( N ) This contains the permutation which separately sorts the two sub-problems in D into ascending order. Note that entries in the first half of this permutation must first be moved one position backward; and entries in the second half must first have NL+1 added to their values.

### PERM (out)

PERM is INTEGER array, dimension ( N ) The permutations (from deflation and sorting) to be applied to each singular block. Not referenced if ICOMPQ = 0.

### GIVPTR (out)

GIVPTR is INTEGER The number of Givens rotations which took place in this subproblem. Not referenced if ICOMPQ = 0.

### GIVCOL (out)

GIVCOL is INTEGER array, dimension ( LDGCOL, 2 ) Each pair of numbers indicates a pair of columns to take place in a Givens rotation. Not referenced if ICOMPQ = 0.

### LDGCOL (in)

LDGCOL is INTEGER The leading dimension of GIVCOL, must be at least N.

### GIVNUM (out)

GIVNUM is DOUBLE PRECISION array, dimension ( LDGNUM, 2 ) Each number indicates the C or S value to be used in the corresponding Givens rotation. Not referenced if ICOMPQ = 0.

### LDGNUM (in)

LDGNUM is INTEGER The leading dimension of GIVNUM, must be at least N.

### C (out)

C is DOUBLE PRECISION C contains garbage if SQRE =0 and the C-value of a Givens rotation related to the right null space if SQRE = 1.

### S (out)

S is DOUBLE PRECISION S contains garbage if SQRE =0 and the S-value of a Givens rotation related to the right null space if SQRE = 1.

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

