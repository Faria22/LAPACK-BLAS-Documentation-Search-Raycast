# DLAQZ3

## Function Signature

```fortran
DLAQZ3(ILSCHUR, ILQ, ILZ, N, ILO, IHI, NW, A, LDA, B,
*     $    LDB, Q, LDQ, Z, LDZ, NS, ND, ALPHAR, ALPHAI, BETA, QC, LDQC,
*     $    ZC, LDZC, WORK, LWORK, REC, INFO)
```

## Description


 DLAQZ3 performs AED

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

A is DOUBLE PRECISION array, dimension (LDA, N)

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max( 1, N ).

### B (in,out)

B is DOUBLE PRECISION array, dimension (LDB, N)

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max( 1, N ).

### Q (in,out)

Q is DOUBLE PRECISION array, dimension (LDQ, N)

### LDQ (in)

LDQ is INTEGER

### Z (in,out)

Z is DOUBLE PRECISION array, dimension (LDZ, N)

### LDZ (in)

LDZ is INTEGER

### NS (out)

NS is INTEGER The number of unconverged eigenvalues available to use as shifts.

### ND (out)

ND is INTEGER The number of converged eigenvalues found.

### ALPHAR (out)

ALPHAR is DOUBLE PRECISION array, dimension (N) The real parts of each scalar alpha defining an eigenvalue of GNEP.

### ALPHAI (out)

ALPHAI is DOUBLE PRECISION array, dimension (N) The imaginary parts of each scalar alpha defining an eigenvalue of GNEP. If ALPHAI(j) is zero, then the j-th eigenvalue is real; if positive, then the j-th and (j+1)-st eigenvalues are a complex conjugate pair, with ALPHAI(j+1) = -ALPHAI(j).

### BETA (out)

BETA is DOUBLE PRECISION array, dimension (N) The scalars beta that define the eigenvalues of GNEP. Together, the quantities alpha = (ALPHAR(j),ALPHAI(j)) and beta = BETA(j) represent the j-th eigenvalue of the matrix pair (A,B), in one of the forms lambda = alpha/beta or mu = beta/alpha. Since either lambda or mu may overflow, they should not, in general, be computed.

### QC (in,out)

QC is DOUBLE PRECISION array, dimension (LDQC, NW)

### LDQC (in)

LDQC is INTEGER

### ZC (in,out)

ZC is DOUBLE PRECISION array, dimension (LDZC, NW)

### LDZC (in)

LDZ is INTEGER

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)) On exit, if INFO >= 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= max(1,N). If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### REC (in)

REC is INTEGER REC indicates the current recursion level. Should be set to 0 on first call.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

