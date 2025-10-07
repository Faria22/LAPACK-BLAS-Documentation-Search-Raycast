# SSB2ST_KERNELS

## Function Signature

```fortran
SSB2ST_KERNELS(UPLO, WANTZ, TTYPE,
*                                   ST, ED, SWEEP, N, NB, IB,
*                                   A, LDA, V, TAU, LDVT, WORK)
```

## Description


 SSB2ST_KERNELS is an internal routine used by the SSYTRD_SB2ST
 subroutine.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1

### WANTZ (in)

WANTZ is LOGICAL which indicate if Eigenvalue are requested or both Eigenvalue/Eigenvectors.

### TTYPE (in)

TTYPE is INTEGER

### ST (in)

ST is INTEGER internal parameter for indices.

### ED (in)

ED is INTEGER internal parameter for indices.

### SWEEP (in)

SWEEP is INTEGER internal parameter for indices.

### N (in)

N is INTEGER. The order of the matrix A.

### NB (in)

NB is INTEGER. The size of the band.

### IB (in)

IB is INTEGER.

### A (in, out)

A is REAL array. A pointer to the matrix A.

### LDA (in)

LDA is INTEGER. The leading dimension of the matrix A.

### V (out)

V is REAL array, dimension 2*n if eigenvalues only are requested or to be queried for vectors.

### TAU (out)

TAU is REAL array, dimension (2*n). The scalar factors of the Householder reflectors are stored in this array.

### LDVT (in)

LDVT is INTEGER.

### WORK (out)

WORK is REAL array. Workspace of size nb.

