# SLASD8

## Function Signature

```fortran
SLASD8(ICOMPQ, K, D, Z, VF, VL, DIFL, DIFR, LDDIFR,
*                          DSIGMA, WORK, INFO)
```

## Description


 SLASD8 finds the square roots of the roots of the secular equation,
 as defined by the values in DSIGMA and Z. It makes the appropriate
 calls to SLASD4, and stores, for each  element in D, the distance
 to its two nearest poles (elements in DSIGMA). It also updates
 the arrays VF and VL, the first and last components of all the
 right singular vectors of the original bidiagonal matrix.

 SLASD8 is called from SLASD6.

## Parameters

### ICOMPQ (in)

ICOMPQ is INTEGER Specifies whether singular vectors are to be computed in factored form in the calling routine: = 0: Compute singular values only. = 1: Compute singular vectors in factored form as well.

### K (in)

K is INTEGER The number of terms in the rational function to be solved by SLASD4. K >= 1.

### D (out)

D is REAL array, dimension ( K ) On output, D contains the updated singular values.

### Z (in,out)

Z is REAL array, dimension ( K ) On entry, the first K elements of this array contain the components of the deflation-adjusted updating row vector. On exit, Z is updated.

### VF (in,out)

VF is REAL array, dimension ( K ) On entry, VF contains information passed through DBEDE8. On exit, VF contains the first K components of the first components of all right singular vectors of the bidiagonal matrix.

### VL (in,out)

VL is REAL array, dimension ( K ) On entry, VL contains information passed through DBEDE8. On exit, VL contains the first K components of the last components of all right singular vectors of the bidiagonal matrix.

### DIFL (out)

DIFL is REAL array, dimension ( K ) On exit, DIFL(I) = D(I) - DSIGMA(I).

### DIFR (out)

DIFR is REAL array, dimension ( LDDIFR, 2 ) if ICOMPQ = 1 and dimension ( K ) if ICOMPQ = 0. On exit, DIFR(I,1) = D(I) - DSIGMA(I+1), DIFR(K,1) is not defined and will not be referenced. If ICOMPQ = 1, DIFR(1:K,2) is an array containing the normalizing factors for the right singular vector matrix.

### LDDIFR (in)

LDDIFR is INTEGER The leading dimension of DIFR, must be at least K.

### DSIGMA (in)

DSIGMA is REAL array, dimension ( K ) On entry, the first K elements of this array contain the old roots of the deflated updating problem. These are the poles of the secular equation.

### WORK (out)

WORK is REAL array, dimension (3*K)

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value. > 0: if INFO = 1, a singular value did not converge

