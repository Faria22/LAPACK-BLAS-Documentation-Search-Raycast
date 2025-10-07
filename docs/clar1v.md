# CLAR1V

## Function Signature

```fortran
CLAR1V(N, B1, BN, LAMBDA, D, L, LD, LLD,
*                  PIVMIN, GAPTOL, Z, WANTNC, NEGCNT, ZTZ, MINGMA,
*                  R, ISUPPZ, NRMINV, RESID, RQCORR, WORK)
```

## Description


 CLAR1V computes the (scaled) r-th column of the inverse of
 the sumbmatrix in rows B1 through BN of the tridiagonal matrix
 L D L**T - sigma I. When sigma is close to an eigenvalue, the
 computed vector is an accurate eigenvector. Usually, r corresponds
 to the index where the eigenvector is largest in magnitude.
 The following steps accomplish this computation :
 (a) Stationary qd transform,  L D L**T - sigma I = L(+) D(+) L(+)**T,
 (b) Progressive qd transform, L D L**T - sigma I = U(-) D(-) U(-)**T,
 (c) Computation of the diagonal elements of the inverse of
     L D L**T - sigma I by combining the above transforms, and choosing
     r as the index where the diagonal of the inverse is (one of the)
     largest in magnitude.
 (d) Computation of the (scaled) r-th column of the inverse using the
     twisted factorization obtained by combining the top part of the
     the stationary and the bottom part of the progressive transform.

## Parameters

### N (in)

N is INTEGER The order of the matrix L D L**T.

### B1 (in)

B1 is INTEGER First index of the submatrix of L D L**T.

### BN (in)

BN is INTEGER Last index of the submatrix of L D L**T.

### LAMBDA (in)

LAMBDA is REAL The shift. In order to compute an accurate eigenvector, LAMBDA should be a good approximation to an eigenvalue of L D L**T.

### L (in)

L is REAL array, dimension (N-1) The (n-1) subdiagonal elements of the unit bidiagonal matrix L, in elements 1 to N-1.

### D (in)

D is REAL array, dimension (N) The n diagonal elements of the diagonal matrix D.

### LD (in)

LD is REAL array, dimension (N-1) The n-1 elements L(i)*D(i).

### LLD (in)

LLD is REAL array, dimension (N-1) The n-1 elements L(i)*L(i)*D(i).

### PIVMIN (in)

PIVMIN is REAL The minimum pivot in the Sturm sequence.

### GAPTOL (in)

GAPTOL is REAL Tolerance that indicates when eigenvector entries are negligible w.r.t. their contribution to the residual.

### Z (in,out)

Z is COMPLEX array, dimension (N) On input, all entries of Z must be set to 0. On output, Z contains the (scaled) r-th column of the inverse. The scaling is such that Z(R) equals 1.

### WANTNC (in)

WANTNC is LOGICAL Specifies whether NEGCNT has to be computed.

### NEGCNT (out)

NEGCNT is INTEGER If WANTNC is .TRUE. then NEGCNT = the number of pivots < pivmin in the matrix factorization L D L**T, and NEGCNT = -1 otherwise.

### ZTZ (out)

ZTZ is REAL The square of the 2-norm of Z.

### MINGMA (out)

MINGMA is REAL The reciprocal of the largest (in magnitude) diagonal element of the inverse of L D L**T - sigma I.

### R (in,out)

R is INTEGER The twist index for the twisted factorization used to compute Z. On input, 0 <= R <= N. If R is input as 0, R is set to the index where (L D L**T - sigma I)^{-1} is largest in magnitude. If 1 <= R <= N, R is unchanged. On output, R contains the twist index used to compute Z. Ideally, R designates the position of the maximum entry in the eigenvector.

### ISUPPZ (out)

ISUPPZ is INTEGER array, dimension (2) The support of the vector in Z, i.e., the vector Z is nonzero only in elements ISUPPZ(1) through ISUPPZ( 2 ).

### NRMINV (out)

NRMINV is REAL NRMINV = 1/SQRT( ZTZ )

### RESID (out)

RESID is REAL The residual of the FP vector. RESID = ABS( MINGMA )/SQRT( ZTZ )

### RQCORR (out)

RQCORR is REAL The Rayleigh Quotient correction to LAMBDA. RQCORR = MINGMA*TMP

### WORK (out)

WORK is REAL array, dimension (4*N)

