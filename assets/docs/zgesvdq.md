```fortran  
subroutine zgesvdq (  
joba,  
jobp,  
jobr,  
jobu,  
jobv,  
m,  
n,  
a,  
lda,  
*                          s,  
u,  
ldu,  
v,  
ldv,  
numrank,  
iwork,  
liwork,  
*                          cwork,  
lcwork,  
rwork,  
lrwork,  
info  
)  
```  
  
ZCGESVDQ computes the singular value decomposition (SVD) of a complex  
M-by-N matrix A, where M >= N. The SVD of A is written as  
[++]   [xx]   [x0]   [xx]  
A = U * SIGMA * V^*,  [++] = [xx] * [ox] * [xx]  
[++]   [xx]  
where SIGMA is an N-by-N diagonal matrix, U is an M-by-N orthonormal  
matrix, and V is an N-by-N unitary matrix. The diagonal elements  
of SIGMA are the singular values of A. The columns of U and V are the  
left and the right singular vectors of A, respectively.  
  
## Parameters  
Joba : Character*1 [in]  
> Specifies the level of accuracy in the computed SVD  
> = 'A' The requested accuracy corresponds to having the backward  
> where EPS = DLAMCH('Epsilon'). This authorises ZGESVDQ to  
> truncate the computed triangular factor in a rank revealing  
> QR factorization whenever the truncated part is below the  
> truncation level.  
> = 'M' Similarly as with 'A', but the truncation is more gentle: it  
> is allowed only when there is a drop on the diagonal of the  
> triangular factor in the QR factorization. This is medium  
> truncation level.  
> = 'H' High accuracy requested. No numerical rank determination based  
> on the rank revealing QR factorization is attempted.  
> = 'E' Same as 'H', and in addition the condition number of column  
> scaled A is estimated and returned in  RWORK(1).  
  
Jobp : Character*1 [in]  
> = 'P' The rows of A are ordered in decreasing order with respect to  
> ||A(i,:)||_\infty. This enhances numerical accuracy at the cost  
> of extra data movement. Recommended for numerical robustness.  
> = 'N' No row pivoting.  
  
Jobr : Character*1 [in]  
> = 'T' After the initial pivoted QR factorization, ZGESVD is applied to  
> some extra data movement (matrix transpositions). Useful for  
> experiments, research and development.  
> = 'N' The triangular factor R is given as input to CGESVD. This may be  
> preferred as it involves less data movement.  
  
Jobu : Character*1 [in]  
> = 'A' All M left singular vectors are computed and returned in the  
> matrix U. See the description of U.  
> = 'S' or 'U' N = min(M,N) left singular vectors are computed and returned  
> in the matrix U. See the description of U.  
> = 'R' Numerical rank NUMRANK is determined and only NUMRANK left singular  
> vectors are computed and returned in the matrix U.  
> = 'F' The N left singular vectors are returned in factored form as the  
> product of the Q factor from the initial QR factorization and the  
> then the necessary information on the row pivoting is stored in  
> IWORK(N+1:N+M-1).  
> = 'N' The left singular vectors are not computed.  
  
Jobv : Character*1 [in]  
> = 'A', 'V' All N right singular vectors are computed and returned in  
> the matrix V.  
> = 'R' Numerical rank NUMRANK is determined and only NUMRANK right singular  
> vectors are computed and returned in the matrix V. This option is  
> allowed only if JOBU = 'R' or JOBU = 'N'; otherwise it is illegal.  
> = 'N' The right singular vectors are not computed.  
  
M : Integer [in]  
> The number of rows of the input matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the input matrix A.  M >= N >= 0.  
  
A : Complex*16 Array of Dimensions Lda X N [in,out]  
> On entry, the input matrix A.  
> On exit, if JOBU .NE. 'N' or JOBV .NE. 'N', the lower triangle of A contains  
> the Householder vectors as stored by ZGEQP3. If JOBU = 'F', these Householder  
> vectors together with CWORK(1:N) can be used to restore the Q factors from  
> the initial pivoted QR factorization of A. See the description of U.  
  
Lda : Integer. [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
S : Double Precision Array of Dimension N. [out]  
> The singular values of A, ordered so that S(i) >= S(i+1).  
  
U : Complex*16 Array, Dimension [out]  
> LDU x M if JOBU = 'A'; see the description of LDU. In this case,  
> on exit, U contains the M left singular vectors.  
> LDU x N if JOBU = 'S', 'U', 'R' ; see the description of LDU. In this  
> case, U contains the leading N or the leading NUMRANK left singular vectors.  
> LDU x N if JOBU = 'F' ; see the description of LDU. In this case U  
> contains N x N unitary matrix that can be used to form the left  
> singular vectors.  
> If JOBU = 'N', U is not referenced.  
  
Ldu : Integer. [in]  
> The leading dimension of the array U.  
> If JOBU = 'A', 'S', 'U', 'R',  LDU >= max(1,M).  
> If JOBU = 'F',                 LDU >= max(1,N).  
> Otherwise,                     LDU >= 1.  
  
V : Complex*16 Array, Dimension [out]  
> LDV x N if JOBV = 'A', 'V', 'R' or if JOBA = 'E' .  
> singular vectors, stored rowwise, of the NUMRANK largest singular values).  
> If JOBV = 'N' and JOBA = 'E', V is used as a workspace.  
> If JOBV = 'N', and JOBA.NE.'E', V is not referenced.  
  
Ldv : Integer [in]  
> The leading dimension of the array V.  
> If JOBV = 'A', 'V', 'R',  or JOBA = 'E', LDV >= max(1,N).  
> Otherwise,                               LDV >= 1.  
  
Numrank : Integer [out]  
> NUMRANK is the numerical rank first determined after the rank  
> revealing QR factorization, following the strategy specified by the  
> value of JOBA. If JOBV = 'R' and JOBU = 'R', only NUMRANK  
> leading singular values and vectors are then requested in the call  
> of CGESVD. The final value of NUMRANK might be further reduced if  
> some singular values are computed as zeros.  
  
Iwork : Integer Array, Dimension (max(1, Liwork)). [out]  
> On exit, IWORK(1:N) contains column pivoting permutation of the  
> rank revealing QR factorization.  
> If JOBP = 'P', IWORK(N+1:N+M-1) contains the indices of the sequence  
> of row swaps used in row pivoting. These can be used to restore the  
> left singular vectors in the case JOBU = 'F'.  
> If LIWORK, LCWORK, or LRWORK = -1, then on exit, if INFO = 0,  
> IWORK(1) returns the minimal LIWORK.  
  
Liwork : Integer [in]  
> The dimension of the array IWORK.  
> LIWORK >= N + M - 1,  if JOBP = 'P';  
> LIWORK >= N           if JOBP = 'N'.  
> If LIWORK = -1, then a workspace query is assumed; the routine  
> only calculates and returns the optimal and minimal sizes  
> for the CWORK, IWORK, and RWORK arrays, and no error  
> message related to LCWORK is issued by XERBLA.  
  
Cwork : Complex*12 Array, Dimension (max(2, Lcwork)), Used As a Workspace. [out]  
> On exit, if, on entry, LCWORK.NE.-1, CWORK(1:N) contains parameters  
> needed to recover the Q factor from the QR factorization computed by  
> ZGEQP3.  
> If LIWORK, LCWORK, or LRWORK = -1, then on exit, if INFO = 0,  
> CWORK(1) returns the optimal LCWORK, and  
> CWORK(2) returns the minimal LCWORK.  
  
Lcwork : Integer [in,out]  
> The dimension of the array CWORK. It is determined as follows:  
> LWUNQ = { MAX( N, 1 ),  if JOBU = 'R', 'S', or 'U'  
> { MAX( M, 1 ),  if JOBU = 'A'  
> LWQRF = MAX( N/2, 1 ), LWUNQ2 = MAX( N, 1 )  
> Then the minimal value of LCWORK is:  
> = MAX( N + LWQP3, LWSVD )        if only the singular values are needed;  
> = MAX( N + LWQP3, LWCON, LWSVD ) if only the singular values are needed,  
> and a scaled condition estimate requested;  
> = N + MAX( LWQP3, LWSVD, LWUNQ ) if the singular values and the left  
> singular vectors are requested;  
> = N + MAX( LWQP3, LWCON, LWSVD, LWUNQ ) if the singular values and the left  
> singular vectors are requested, and also  
> a scaled condition estimate requested;  
> = N + MAX( LWQP3, LWSVD )        if the singular values and the right  
> singular vectors are requested;  
> = N + MAX( LWQP3, LWCON, LWSVD ) if the singular values and the right  
> singular vectors are requested, and also  
> a scaled condition etimate requested;  
> = N + MAX( LWQP3, LWSVD, LWUNQ ) if the full SVD is requested with JOBV = 'R';  
> independent of JOBR;  
> = N + MAX( LWQP3, LWCON, LWSVD, LWUNQ ) if the full SVD is requested,  
> JOBV = 'R' and, also a scaled condition  
> estimate requested; independent of JOBR;  
> = MAX( N + MAX( LWQP3, LWSVD, LWUNQ ),  
> N + MAX( LWQP3, N/2+LWLQF, N/2+LWSVD2, N/2+LWUNLQ, LWUNQ) ) if the  
> full SVD is requested with JOBV = 'A' or 'V', and  
> JOBR ='N'  
> = MAX( N + MAX( LWQP3, LWCON, LWSVD, LWUNQ ),  
> N + MAX( LWQP3, LWCON, N/2+LWLQF, N/2+LWSVD2, N/2+LWUNLQ, LWUNQ ) )  
> if the full SVD is requested with JOBV = 'A' or 'V', and  
> JOBR ='N', and also a scaled condition number estimate  
> requested.  
> = MAX( N + MAX( LWQP3, LWSVD, LWUNQ ),  
> N + MAX( LWQP3, N/2+LWQRF, N/2+LWSVD2, N/2+LWUNQ2, LWUNQ ) ) if the  
> full SVD is requested with JOBV = 'A', 'V', and JOBR ='T'  
> = MAX( N + MAX( LWQP3, LWCON, LWSVD, LWUNQ ),  
> N + MAX( LWQP3, LWCON, N/2+LWQRF, N/2+LWSVD2, N/2+LWUNQ2, LWUNQ ) )  
> if the full SVD is requested with JOBV = 'A', 'V' and  
> JOBR ='T', and also a scaled condition number estimate  
> requested.  
> Finally, LCWORK must be at least two: LCWORK = MAX( 2, LCWORK ).  
> If LCWORK = -1, then a workspace query is assumed; the routine  
> only calculates and returns the optimal and minimal sizes  
> for the CWORK, IWORK, and RWORK arrays, and no error  
> message related to LCWORK is issued by XERBLA.  
  
Rwork : Double Precision Array, Dimension (max(1, Lrwork)). [out]  
> On exit,  
> 1. If JOBA = 'E', RWORK(1) contains an estimate of the condition  
> has unit columns in the Euclidean norm, then, assuming full column rank,  
> Otherwise, RWORK(1) = -1.  
> 2. RWORK(2) contains the number of singular values computed as  
> exact zeros in ZGESVD applied to the upper triangular or trapezoidal  
> R (from the initial QR factorization). In case of early exit (no call to  
> ZGESVD, such as in the case of zero matrix) RWORK(2) = -1.  
> If LIWORK, LCWORK, or LRWORK = -1, then on exit, if INFO = 0,  
> RWORK(1) returns the minimal LRWORK.  
  
Lrwork : Integer. [in]  
> The dimension of the array RWORK.  
> If LRWORK = -1, then a workspace query is assumed; the routine  
> only calculates and returns the optimal and minimal sizes  
> for the CWORK, IWORK, and RWORK arrays, and no error  
> message related to LCWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit.  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
> > 0:  if ZBDSQR did not converge, INFO specifies how many superdiagonals  
> of an intermediate bidiagonal form B (computed in ZGESVD) did not  
> converge to zero.  
  
