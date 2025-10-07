# SGGHRD

## Function Signature

```fortran
SGGHRD(COMPQ, COMPZ, N, ILO, IHI, A, LDA, B, LDB, Q,
*                          LDQ, Z, LDZ, INFO)
```

## Description


 SGGHRD reduces a pair of real matrices (A,B) to generalized upper
 Hessenberg form using orthogonal transformations, where A is a
 general matrix and B is upper triangular.  The form of the
 generalized eigenvalue problem is
    A*x = lambda*B*x,
 and B is typically made upper triangular by computing its QR
 factorization and moving the orthogonal matrix Q to the left side
 of the equation.

 This subroutine simultaneously reduces A to a Hessenberg matrix H:
    Q**T*A*Z = H
 and transforms B to another upper triangular matrix T:
    Q**T*B*Z = T
 in order to reduce the problem to its standard form
    H*y = lambda*T*y
 where y = Z**T*x.

 The orthogonal matrices Q and Z are determined as products of Givens
 rotations.  They may either be formed explicitly, or they may be
 postmultiplied into input matrices Q1 and Z1, so that

      Q1 * A * Z1**T = (Q1*Q) * H * (Z1*Z)**T

      Q1 * B * Z1**T = (Q1*Q) * T * (Z1*Z)**T

 If Q1 is the orthogonal matrix from the QR factorization of B in the
 original equation A*x = lambda*B*x, then SGGHRD reduces the original
 problem to generalized Hessenberg form.

## Parameters

### COMPQ (in)

COMPQ is CHARACTER*1 = 'N': do not compute Q; = 'I': Q is initialized to the unit matrix, and the orthogonal matrix Q is returned; = 'V': Q must contain an orthogonal matrix Q1 on entry, and the product Q1*Q is returned.

### COMPZ (in)

COMPZ is CHARACTER*1 = 'N': do not compute Z; = 'I': Z is initialized to the unit matrix, and the orthogonal matrix Z is returned; = 'V': Z must contain an orthogonal matrix Z1 on entry, and the product Z1*Z is returned.

### N (in)

N is INTEGER The order of the matrices A and B. N >= 0.

### ILO (in)

ILO is INTEGER

### IHI (in)

IHI is INTEGER ILO and IHI mark the rows and columns of A which are to be reduced. It is assumed that A is already upper triangular in rows and columns 1:ILO-1 and IHI+1:N. ILO and IHI are normally set by a previous call to SGGBAL; otherwise they should be set to 1 and N respectively. 1 <= ILO <= IHI <= N, if N > 0; ILO=1 and IHI=0, if N=0.

### A (in,out)

A is REAL array, dimension (LDA, N) On entry, the N-by-N general matrix to be reduced. On exit, the upper triangle and the first subdiagonal of A are overwritten with the upper Hessenberg matrix H, and the rest is set to zero.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in,out)

B is REAL array, dimension (LDB, N) On entry, the N-by-N upper triangular matrix B. On exit, the upper triangular matrix T = Q**T B Z. The elements below the diagonal are set to zero.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### Q (in,out)

Q is REAL array, dimension (LDQ, N) On entry, if COMPQ = 'V', the orthogonal matrix Q1, typically from the QR factorization of B. On exit, if COMPQ='I', the orthogonal matrix Q, and if COMPQ = 'V', the product Q1*Q. Not referenced if COMPQ='N'.

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= N if COMPQ='V' or 'I'; LDQ >= 1 otherwise.

### Z (in,out)

Z is REAL array, dimension (LDZ, N) On entry, if COMPZ = 'V', the orthogonal matrix Z1. On exit, if COMPZ='I', the orthogonal matrix Z, and if COMPZ = 'V', the product Z1*Z. Not referenced if COMPZ='N'.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= N if COMPZ='V' or 'I'; LDZ >= 1 otherwise.

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

