# CGEHD2

## Function Signature

```fortran
CGEHD2(N, ILO, IHI, A, LDA, TAU, WORK, INFO)
```

## Description


 CGEHD2 reduces a complex general matrix A to upper Hessenberg form H
 by a unitary similarity transformation:  Q**H * A * Q = H .

## Parameters

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### ILO (in)

ILO is INTEGER

### IHI (in)

IHI is INTEGER It is assumed that A is already upper triangular in rows and columns 1:ILO-1 and IHI+1:N. ILO and IHI are normally set by a previous call to CGEBAL; otherwise they should be set to 1 and N respectively. See Further Details. 1 <= ILO <= IHI <= max(1,N).

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the n by n general matrix to be reduced. On exit, the upper triangle and the first subdiagonal of A are overwritten with the upper Hessenberg matrix H, and the elements below the first subdiagonal, with the array TAU, represent the unitary matrix Q as a product of elementary reflectors. See Further Details.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### TAU (out)

TAU is COMPLEX array, dimension (N-1) The scalar factors of the elementary reflectors (see Further Details).

### WORK (out)

WORK is COMPLEX array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value.

