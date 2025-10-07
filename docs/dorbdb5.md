# DORBDB5

## Function Signature

```fortran
DORBDB5(M1, M2, N, X1, INCX1, X2, INCX2, Q1, LDQ1, Q2,
*                           LDQ2, WORK, LWORK, INFO)
```

## Description


 DORBDB5 orthogonalizes the column vector
      X = [ X1 ]
          [ X2 ]
 with respect to the columns of
      Q = [ Q1 ] .
          [ Q2 ]
 The columns of Q must be orthonormal.

 If the projection is zero according to Kahan's "twice is enough"
 criterion, then some other vector from the orthogonal complement
 is returned. This vector is chosen in an arbitrary but deterministic
 way.


## Parameters

### M1 (in)

M1 is INTEGER The dimension of X1 and the number of rows in Q1. 0 <= M1.

### M2 (in)

M2 is INTEGER The dimension of X2 and the number of rows in Q2. 0 <= M2.

### N (in)

N is INTEGER The number of columns in Q1 and Q2. 0 <= N.

### X1 (in,out)

X1 is DOUBLE PRECISION array, dimension (M1) On entry, the top part of the vector to be orthogonalized. On exit, the top part of the projected vector.

### INCX1 (in)

INCX1 is INTEGER Increment for entries of X1.

### X2 (in,out)

X2 is DOUBLE PRECISION array, dimension (M2) On entry, the bottom part of the vector to be orthogonalized. On exit, the bottom part of the projected vector.

### INCX2 (in)

INCX2 is INTEGER Increment for entries of X2.

### Q1 (in)

Q1 is DOUBLE PRECISION array, dimension (LDQ1, N) The top part of the orthonormal basis matrix.

### LDQ1 (in)

LDQ1 is INTEGER The leading dimension of Q1. LDQ1 >= M1.

### Q2 (in)

Q2 is DOUBLE PRECISION array, dimension (LDQ2, N) The bottom part of the orthonormal basis matrix.

### LDQ2 (in)

LDQ2 is INTEGER The leading dimension of Q2. LDQ2 >= M2.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (LWORK)

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= N.

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

