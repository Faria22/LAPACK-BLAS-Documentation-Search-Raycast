# DLAHR2

## Function Signature

```fortran
DLAHR2(N, K, NB, A, LDA, TAU, T, LDT, Y, LDY)
```

## Description


 DLAHR2 reduces the first NB columns of A real general n-BY-(n-k+1)
 matrix A so that elements below the k-th subdiagonal are zero. The
 reduction is performed by an orthogonal similarity transformation
 Q**T * A * Q. The routine returns the matrices V and T which determine
 Q as a block reflector I - V*T*V**T, and also the matrix Y = A * V * T.

 This is an auxiliary routine called by DGEHRD.

## Parameters

### N (in)

N is INTEGER The order of the matrix A.

### K (in)

K is INTEGER The offset for the reduction. Elements below the k-th subdiagonal in the first NB columns are reduced to zero. K < N.

### NB (in)

NB is INTEGER The number of columns to be reduced.

### A (in,out)

A is DOUBLE PRECISION array, dimension (LDA,N-K+1) On entry, the n-by-(n-k+1) general matrix A. On exit, the elements on and above the k-th subdiagonal in the first NB columns are overwritten with the corresponding elements of the reduced matrix; the elements below the k-th subdiagonal, with the array TAU, represent the matrix Q as a product of elementary reflectors. The other columns of A are unchanged. See Further Details.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### TAU (out)

TAU is DOUBLE PRECISION array, dimension (NB) The scalar factors of the elementary reflectors. See Further Details.

### T (out)

T is DOUBLE PRECISION array, dimension (LDT,NB) The upper triangular matrix T.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= NB.

### Y (out)

Y is DOUBLE PRECISION array, dimension (LDY,NB) The n-by-nb matrix Y.

### LDY (in)

LDY is INTEGER The leading dimension of the array Y. LDY >= N.

