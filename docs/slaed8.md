# SLAED8

## Function Signature

```fortran
SLAED8(ICOMPQ, K, N, QSIZ, D, Q, LDQ, INDXQ, RHO,
*                          CUTPNT, Z, DLAMBDA, Q2, LDQ2, W, PERM, GIVPTR,
*                          GIVCOL, GIVNUM, INDXP, INDX, INFO)
```

## Description


 SLAED8 merges the two sets of eigenvalues together into a single
 sorted set.  Then it tries to deflate the size of the problem.
 There are two ways in which deflation can occur:  when two or more
 eigenvalues are close together or if there is a tiny element in the
 Z vector.  For each such occurrence the order of the related secular
 equation problem is reduced by one.

## Parameters

### ICOMPQ (in)

ICOMPQ is INTEGER = 0: Compute eigenvalues only. = 1: Compute eigenvectors of original dense symmetric matrix also. On entry, Q contains the orthogonal matrix used to reduce the original matrix to tridiagonal form.

### K (out)

K is INTEGER The number of non-deflated eigenvalues, and the order of the related secular equation.

### N (in)

N is INTEGER The dimension of the symmetric tridiagonal matrix. N >= 0.

### QSIZ (in)

QSIZ is INTEGER The dimension of the orthogonal matrix used to reduce the full matrix to tridiagonal form. QSIZ >= N if ICOMPQ = 1.

### D (in,out)

D is REAL array, dimension (N) On entry, the eigenvalues of the two submatrices to be combined. On exit, the trailing (N-K) updated eigenvalues (those which were deflated) sorted into increasing order.

### Q (in,out)

Q is REAL array, dimension (LDQ,N) If ICOMPQ = 0, Q is not referenced. Otherwise, on entry, Q contains the eigenvectors of the partially solved system which has been previously updated in matrix multiplies with other partially solved eigensystems. On exit, Q contains the trailing (N-K) updated eigenvectors (those which were deflated) in its last N-K columns.

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= max(1,N).

### INDXQ (in)

INDXQ is INTEGER array, dimension (N) The permutation which separately sorts the two sub-problems in D into ascending order. Note that elements in the second half of this permutation must first have CUTPNT added to their values in order to be accurate.

### RHO (in,out)

RHO is REAL On entry, the off-diagonal element associated with the rank-1 cut which originally split the two submatrices which are now being recombined. On exit, RHO has been modified to the value required by SLAED3.

### CUTPNT (in)

CUTPNT is INTEGER The location of the last eigenvalue in the leading sub-matrix. min(1,N) <= CUTPNT <= N.

### Z (in)

Z is REAL array, dimension (N) On entry, Z contains the updating vector (the last row of the first sub-eigenvector matrix and the first row of the second sub-eigenvector matrix). On exit, the contents of Z are destroyed by the updating process.

### DLAMBDA (out)

DLAMBDA is REAL array, dimension (N) A copy of the first K eigenvalues which will be used by SLAED3 to form the secular equation.

### Q2 (out)

Q2 is REAL array, dimension (LDQ2,N) If ICOMPQ = 0, Q2 is not referenced. Otherwise, a copy of the first K eigenvectors which will be used by SLAED7 in a matrix multiply (SGEMM) to update the new eigenvectors.

### LDQ2 (in)

LDQ2 is INTEGER The leading dimension of the array Q2. LDQ2 >= max(1,N).

### W (out)

W is REAL array, dimension (N) The first k values of the final deflation-altered z-vector and will be passed to SLAED3.

### PERM (out)

PERM is INTEGER array, dimension (N) The permutations (from deflation and sorting) to be applied to each eigenblock.

### GIVPTR (out)

GIVPTR is INTEGER The number of Givens rotations which took place in this subproblem.

### GIVCOL (out)

GIVCOL is INTEGER array, dimension (2, N) Each pair of numbers indicates a pair of columns to take place in a Givens rotation.

### GIVNUM (out)

GIVNUM is REAL array, dimension (2, N) Each number indicates the S value to be used in the corresponding Givens rotation.

### INDXP (out)

INDXP is INTEGER array, dimension (N) The permutation used to place deflated values of D at the end of the array. INDXP(1:K) points to the nondeflated D-values and INDXP(K+1:N) points to the deflated eigenvalues.

### INDX (out)

INDX is INTEGER array, dimension (N) The permutation used to sort the contents of D into ascending order.

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

