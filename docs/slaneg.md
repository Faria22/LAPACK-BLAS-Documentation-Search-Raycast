# SLANEG

## Function Signature

```fortran
SLANEG(N, D, LLD, SIGMA, PIVMIN, R)
```

## Description


 SLANEG computes the Sturm count, the number of negative pivots
 encountered while factoring tridiagonal T - sigma I = L D L^T.
 This implementation works directly on the factors without forming
 the tridiagonal matrix T.  The Sturm count is also the number of
 eigenvalues of T less than sigma.

 This routine is called from SLARRB.

 The current routine does not use the PIVMIN parameter but rather
 requires IEEE-754 propagation of Infinities and NaNs.  This
 routine also has no input range restrictions but does require
 default exception handling such that x/0 produces Inf when x is
 non-zero, and Inf/Inf produces NaN.  For more information, see:

   Marques, Riedy, and Voemel, "Benefits of IEEE-754 Features in
   Modern Symmetric Tridiagonal Eigensolvers," SIAM Journal on
   Scientific Computing, v28, n5, 2006.  DOI 10.1137/050641624
   (Tech report version in LAWN 172 with the same title.)

## Parameters

### N (in)

N is INTEGER The order of the matrix.

### D (in)

D is REAL array, dimension (N) The N diagonal elements of the diagonal matrix D.

### LLD (in)

LLD is REAL array, dimension (N-1) The (N-1) elements L(i)*L(i)*D(i).

### SIGMA (in)

SIGMA is REAL Shift amount in T - sigma I = L D L^T.

### PIVMIN (in)

PIVMIN is REAL The minimum pivot in the Sturm sequence. May be used when zero pivots are encountered on non-IEEE-754 architectures.

### R (in)

R is INTEGER The twist index for the twisted factorization that is used for the negcount.

