```fortran  
subroutine zgejsv (  
joba,  
jobu,  
jobv,  
jobr,  
jobt,  
jobp,  
*                         m,  
n,  
a,  
lda,  
sva,  
u,  
ldu,  
v,  
ldv,  
*                         cwork,  
lwork,  
rwork,  
lrwork,  
iwork,  
info  
)  
```  
  
ZGEJSV computes the singular value decomposition (SVD) of a complex M-by-N  
matrix [A], where M >= N. The SVD of [A] is written as  
  
[A] = [U] * [SIGMA] * [V]^*,  
  
where [SIGMA] is an N-by-N (M-by-N) matrix which is zero except for its N  
diagonal elements, [U] is an M-by-N (or M-by-M) unitary matrix, and  
[V] is an N-by-N unitary matrix. The diagonal elements of [SIGMA] are  
the singular values of [A]. The columns of [U] and [V] are the left and  
the right singular vectors of [A], respectively. The matrices [U] and [V]  
are computed and stored in the arrays U and V, respectively. The diagonal  
of [SIGMA] is computed and stored in the array SVA.  
  
## Parameters  
Joba : Character*1 [in]  
> Specifies the level of accuracy:  
> with well-conditioned B and arbitrary diagonal matrix D.  
> The accuracy cannot be spoiled by COLUMN scaling. The  
> accuracy of the computed output depends on the condition of  
> B, and the procedure aims at the best theoretical accuracy.  
> The relative error max_{i=1:N}|d sigma_i| / sigma_i is  
> The input matrix is preprocessed with the QRF with column  
> pivoting. This initial preprocessing and preconditioning by  
> a rank revealing QR factorization is common for all values of  
> JOBA. Additional actions are specified as follows:  
> = 'E': Computation as with 'C' with an additional estimate of the  
> condition number of B. It provides a realistic error bound.  
> D1, D2, and well-conditioned matrix C, this option gives  
> higher accuracy than the 'C' option. If the structure of the  
> input matrix is not known, and relative accuracy is  
> desirable, then this option is advisable. The input matrix A  
> is preprocessed with QR factorization with FULL (row and  
> column) pivoting.  
> = 'G': Computation as with 'F' with an additional estimate of the  
> rows, then using this condition number gives too pessimistic  
> error bound.  
> = 'A': Small singular values are not well determined by the data  
> and are considered as noisy; the matrix is treated as  
> numerically rank deficient. The error in the computed  
> This gives the procedure the licence to discard (set to zero)  
> = 'R': Similar as in 'A'. Rank revealing property of the initial  
> QR factorization is used do reveal (using triangular factor)  
> numerical RANK is declared to be r. The SVD is computed with  
> absolute error bounds, but more accurately than with 'A'.  
  
Jobu : Character*1 [in]  
> Specifies whether to compute the columns of U:  
> = 'U': N columns of U are returned in the array U.  
> = 'F': full set of M left sing. vectors is returned in the array U.  
> of U.  
> = 'N': U is not computed.  
  
Jobv : Character*1 [in]  
> Specifies whether to compute the matrix V:  
> = 'V': N columns of V are returned in the array V; Jacobi rotations  
> are not explicitly accumulated.  
> = 'J': N columns of V are returned in the array V, but they are  
> computed as the product of Jacobi rotations, if JOBT = 'N'.  
> of V.  
> = 'N': V is not computed.  
  
Jobr : Character*1 [in]  
> Specifies the RANGE for the singular values. Issues the licence to  
> set to zero small positive singular values if they are outside  
> specified range. If A .NE. 0 is scaled so that the largest singular  
> SQRT(SFMIN) (for JOBR = 'R'), or less than SMALL=SFMIN/EPSLN,  
> where SFMIN=DLAMCH('S'), EPSLN=DLAMCH('E').  
> BLAS and QR factorizations and triangular solvers are  
> implemented to work in that range. If the condition of A  
> is greater than BIG, use ZGESVJ.  
> (roughly, as described above). This option is recommended.  
> ===========================  
> For computing the singular values in the FULL range [SFMIN,BIG]  
> use ZGESVJ.  
  
Jobt : Character*1 [in]  
> If the matrix is square then the procedure may determine to use  
> If the matrix is not square, JOBT is ignored.  
> The decision is based on two values of entropy over the adjoint  
> = 'T': transpose if entropy test indicates possibly faster  
> = 'N': do not speculate.  
> The option 'T' can be used to compute only the singular values, or  
> the full SVD (U, SIGMA and V). For only one set of singular vectors  
> (U or V), the caller should provide both U and V, as one of the  
> matrices is used as workspace if the matrix A is transposed.  
> The implementer can easily remove this constraint and make the  
> code more complicated. See the descriptions of U and V.  
> In general, this option is considered experimental, and 'N'; should  
> be preferred. This is subject to changes in the future.  
  
Jobp : Character*1 [in]  
> Issues the licence to introduce structured perturbations to drown  
> denormalized numbers. This licence should be active if the  
> denormals are poorly implemented, causing slow computation,  
> especially in cases of fast convergence (!). For details see [1,2].  
> For the sake of simplicity, this perturbations are included only  
> when the full SVD or only the singular values are requested. The  
> implementer/user can easily add the perturbation for the cases of  
> computing one set of singular vectors.  
> = 'P': introduce perturbation  
> = 'N': do not perturb  
  
M : Integer [in]  
> The number of rows of the input matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the input matrix A. M >= N >= 0.  
  
A : Complex*16 Array, Dimension (lda,n) [in,out]  
> On entry, the M-by-N matrix A.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
Sva : Double Precision Array, Dimension (n) [out]  
> On exit,  
> - For RWORK(1)/RWORK(2) = ONE: The singular values of A. During  
> the computation SVA contains Euclidean column norms of the  
> iterated matrices in the array A.  
> - For RWORK(1) .NE. RWORK(2): The singular values of A are  
> sigma_max(A) overflows or if small singular values have been  
> saved from underflow by scaling the input matrix A.  
> - If JOBR='R' then some of the singular values may be returned  
> as exact zeros obtained by "set to zero" because they are  
> below the numerical rank threshold or are denormalized numbers.  
  
U : Complex*16 Array, Dimension ( Ldu, N ) [out]  
> If JOBU = 'U', then U contains on exit the M-by-N matrix of  
> the left singular vectors.  
> If JOBU = 'F', then U contains on exit the M-by-M matrix of  
> the left singular vectors, including an ONB  
> of the orthogonal complement of the Range(A).  
> If JOBU = 'W'  .AND. (JOBV = 'V' .AND. JOBT = 'T' .AND. M = N),  
> then U is used as workspace if the procedure  
> copied back to the V array. This 'W' option is just  
> a reminder to the caller that in this case U is  
> If JOBU = 'N'  U is not referenced, unless JOBT='T'.  
  
Ldu : Integer [in]  
> The leading dimension of the array U,  LDU >= 1.  
> IF  JOBU = 'U' or 'F' or 'W',  then LDU >= M.  
  
V : Complex*16 Array, Dimension ( Ldv, N ) [out]  
> If JOBV = 'V', 'J' then V contains on exit the N-by-N matrix of  
> the right singular vectors;  
> If JOBV = 'W', AND (JOBU = 'U' AND JOBT = 'T' AND M = N),  
> then V is used as workspace if the procedure  
> copied back to the U array. This 'W' option is just  
> a reminder to the caller that in this case V is  
> If JOBV = 'N'  V is not referenced, unless JOBT='T'.  
  
Ldv : Integer [in]  
> The leading dimension of the array V,  LDV >= 1.  
> If JOBV = 'V' or 'J' or 'W', then LDV >= N.  
  
Cwork : Complex*16 Array, Dimension (max(2,lwork)) [out]  
> If the call to ZGEJSV is a workspace query (indicated by LWORK=-1 or  
> LRWORK=-1), then on exit CWORK(1) contains the required length of  
> CWORK for the job parameters used in the call.  
  
Lwork : Integer [in]  
> Length of CWORK to confirm proper allocation of workspace.  
> LWORK depends on the job:  
> 1. If only SIGMA is needed ( JOBU = 'N', JOBV = 'N' ) and  
> 1.1 .. no scaled condition estimate required (JOBA.NE.'E'.AND.JOBA.NE.'G'):  
> ->> For optimal performance (blocked code) the optimal value  
> block size for ZGEQP3 and ZGEQRF.  
> In general, optimal LWORK is computed as  
> LWORK >= max(N+LWORK(ZGEQP3),N+LWORK(ZGEQRF), LWORK(ZGESVJ)).  
> 1.2. .. an estimate of the scaled condition number of A is  
> required (JOBA='E', or 'G'). In this case, LWORK the minimal  
> ->> For optimal performance (blocked code) the optimal value  
> In general, the optimal length LWORK is computed as  
> LWORK >= max(N+LWORK(ZGEQP3),N+LWORK(ZGEQRF), LWORK(ZGESVJ),  
> 2. If SIGMA and the right singular vectors are needed (JOBV = 'V'),  
> (JOBU = 'N')  
> 2.1   .. no scaled condition estimate requested (JOBE = 'N'):  
> -> For optimal performance,  
> where NB is the optimal block size for ZGEQP3, ZGEQRF, ZGELQF,  
> ZUNMLQ. In general, the optimal length LWORK is computed as  
> LWORK >= max(N+LWORK(ZGEQP3), N+LWORK(ZGESVJ),  
> 2.2 .. an estimate of the scaled condition number of A is  
> required (JOBA='E', or 'G').  
> -> For optimal performance,  
> where NB is the optimal block size for ZGEQP3, ZGEQRF, ZGELQF,  
> ZUNMLQ. In general, the optimal length LWORK is computed as  
> LWORK >= max(N+LWORK(ZGEQP3), LWORK(ZPOCON), N+LWORK(ZGESVJ),  
> 3. If SIGMA and the left singular vectors are needed  
> 3.1  .. no scaled condition estimate requested (JOBE = 'N'):  
> -> For optimal performance:  
> where NB is the optimal block size for ZGEQP3, ZGEQRF, ZUNMQR.  
> In general, the optimal length LWORK is computed as  
> 3.2  .. an estimate of the scaled condition number of A is  
> required (JOBA='E', or 'G').  
> -> For optimal performance:  
> where NB is the optimal block size for ZGEQP3, ZGEQRF, ZUNMQR.  
> In general, the optimal length LWORK is computed as  
> LWORK >= max(N+LWORK(ZGEQP3),N+LWORK(ZPOCON),  
> 4. If the full SVD is needed: (JOBU = 'U' or JOBU = 'F') and  
> 4.1. if JOBV = 'V'  
> 4.2. if JOBV = 'J' the minimal requirement is  
> In both cases, the allocated CWORK can accommodate blocked runs  
> of ZGEQP3, ZGEQRF, ZGELQF, SUNMQR, ZUNMLQ.  
> If the call to ZGEJSV is a workspace query (indicated by LWORK=-1 or  
> LRWORK=-1), then on exit CWORK(1) contains the optimal and CWORK(2) contains the  
> minimal length of CWORK for the job parameters used in the call.  
  
Rwork : Double Precision Array, Dimension (max(7,lrwork)) [out]  
> On exit,  
> RWORK(1) = Determines the scaling factor SCALE = RWORK(2) / RWORK(1)  
> of A. (See the description of SVA().)  
> RWORK(2) = See the description of RWORK(1).  
> RWORK(3) = SCONDA is an estimate for the condition number of  
> column equilibrated A. (If JOBA = 'E' or 'G')  
> It is computed using ZPOCON. It holds  
> where R is the triangular factor from the QRF of A.  
> However, if R is truncated and the numerical rank is  
> determined to be strictly smaller than N, SCONDA is  
> returned as -1, thus indicating that the smallest  
> singular values might be lost.  
> If full SVD is needed, the following two condition numbers are  
> useful for the analysis of the algorithm. They are provided for  
> a developer/implementer who is familiar with the details of  
> the method.  
> RWORK(4) = an estimate of the scaled condition number of the  
> triangular factor in the first QR factorization.  
> RWORK(5) = an estimate of the scaled condition number of the  
> triangular factor in the second QR factorization.  
> The following two parameters are computed if JOBT = 'T'.  
> They are provided for a developer/implementer who is familiar  
> with the details of the method.  
> probability simplex.  
> If the call to ZGEJSV is a workspace query (indicated by LWORK=-1 or  
> LRWORK=-1), then on exit RWORK(1) contains the required length of  
> RWORK for the job parameters used in the call.  
  
Lrwork : Integer [in]  
> Length of RWORK to confirm proper allocation of workspace.  
> LRWORK depends on the job:  
> 1. If only the singular values are requested i.e. if  
> LSAME(JOBU,'N') .AND. LSAME(JOBV,'N')  
> then:  
> 1.1. If LSAME(JOBT,'T') .OR. LSAME(JOBA,'F') .OR. LSAME(JOBA,'G'),  
> 1.2. Otherwise, LRWORK  = max( 7,  N ).  
> 2. If singular values with the right singular vectors are requested  
> i.e. if  
> (LSAME(JOBV,'V').OR.LSAME(JOBV,'J')) .AND.  
> .NOT.(LSAME(JOBU,'U').OR.LSAME(JOBU,'F'))  
> then:  
> 2.1. If LSAME(JOBT,'T') .OR. LSAME(JOBA,'F') .OR. LSAME(JOBA,'G'),  
> 2.2. Otherwise, LRWORK  = max( 7,  N ).  
> 3. If singular values with the left singular vectors are requested, i.e. if  
> (LSAME(JOBU,'U').OR.LSAME(JOBU,'F')) .AND.  
> .NOT.(LSAME(JOBV,'V').OR.LSAME(JOBV,'J'))  
> then:  
> 3.1. If LSAME(JOBT,'T') .OR. LSAME(JOBA,'F') .OR. LSAME(JOBA,'G'),  
> 3.2. Otherwise, LRWORK  = max( 7,  N ).  
> 4. If singular values with both the left and the right singular vectors  
> are requested, i.e. if  
> (LSAME(JOBU,'U').OR.LSAME(JOBU,'F')) .AND.  
> (LSAME(JOBV,'V').OR.LSAME(JOBV,'J'))  
> then:  
> 4.1. If LSAME(JOBT,'T') .OR. LSAME(JOBA,'F') .OR. LSAME(JOBA,'G'),  
> 4.2. Otherwise, LRWORK  = max( 7, N ).  
> If, on entry, LRWORK = -1 or LWORK=-1, a workspace query is assumed and  
> the length of RWORK is returned in RWORK(1).  
  
Iwork : Integer Array, of Dimension At Least 4, That Further Depends [out]  
> on the job:  
> 1. If only the singular values are requested then:  
> If ( LSAME(JOBT,'T') .OR. LSAME(JOBA,'F') .OR. LSAME(JOBA,'G') )  
> then the length of IWORK is N+M; otherwise the length of IWORK is N.  
> 2. If the singular values and the right singular vectors are requested then:  
> If ( LSAME(JOBT,'T') .OR. LSAME(JOBA,'F') .OR. LSAME(JOBA,'G') )  
> then the length of IWORK is N+M; otherwise the length of IWORK is N.  
> 3. If the singular values and the left singular vectors are requested then:  
> If ( LSAME(JOBT,'T') .OR. LSAME(JOBA,'F') .OR. LSAME(JOBA,'G') )  
> then the length of IWORK is N+M; otherwise the length of IWORK is N.  
> 4. If the singular values with both the left and the right singular vectors  
> are requested, then:  
> 4.1. If LSAME(JOBV,'J') the length of IWORK is determined as follows:  
> If ( LSAME(JOBT,'T') .OR. LSAME(JOBA,'F') .OR. LSAME(JOBA,'G') )  
> then the length of IWORK is N+M; otherwise the length of IWORK is N.  
> 4.2. If LSAME(JOBV,'V') the length of IWORK is determined as follows:  
> If ( LSAME(JOBT,'T') .OR. LSAME(JOBA,'F') .OR. LSAME(JOBA,'G') )  
> On exit,  
> IWORK(1) = the numerical rank determined after the initial  
> QR factorization with pivoting. See the descriptions  
> of JOBA and JOBR.  
> IWORK(2) = the number of the computed nonzero singular values  
> IWORK(3) = if nonzero, a warning message:  
> If IWORK(3) = 1 then some of the column norms of A  
> were denormalized floats. The requested high accuracy  
> is not warranted by the data.  
> do the job as specified by the JOB parameters.  
> If the call to ZGEJSV is a workspace query (indicated by LWORK = -1 or  
> LRWORK = -1), then on exit IWORK(1) contains the required length of  
> IWORK for the job parameters used in the call.  
  
Info : Integer [out]  
> < 0:  if INFO = -i, then the i-th argument had an illegal value.  
> = 0:  successful exit;  
> > 0:  ZGEJSV  did not converge in the maximal allowed number  
> of sweeps. The computed values may be inaccurate.  
  
