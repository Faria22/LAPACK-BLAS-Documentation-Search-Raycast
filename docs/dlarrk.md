# DLARRK

## Function Signature

```fortran
DLARRK(N, IW, GL, GU,
*                           D, E2, PIVMIN, RELTOL, W, WERR, INFO)
```

## Description


 DLARRK computes one eigenvalue of a symmetric tridiagonal
 matrix T to suitable accuracy. This is an auxiliary code to be
 called from DSTEMR.

 To avoid overflow, the matrix must be scaled so that its
 largest element is no greater than overflow**(1/2) * underflow**(1/4) in absolute value, and for greatest
 accuracy, it should not be much smaller than that.

 See W. Kahan "Accurate Eigenvalues of a Symmetric Tridiagonal
 Matrix", Report CS41, Computer Science Dept., Stanford
 University, July 21, 1966.

## Parameters

### N (in)

N is INTEGER The order of the tridiagonal matrix T. N >= 0.

### IW (in)

IW is INTEGER The index of the eigenvalues to be returned.

### GL (in)

GL is DOUBLE PRECISION

### GU (in)

GU is DOUBLE PRECISION An upper and a lower bound on the eigenvalue.

### D (in)

D is DOUBLE PRECISION array, dimension (N) The n diagonal elements of the tridiagonal matrix T.

### E2 (in)

E2 is DOUBLE PRECISION array, dimension (N-1) The (n-1) squared off-diagonal elements of the tridiagonal matrix T.

### PIVMIN (in)

PIVMIN is DOUBLE PRECISION The minimum pivot allowed in the Sturm sequence for T.

### RELTOL (in)

RELTOL is DOUBLE PRECISION The minimum relative width of an interval. When an interval is narrower than RELTOL times the larger (in magnitude) endpoint, then it is considered to be sufficiently small, i.e., converged. Note: this should always be at least radix*machine epsilon.

### W (out)

W is DOUBLE PRECISION

### WERR (out)

WERR is DOUBLE PRECISION The error bound on the corresponding eigenvalue approximation in W.

### INFO (out)

INFO is INTEGER = 0: Eigenvalue converged = -1: Eigenvalue did NOT converge

