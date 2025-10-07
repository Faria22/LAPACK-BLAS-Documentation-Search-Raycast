# ZLAQZ3

## Function Signature

```fortran
ZLAQZ3(ILSCHUR, ILQ, ILZ, N, ILO, IHI, NSHIFTS,
*     $    NBLOCK_DESIRED, ALPHA, BETA, A, LDA, B, LDB, Q, LDQ, Z, LDZ,
*     $    QC, LDQC, ZC, LDZC, WORK, LWORK, INFO)
```

## Description


 ZLAQZ3 Executes a single multishift QZ sweep

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

IHI is INTEGER

### NSHIFTS (in)

NSHIFTS is INTEGER The desired number of shifts to use

### NBLOCK_DESIRED (in)

NBLOCK_DESIRED is INTEGER The desired size of the computational windows

### ALPHA (in)

ALPHA is COMPLEX*16 array. SR contains the alpha parts of the shifts to use.

### BETA (in)

BETA is COMPLEX*16 array. SS contains the scale of the shifts to use.

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

### QC (in,out)

QC is COMPLEX*16 array, dimension (LDQC, NBLOCK_DESIRED)

### LDQC (in)

LDQC is INTEGER

### ZC (in,out)

ZC is COMPLEX*16 array, dimension (LDZC, NBLOCK_DESIRED)

### LDZC (in)

LDZ is INTEGER

### WORK (out)

WORK is COMPLEX*16 array, dimension (MAX(1,LWORK)) On exit, if INFO >= 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= max(1,N). If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

