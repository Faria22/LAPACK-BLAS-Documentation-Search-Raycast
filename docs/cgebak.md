# CGEBAK

## Function Signature

```fortran
CGEBAK(JOB, SIDE, N, ILO, IHI, SCALE, M, V, LDV,
*                          INFO)
```

## Description


 CGEBAK forms the right or left eigenvectors of a complex general
 matrix by backward transformation on the computed eigenvectors of the
 balanced matrix output by CGEBAL.

## Parameters

### JOB (in)

JOB is CHARACTER*1 Specifies the type of backward transformation required: = 'N': do nothing, return immediately; = 'P': do backward transformation for permutation only; = 'S': do backward transformation for scaling only; = 'B': do backward transformations for both permutation and scaling. JOB must be the same as the argument JOB supplied to CGEBAL.

### SIDE (in)

SIDE is CHARACTER*1 = 'R': V contains right eigenvectors; = 'L': V contains left eigenvectors.

### N (in)

N is INTEGER The number of rows of the matrix V. N >= 0.

### ILO (in)

ILO is INTEGER

### IHI (in)

IHI is INTEGER The integers ILO and IHI determined by CGEBAL. 1 <= ILO <= IHI <= N, if N > 0; ILO=1 and IHI=0, if N=0.

### SCALE (in)

SCALE is REAL array, dimension (N) Details of the permutation and scaling factors, as returned by CGEBAL.

### M (in)

M is INTEGER The number of columns of the matrix V. M >= 0.

### V (in,out)

V is COMPLEX array, dimension (LDV,M) On entry, the matrix of right or left eigenvectors to be transformed, as returned by CHSEIN or CTREVC. On exit, V is overwritten by the transformed eigenvectors.

### LDV (in)

LDV is INTEGER The leading dimension of the array V. LDV >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value.

