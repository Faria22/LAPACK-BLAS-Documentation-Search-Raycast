# ZUNCSD2BY1

## Function Signature

```fortran
ZUNCSD2BY1(JOBU1, JOBU2, JOBV1T, M, P, Q, X11, LDX11,
*                              X21, LDX21, THETA, U1, LDU1, U2, LDU2, V1T,
*                              LDV1T, WORK, LWORK, RWORK, LRWORK, IWORK,
*                              INFO)
```

## Description


 ZUNCSD2BY1 computes the CS decomposition of an M-by-Q matrix X with
 orthonormal columns that has been partitioned into a 2-by-1 block
 structure:

                                [  I1 0  0 ]
                                [  0  C  0 ]
          [ X11 ]   [ U1 |    ] [  0  0  0 ]
      X = [-----] = [---------] [----------] V1**T .
          [ X21 ]   [    | U2 ] [  0  0  0 ]
                                [  0  S  0 ]
                                [  0  0  I2]

 X11 is P-by-Q. The unitary matrices U1, U2, and V1 are P-by-P,
 (M-P)-by-(M-P), and Q-by-Q, respectively. C and S are R-by-R
 nonnegative diagonal matrices satisfying C^2 + S^2 = I, in which
 R = MIN(P,M-P,Q,M-Q). I1 is a K1-by-K1 identity matrix and I2 is a
 K2-by-K2 identity matrix, where K1 = MAX(Q+P-M,0), K2 = MAX(Q-P,0).

## Parameters

### JOBU1 (in)

JOBU1 is CHARACTER = 'Y': U1 is computed; otherwise: U1 is not computed.

### JOBU2 (in)

JOBU2 is CHARACTER = 'Y': U2 is computed; otherwise: U2 is not computed.

### JOBV1T (in)

JOBV1T is CHARACTER = 'Y': V1T is computed; otherwise: V1T is not computed.

### M (in)

M is INTEGER The number of rows in X.

### P (in)

P is INTEGER The number of rows in X11. 0 <= P <= M.

### Q (in)

Q is INTEGER The number of columns in X11 and X21. 0 <= Q <= M.

### X11 (in,out)

X11 is COMPLEX*16 array, dimension (LDX11,Q) On entry, part of the unitary matrix whose CSD is desired.

### LDX11 (in)

LDX11 is INTEGER The leading dimension of X11. LDX11 >= MAX(1,P).

### X21 (in,out)

X21 is COMPLEX*16 array, dimension (LDX21,Q) On entry, part of the unitary matrix whose CSD is desired.

### LDX21 (in)

LDX21 is INTEGER The leading dimension of X21. LDX21 >= MAX(1,M-P).

### THETA (out)

THETA is DOUBLE PRECISION array, dimension (R), in which R = MIN(P,M-P,Q,M-Q). C = DIAG( COS(THETA(1)), ... , COS(THETA(R)) ) and S = DIAG( SIN(THETA(1)), ... , SIN(THETA(R)) ).

### U1 (out)

U1 is COMPLEX*16 array, dimension (P) If JOBU1 = 'Y', U1 contains the P-by-P unitary matrix U1.

### LDU1 (in)

LDU1 is INTEGER The leading dimension of U1. If JOBU1 = 'Y', LDU1 >= MAX(1,P).

### U2 (out)

U2 is COMPLEX*16 array, dimension (M-P) If JOBU2 = 'Y', U2 contains the (M-P)-by-(M-P) unitary matrix U2.

### LDU2 (in)

LDU2 is INTEGER The leading dimension of U2. If JOBU2 = 'Y', LDU2 >= MAX(1,M-P).

### V1T (out)

V1T is COMPLEX*16 array, dimension (Q) If JOBV1T = 'Y', V1T contains the Q-by-Q matrix unitary matrix V1**T.

### LDV1T (in)

LDV1T is INTEGER The leading dimension of V1T. If JOBV1T = 'Y', LDV1T >= MAX(1,Q).

### WORK (out)

WORK is COMPLEX*16 array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK and RWORK arrays, returns this value as the first entry of the WORK and RWORK array, respectively, and no error message related to LWORK or LRWORK is issued by XERBLA.

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (MAX(1,LRWORK)) On exit, if INFO = 0, RWORK(1) returns the optimal LRWORK. If INFO > 0 on exit, RWORK(2:R) contains the values PHI(1), ..., PHI(R-1) that, together with THETA(1), ..., THETA(R), define the matrix in intermediate bidiagonal-block form remaining after nonconvergence. INFO specifies the number of nonzero PHI's.

### LRWORK (in)

LRWORK is INTEGER The dimension of the array RWORK. If LRWORK=-1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK and RWORK arrays, returns this value as the first entry of the WORK and RWORK array, respectively, and no error message related to LWORK or LRWORK is issued by XERBLA.

### IWORK (out)

IWORK is INTEGER array, dimension (M-MIN(P,M-P,Q,M-Q))

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value. > 0: ZBBCSD did not converge. See the description of WORK above for details.

