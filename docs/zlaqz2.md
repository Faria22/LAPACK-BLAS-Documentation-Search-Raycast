# ZLAQZ2

## Function Signature

```fortran
ZLAQZ2(ILSCHUR, ILQ, ILZ, N, ILO, IHI, NW, A, LDA, B,
*     $    LDB, Q, LDQ, Z, LDZ, NS, ND, ALPHA, BETA, QC, LDQC, ZC, LDZC,
*     $    WORK, LWORK, RWORK, REC, INFO)
```

## Description


 ZLAQZ2 performs AED

## Parameters

### ILSCHUR (in)

ILSCHUR is LOGICAL Determines whether or not to update the full Schur form

### ILQ (in)

ILQ is LOGICAL Determines whether or not to update the matrix Q

### ILZ (in)

ILZ is LOGICAL Determines whether or not to update the matrix Z

### N (in)

N is INTEGER The order of the matrices A, B, Q, and Z. N >= 0.

### ILO (in)

ILO is INTEGER

### IHI (in)

IHI is INTEGER ILO and IHI mark the rows and columns of (A,B) which are to be normalized

### NW (in)

NW is INTEGER The desired size of the deflation window.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA, N)

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max( 1, N ).

### B (in,out)

B is COMPLEX*16 array, dimension (LDB, N)

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max( 1, N ).

### Q (in,out)

Q is COMPLEX*16 array, dimension (LDQ, N)

### LDQ (in)

LDQ is INTEGER

### Z (in,out)

Z is COMPLEX*16 array, dimension (LDZ, N)

### LDZ (in)

LDZ is INTEGER

### NS (out)

NS is INTEGER The number of unconverged eigenvalues available to use as shifts.

### ND (out)

ND is INTEGER The number of converged eigenvalues found.

### ALPHA (out)

ALPHA is COMPLEX*16 array, dimension (N) Each scalar alpha defining an eigenvalue of GNEP.

### BETA (out)

BETA is COMPLEX*16 array, dimension (N) The scalars beta that define the eigenvalues of GNEP. Together, the quantities alpha = ALPHA(j) and beta = BETA(j) represent the j-th eigenvalue of the matrix pair (A,B), in one of the forms lambda = alpha/beta or mu = beta/alpha. Since either lambda or mu may overflow, they should not, in general, be computed.

### QC (in,out)

QC is COMPLEX*16 array, dimension (LDQC, NW)

### LDQC (in)

LDQC is INTEGER

### ZC (in,out)

ZC is COMPLEX*16 array, dimension (LDZC, NW)

### LDZC (in)

LDZ is INTEGER

### WORK (out)

WORK is COMPLEX*16 array, dimension (MAX(1,LWORK)) On exit, if INFO >= 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= max(1,N). If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (N)

### REC (in)

REC is INTEGER REC indicates the current recursion level. Should be set to 0 on first call.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

