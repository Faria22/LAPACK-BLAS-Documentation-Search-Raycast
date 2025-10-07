```fortran
subroutine zuncsd2by1	(	jobu1,
		jobu2,
		jobv1t,
		m,
		p,
		q,
		x11,
		ldx11,
		*                              x21,
		ldx21,
		theta,
		u1,
		ldu1,
		u2,
		ldu2,
		v1t,
		*                              ldv1t,
		work,
		lwork,
		rwork,
		lrwork,
		iwork,
		*                              info )
```

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
Jobu1 : Character [in]
> = 'Y':      U1 is computed;
> otherwise:  U1 is not computed.

Jobu2 : Character [in]
> = 'Y':      U2 is computed;
> otherwise:  U2 is not computed.

Jobv1t : Character [in]
> = 'Y':      V1T is computed;
> otherwise:  V1T is not computed.

M : Integer [in]
> The number of rows in X.

P : Integer [in]
> The number of rows in X11. 0 <= P <= M.

Q : Integer [in]
> The number of columns in X11 and X21. 0 <= Q <= M.

X11 : Complex*16 Array, Dimension (ldx11,q) [in,out]
> On entry, part of the unitary matrix whose CSD is desired.

Ldx11 : Integer [in]
> The leading dimension of X11. LDX11 >= MAX(1,P).

X21 : Complex*16 Array, Dimension (ldx21,q) [in,out]
> On entry, part of the unitary matrix whose CSD is desired.

Ldx21 : Integer [in]
> The leading dimension of X21. LDX21 >= MAX(1,M-P).

Theta : Double Precision Array, Dimension (r), In Which R = [out]
> MIN(P,M-P,Q,M-Q).
> C = DIAG( COS(THETA(1)), ... , COS(THETA(R)) ) and
> S = DIAG( SIN(THETA(1)), ... , SIN(THETA(R)) ).

U1 : Complex*16 Array, Dimension (p) [out]
> If JOBU1 = 'Y', U1 contains the P-by-P unitary matrix U1.

Ldu1 : Integer [in]
> The leading dimension of U1. If JOBU1 = 'Y', LDU1 >=
> MAX(1,P).

U2 : Complex*16 Array, Dimension (m-p) [out]
> If JOBU2 = 'Y', U2 contains the (M-P)-by-(M-P) unitary
> matrix U2.

Ldu2 : Integer [in]
> The leading dimension of U2. If JOBU2 = 'Y', LDU2 >=
> MAX(1,M-P).

V1t : Complex*16 Array, Dimension (q) [out]
> If JOBV1T = 'Y', V1T contains the Q-by-Q matrix unitary
> matrix V1**T.

Ldv1t : Integer [in]
> The leading dimension of V1T. If JOBV1T = 'Y', LDV1T >=
> MAX(1,Q).

Work : Complex*16 Array, Dimension (max(1,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK.
> If LWORK = -1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK and RWORK
> arrays, returns this value as the first entry of the WORK
> and RWORK array, respectively, and no error message related
> to LWORK or LRWORK is issued by XERBLA.

Rwork : Double Precision Array, Dimension (max(1,lrwork)) [out]
> On exit, if INFO = 0, RWORK(1) returns the optimal LRWORK.
> If INFO > 0 on exit, RWORK(2:R) contains the values PHI(1),
> ..., PHI(R-1) that, together with THETA(1), ..., THETA(R),
> define the matrix in intermediate bidiagonal-block form
> remaining after nonconvergence. INFO specifies the number
> of nonzero PHI's.

Lrwork : Integer [in]
> The dimension of the array RWORK.
> If LRWORK=-1, then a workspace query is assumed; the routine
> only calculates the optimal size of the WORK and RWORK
> arrays, returns this value as the first entry of the WORK
> and RWORK array, respectively, and no error message related
> to LWORK or LRWORK is issued by XERBLA.

Iwork : Integer Array, Dimension (m-min(p,m-p,q,m-q)) [out]

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.
> > 0:  ZBBCSD did not converge. See the description of WORK
> above for details.

