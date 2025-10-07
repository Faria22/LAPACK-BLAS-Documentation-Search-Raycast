# SORBDB3

## Function Signature

```fortran
SORBDB3(M, P, Q, X11, LDX11, X21, LDX21, THETA, PHI,
*                           TAUP1, TAUP2, TAUQ1, WORK, LWORK, INFO)
```

## Description


 SORBDB3 simultaneously bidiagonalizes the blocks of a tall and skinny
 matrix X with orthonormal columns:

                            [ B11 ]
      [ X11 ]   [ P1 |    ] [  0  ]
      [-----] = [---------] [-----] Q1**T .
      [ X21 ]   [    | P2 ] [ B21 ]
                            [  0  ]

 X11 is P-by-Q, and X21 is (M-P)-by-Q. M-P must be no larger than P,
 Q, or M-Q. Routines SORBDB1, SORBDB2, and SORBDB4 handle cases in
 which M-P is not the minimum dimension.

 The orthogonal matrices P1, P2, and Q1 are P-by-P, (M-P)-by-(M-P),
 and (M-Q)-by-(M-Q), respectively. They are represented implicitly by
 Householder vectors.

 B11 and B12 are (M-P)-by-(M-P) bidiagonal matrices represented
 implicitly by angles THETA, PHI.


## Parameters

### M (in)

M is INTEGER The number of rows X11 plus the number of rows in X21.

### P (in)

P is INTEGER The number of rows in X11. 0 <= P <= M. M-P <= min(P,Q,M-Q).

### Q (in)

Q is INTEGER The number of columns in X11 and X21. 0 <= Q <= M.

### X11 (in,out)

X11 is REAL array, dimension (LDX11,Q) On entry, the top block of the matrix X to be reduced. On exit, the columns of tril(X11) specify reflectors for P1 and the rows of triu(X11,1) specify reflectors for Q1.

### LDX11 (in)

LDX11 is INTEGER The leading dimension of X11. LDX11 >= P.

### X21 (in,out)

X21 is REAL array, dimension (LDX21,Q) On entry, the bottom block of the matrix X to be reduced. On exit, the columns of tril(X21) specify reflectors for P2.

### LDX21 (in)

LDX21 is INTEGER The leading dimension of X21. LDX21 >= M-P.

### THETA (out)

THETA is REAL array, dimension (Q) The entries of the bidiagonal blocks B11, B21 are defined by THETA and PHI. See Further Details.

### PHI (out)

PHI is REAL array, dimension (Q-1) The entries of the bidiagonal blocks B11, B21 are defined by THETA and PHI. See Further Details.

### TAUP1 (out)

TAUP1 is REAL array, dimension (P) The scalar factors of the elementary reflectors that define P1.

### TAUP2 (out)

TAUP2 is REAL array, dimension (M-P) The scalar factors of the elementary reflectors that define P2.

### TAUQ1 (out)

TAUQ1 is REAL array, dimension (Q) The scalar factors of the elementary reflectors that define Q1.

### WORK (out)

WORK is REAL array, dimension (LWORK)

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= M-Q. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

