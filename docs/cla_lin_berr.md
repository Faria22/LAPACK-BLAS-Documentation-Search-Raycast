# CLA_LIN_BERR

## Function Signature

```fortran
CLA_LIN_BERR(N, NZ, NRHS, RES, AYB, BERR)
```

## Description


    CLA_LIN_BERR computes componentwise relative backward error from
    the formula
        max(i) ( abs(R(i)) / ( abs(op(A_s))*abs(Y) + abs(B_s) )(i) )
    where abs(Z) is the componentwise absolute value of the matrix
    or vector Z.

## Parameters

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### NZ (in)

NZ is INTEGER We add (NZ+1)*SLAMCH( 'Safe minimum' ) to R(i) in the numerator to guard against spuriously zero residuals. Default value is N.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrices AYB, RES, and BERR. NRHS >= 0.

### RES (in)

RES is COMPLEX array, dimension (N,NRHS) The residual matrix, i.e., the matrix R in the relative backward error formula above.

### AYB (in)

AYB is REAL array, dimension (N, NRHS) The denominator in the relative backward error formula above, i.e., the matrix abs(op(A_s))*abs(Y) + abs(B_s). The matrices A, Y, and B are from iterative refinement (see cla_gerfsx_extended.f).

### BERR (out)

BERR is REAL array, dimension (NRHS) The componentwise relative backward error from the formula above.

