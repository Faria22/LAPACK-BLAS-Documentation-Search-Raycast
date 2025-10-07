# CUNBDB

## Function Signature

```fortran
CUNBDB(TRANS, SIGNS, M, P, Q, X11, LDX11, X12, LDX12,
*                          X21, LDX21, X22, LDX22, THETA, PHI, TAUP1,
*                          TAUP2, TAUQ1, TAUQ2, WORK, LWORK, INFO)
```

## Description


 CUNBDB simultaneously bidiagonalizes the blocks of an M-by-M
 partitioned unitary matrix X:

                                 [ B11 | B12 0  0 ]
     [ X11 | X12 ]   [ P1 |    ] [  0  |  0 -I  0 ] [ Q1 |    ]**H
 X = [-----------] = [---------] [----------------] [---------]   .
     [ X21 | X22 ]   [    | P2 ] [ B21 | B22 0  0 ] [    | Q2 ]
                                 [  0  |  0  0  I ]

 X11 is P-by-Q. Q must be no larger than P, M-P, or M-Q. (If this is
 not the case, then X must be transposed and/or permuted. This can be
 done in constant time using the TRANS and SIGNS options. See CUNCSD
 for details.)

 The unitary matrices P1, P2, Q1, and Q2 are P-by-P, (M-P)-by-
 (M-P), Q-by-Q, and (M-Q)-by-(M-Q), respectively. They are
 represented implicitly by Householder vectors.

 B11, B12, B21, and B22 are Q-by-Q bidiagonal matrices represented
 implicitly by angles THETA, PHI.

## Parameters

### TRANS (in)

TRANS is CHARACTER = 'T': X, U1, U2, V1T, and V2T are stored in row-major order; otherwise: X, U1, U2, V1T, and V2T are stored in column- major order.

### SIGNS (in)

SIGNS is CHARACTER = 'O': The lower-left block is made nonpositive (the "other" convention); otherwise: The upper-right block is made nonpositive (the "default" convention).

### M (in)

M is INTEGER The number of rows and columns in X.

### P (in)

P is INTEGER The number of rows in X11 and X12. 0 <= P <= M.

### Q (in)

Q is INTEGER The number of columns in X11 and X21. 0 <= Q <= MIN(P,M-P,M-Q).

### X11 (in,out)

X11 is COMPLEX array, dimension (LDX11,Q) On entry, the top-left block of the unitary matrix to be reduced. On exit, the form depends on TRANS: If TRANS = 'N', then the columns of tril(X11) specify reflectors for P1, the rows of triu(X11,1) specify reflectors for Q1; else TRANS = 'T', and the rows of triu(X11) specify reflectors for P1, the columns of tril(X11,-1) specify reflectors for Q1.

### LDX11 (in)

LDX11 is INTEGER The leading dimension of X11. If TRANS = 'N', then LDX11 >= P; else LDX11 >= Q.

### X12 (in,out)

X12 is COMPLEX array, dimension (LDX12,M-Q) On entry, the top-right block of the unitary matrix to be reduced. On exit, the form depends on TRANS: If TRANS = 'N', then the rows of triu(X12) specify the first P reflectors for Q2; else TRANS = 'T', and the columns of tril(X12) specify the first P reflectors for Q2.

### LDX12 (in)

LDX12 is INTEGER The leading dimension of X12. If TRANS = 'N', then LDX12 >= P; else LDX11 >= M-Q.

### X21 (in,out)

X21 is COMPLEX array, dimension (LDX21,Q) On entry, the bottom-left block of the unitary matrix to be reduced. On exit, the form depends on TRANS: If TRANS = 'N', then the columns of tril(X21) specify reflectors for P2; else TRANS = 'T', and the rows of triu(X21) specify reflectors for P2.

### LDX21 (in)

LDX21 is INTEGER The leading dimension of X21. If TRANS = 'N', then LDX21 >= M-P; else LDX21 >= Q.

### X22 (in,out)

X22 is COMPLEX array, dimension (LDX22,M-Q) On entry, the bottom-right block of the unitary matrix to be reduced. On exit, the form depends on TRANS: If TRANS = 'N', then the rows of triu(X22(Q+1:M-P,P+1:M-Q)) specify the last M-P-Q reflectors for Q2, else TRANS = 'T', and the columns of tril(X22(P+1:M-Q,Q+1:M-P)) specify the last M-P-Q reflectors for P2.

### LDX22 (in)

LDX22 is INTEGER The leading dimension of X22. If TRANS = 'N', then LDX22 >= M-P; else LDX22 >= M-Q.

### THETA (out)

THETA is REAL array, dimension (Q) The entries of the bidiagonal blocks B11, B12, B21, B22 can be computed from the angles THETA and PHI. See Further Details.

### PHI (out)

PHI is REAL array, dimension (Q-1) The entries of the bidiagonal blocks B11, B12, B21, B22 can be computed from the angles THETA and PHI. See Further Details.

### TAUP1 (out)

TAUP1 is COMPLEX array, dimension (P) The scalar factors of the elementary reflectors that define P1.

### TAUP2 (out)

TAUP2 is COMPLEX array, dimension (M-P) The scalar factors of the elementary reflectors that define P2.

### TAUQ1 (out)

TAUQ1 is COMPLEX array, dimension (Q) The scalar factors of the elementary reflectors that define Q1.

### TAUQ2 (out)

TAUQ2 is COMPLEX array, dimension (M-Q) The scalar factors of the elementary reflectors that define Q2.

### WORK (out)

WORK is COMPLEX array, dimension (LWORK)

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= M-Q. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

