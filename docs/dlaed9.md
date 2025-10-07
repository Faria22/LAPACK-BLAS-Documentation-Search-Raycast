# DLAED9

## Function Signature

```fortran
DLAED9(K, KSTART, KSTOP, N, D, Q, LDQ, RHO, DLAMBDA,
*                          W, S, LDS, INFO)
```

## Description


 DLAED9 finds the roots of the secular equation, as defined by the
 values in D, Z, and RHO, between KSTART and KSTOP.  It makes the
 appropriate calls to DLAED4 and then stores the new matrix of
 eigenvectors for use in calculating the next level of Z vectors.

## Parameters

### K (in)

K is INTEGER The number of terms in the rational function to be solved by DLAED4. K >= 0.

### KSTART (in)

KSTART is INTEGER

### KSTOP (in)

KSTOP is INTEGER The updated eigenvalues Lambda(I), KSTART <= I <= KSTOP are to be computed. 1 <= KSTART <= KSTOP <= K.

### N (in)

N is INTEGER The number of rows and columns in the Q matrix. N >= K (delation may result in N > K).

### D (out)

D is DOUBLE PRECISION array, dimension (N) D(I) contains the updated eigenvalues for KSTART <= I <= KSTOP.

### Q (out)

Q is DOUBLE PRECISION array, dimension (LDQ,N)

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= max( 1, N ).

### RHO (in)

RHO is DOUBLE PRECISION The value of the parameter in the rank one update equation. RHO >= 0 required.

### DLAMBDA (in)

DLAMBDA is DOUBLE PRECISION array, dimension (K) The first K elements of this array contain the old roots of the deflated updating problem. These are the poles of the secular equation.

### W (in)

W is DOUBLE PRECISION array, dimension (K) The first K elements of this array contain the components of the deflation-adjusted updating vector.

### S (out)

S is DOUBLE PRECISION array, dimension (LDS, K) Will contain the eigenvectors of the repaired matrix which will be stored for subsequent Z vector calculation and multiplied by the previously accumulated eigenvectors to update the system.

### LDS (in)

LDS is INTEGER The leading dimension of S. LDS >= max( 1, K ).

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value. > 0: if INFO = 1, an eigenvalue did not converge

