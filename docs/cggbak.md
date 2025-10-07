# CGGBAK

## Function Signature

```fortran
CGGBAK(JOB, SIDE, N, ILO, IHI, LSCALE, RSCALE, M, V,
*                          LDV, INFO)
```

## Description


 CGGBAK forms the right or left eigenvectors of a complex generalized
 eigenvalue problem A*x = lambda*B*x, by backward transformation on
 the computed eigenvectors of the balanced pair of matrices output by
 CGGBAL.

## Parameters

### JOB (in)

JOB is CHARACTER*1 Specifies the type of backward transformation required: = 'N': do nothing, return immediately; = 'P': do backward transformation for permutation only; = 'S': do backward transformation for scaling only; = 'B': do backward transformations for both permutation and scaling. JOB must be the same as the argument JOB supplied to CGGBAL.

### SIDE (in)

SIDE is CHARACTER*1 = 'R': V contains right eigenvectors; = 'L': V contains left eigenvectors.

### N (in)

N is INTEGER The number of rows of the matrix V. N >= 0.

### ILO (in)

ILO is INTEGER

### IHI (in)

IHI is INTEGER The integers ILO and IHI determined by CGGBAL. 1 <= ILO <= IHI <= N, if N > 0; ILO=1 and IHI=0, if N=0.

### LSCALE (in)

LSCALE is REAL array, dimension (N) Details of the permutations and/or scaling factors applied to the left side of A and B, as returned by CGGBAL.

### RSCALE (in)

RSCALE is REAL array, dimension (N) Details of the permutations and/or scaling factors applied to the right side of A and B, as returned by CGGBAL.

### M (in)

M is INTEGER The number of columns of the matrix V. M >= 0.

### V (in,out)

V is COMPLEX array, dimension (LDV,M) On entry, the matrix of right or left eigenvectors to be transformed, as returned by CTGEVC. On exit, V is overwritten by the transformed eigenvectors.

### LDV (in)

LDV is INTEGER The leading dimension of the matrix V. LDV >= max(1,N).

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

