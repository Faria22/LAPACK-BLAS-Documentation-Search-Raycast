# DLARMM

## Function Signature

```fortran
DLARMM(ANORM, BNORM, CNORM)
```

## Description


 DLARMM returns a factor s in (0, 1] such that the linear updates

    (s * C) - A * (s * B)  and  (s * C) - (s * A) * B

 cannot overflow, where A, B, and C are matrices of conforming
 dimensions.

 This is an auxiliary routine so there is no argument checking.

## Parameters

### ANORM (in)

ANORM is DOUBLE PRECISION The infinity norm of A. ANORM >= 0. The number of rows of the matrix A. M >= 0.

### BNORM (in)

BNORM is DOUBLE PRECISION The infinity norm of B. BNORM >= 0.

### CNORM (in)

CNORM is DOUBLE PRECISION The infinity norm of C. CNORM >= 0.

