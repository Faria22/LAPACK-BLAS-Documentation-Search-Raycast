# SLASD3

## Function Signature

```fortran
SLASD3(NL, NR, SQRE, K, D, Q, LDQ, DSIGMA, U, LDU, U2,
*                          LDU2, VT, LDVT, VT2, LDVT2, IDXC, CTOT, Z,
*                          INFO)
```

## Description


 SLASD3 finds all the square roots of the roots of the secular
 equation, as defined by the values in D and Z.  It makes the
 appropriate calls to SLASD4 and then updates the singular
 vectors by matrix multiplication.

 SLASD3 is called from SLASD1.

## Parameters

### NL (in)

NL is INTEGER The row dimension of the upper block. NL >= 1.

### NR (in)

NR is INTEGER The row dimension of the lower block. NR >= 1.

### SQRE (in)

SQRE is INTEGER = 0: the lower block is an NR-by-NR square matrix. = 1: the lower block is an NR-by-(NR+1) rectangular matrix. The bidiagonal matrix has N = NL + NR + 1 rows and M = N + SQRE >= N columns.

### K (in)

K is INTEGER The size of the secular equation, 1 =< K = < N.

### D (out)

D is REAL array, dimension(K) On exit the square roots of the roots of the secular equation, in ascending order.

### Q (out)

Q is REAL array, dimension (LDQ,K)

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= K.

### DSIGMA (in)

DSIGMA is REAL array, dimension(K) The first K elements of this array contain the old roots of the deflated updating problem. These are the poles of the secular equation.

### U (out)

U is REAL array, dimension (LDU, N) The last N - K columns of this matrix contain the deflated left singular vectors.

### LDU (in)

LDU is INTEGER The leading dimension of the array U. LDU >= N.

### U2 (in)

U2 is REAL array, dimension (LDU2, N) The first K columns of this matrix contain the non-deflated left singular vectors for the split problem.

### LDU2 (in)

LDU2 is INTEGER The leading dimension of the array U2. LDU2 >= N.

### VT (out)

VT is REAL array, dimension (LDVT, M) The last M - K columns of VT**T contain the deflated right singular vectors.

### LDVT (in)

LDVT is INTEGER The leading dimension of the array VT. LDVT >= N.

### VT2 (in,out)

VT2 is REAL array, dimension (LDVT2, N) The first K columns of VT2**T contain the non-deflated right singular vectors for the split problem.

### LDVT2 (in)

LDVT2 is INTEGER The leading dimension of the array VT2. LDVT2 >= N.

### IDXC (in)

IDXC is INTEGER array, dimension (N) The permutation used to arrange the columns of U (and rows of VT) into three groups: the first group contains non-zero entries only at and above (or before) NL +1; the second contains non-zero entries only at and below (or after) NL+2; and the third is dense. The first column of U and the row of VT are treated separately, however. The rows of the singular vectors found by SLASD4 must be likewise permuted before the matrix multiplies can take place.

### CTOT (in)

CTOT is INTEGER array, dimension (4) A count of the total number of the various types of columns in U (or rows in VT), as described in IDXC. The fourth column type is any column which has been deflated.

### Z (in,out)

Z is REAL array, dimension (K) The first K elements of this array contain the components of the deflation-adjusted updating row vector.

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value. > 0: if INFO = 1, a singular value did not converge

