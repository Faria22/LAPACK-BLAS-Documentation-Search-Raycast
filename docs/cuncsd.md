# CUNCSD

## Function Signature

```fortran
CUNCSD(JOBU1, JOBU2, JOBV1T, JOBV2T, TRANS,
*                                    SIGNS, M, P, Q, X11, LDX11, X12,
*                                    LDX12, X21, LDX21, X22, LDX22, THETA,
*                                    U1, LDU1, U2, LDU2, V1T, LDV1T, V2T,
*                                    LDV2T, WORK, LWORK, RWORK, LRWORK,
*                                    IWORK, INFO)
```

## Description


 CUNCSD computes the CS decomposition of an M-by-M partitioned
 unitary matrix X:

                                 [  I  0  0 |  0  0  0 ]
                                 [  0  C  0 |  0 -S  0 ]
     [ X11 | X12 ]   [ U1 |    ] [  0  0  0 |  0  0 -I ] [ V1 |    ]**H
 X = [-----------] = [---------] [---------------------] [---------]   .
     [ X21 | X22 ]   [    | U2 ] [  0  0  0 |  I  0  0 ] [    | V2 ]
                                 [  0  S  0 |  0  C  0 ]
                                 [  0  0  I |  0  0  0 ]

 X11 is P-by-Q. The unitary matrices U1, U2, V1, and V2 are P-by-P,
 (M-P)-by-(M-P), Q-by-Q, and (M-Q)-by-(M-Q), respectively. C and S are
 R-by-R nonnegative diagonal matrices satisfying C^2 + S^2 = I, in
 which R = MIN(P,M-P,Q,M-Q).

## Parameters

### JOBU1 (in)

JOBU1 is CHARACTER = 'Y': U1 is computed; otherwise: U1 is not computed.

### JOBU2 (in)

JOBU2 is CHARACTER = 'Y': U2 is computed; otherwise: U2 is not computed.

### JOBV1T (in)

JOBV1T is CHARACTER = 'Y': V1T is computed; otherwise: V1T is not computed.

### JOBV2T (in)

JOBV2T is CHARACTER = 'Y': V2T is computed; otherwise: V2T is not computed.

### TRANS (in)

TRANS is CHARACTER = 'T': X, U1, U2, V1T, and V2T are stored in row-major order; otherwise: X, U1, U2, V1T, and V2T are stored in column- major order.

### SIGNS (in)

SIGNS is CHARACTER = 'O': The lower-left block is made nonpositive (the "other" convention); otherwise: The upper-right block is made nonpositive (the "default" convention).

### M (in)

M is INTEGER The number of rows and columns in X.

### P (in)

P is INTEGER The number of rows in X11 and X12. 0 <= P <= M.

### Q (in)

Q is INTEGER The number of columns in X11 and X21. 0 <= Q <= M.

### X11 (in,out)

X11 is COMPLEX array, dimension (LDX11,Q) On entry, part of the unitary matrix whose CSD is desired.

### LDX11 (in)

LDX11 is INTEGER The leading dimension of X11. LDX11 >= MAX(1,P).

### X12 (in,out)

X12 is COMPLEX array, dimension (LDX12,M-Q) On entry, part of the unitary matrix whose CSD is desired.

### LDX12 (in)

LDX12 is INTEGER The leading dimension of X12. LDX12 >= MAX(1,P).

### X21 (in,out)

X21 is COMPLEX array, dimension (LDX21,Q) On entry, part of the unitary matrix whose CSD is desired.

### LDX21 (in)

LDX21 is INTEGER The leading dimension of X11. LDX21 >= MAX(1,M-P).

### X22 (in,out)

X22 is COMPLEX array, dimension (LDX22,M-Q) On entry, part of the unitary matrix whose CSD is desired.

### LDX22 (in)

LDX22 is INTEGER The leading dimension of X11. LDX22 >= MAX(1,M-P).

### THETA (out)

THETA is REAL array, dimension (R), in which R = MIN(P,M-P,Q,M-Q). C = DIAG( COS(THETA(1)), ... , COS(THETA(R)) ) and S = DIAG( SIN(THETA(1)), ... , SIN(THETA(R)) ).

### U1 (out)

U1 is COMPLEX array, dimension (LDU1,P) If JOBU1 = 'Y', U1 contains the P-by-P unitary matrix U1.

### LDU1 (in)

LDU1 is INTEGER The leading dimension of U1. If JOBU1 = 'Y', LDU1 >= MAX(1,P).

### U2 (out)

U2 is COMPLEX array, dimension (LDU2,M-P) If JOBU2 = 'Y', U2 contains the (M-P)-by-(M-P) unitary matrix U2.

### LDU2 (in)

LDU2 is INTEGER The leading dimension of U2. If JOBU2 = 'Y', LDU2 >= MAX(1,M-P).

### V1T (out)

V1T is COMPLEX array, dimension (LDV1T,Q) If JOBV1T = 'Y', V1T contains the Q-by-Q matrix unitary matrix V1**H.

### LDV1T (in)

LDV1T is INTEGER The leading dimension of V1T. If JOBV1T = 'Y', LDV1T >= MAX(1,Q).

### V2T (out)

V2T is COMPLEX array, dimension (LDV2T,M-Q) If JOBV2T = 'Y', V2T contains the (M-Q)-by-(M-Q) unitary matrix V2**H.

### LDV2T (in)

LDV2T is INTEGER The leading dimension of V2T. If JOBV2T = 'Y', LDV2T >= MAX(1,M-Q).

### WORK (out)

WORK is COMPLEX array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the work array, and no error message related to LWORK is issued by XERBLA.

### RWORK (out)

RWORK is REAL array, dimension MAX(1,LRWORK) On exit, if INFO = 0, RWORK(1) returns the optimal LRWORK. If INFO > 0 on exit, RWORK(2:R) contains the values PHI(1), ..., PHI(R-1) that, together with THETA(1), ..., THETA(R), define the matrix in intermediate bidiagonal-block form remaining after nonconvergence. INFO specifies the number of nonzero PHI's.

### LRWORK (in)

LRWORK is INTEGER The dimension of the array RWORK. If LRWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the RWORK array, returns this value as the first entry of the work array, and no error message related to LRWORK is issued by XERBLA.

### IWORK (out)

IWORK is INTEGER array, dimension (M-MIN(P,M-P,Q,M-Q))

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value. > 0: CBBCSD did not converge. See the description of RWORK above for details.

