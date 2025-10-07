```fortran  
subroutine zgees (  
jobvs,  
sort,  
select,  
n,  
a,  
lda,  
sdim,  
w,  
vs,  
*                         ldvs,  
work,  
lwork,  
rwork,  
bwork,  
info  
)  
```  
  
ZGEES computes for an N-by-N complex nonsymmetric matrix A, the  
eigenvalues, the Schur form T, and, optionally, the matrix of Schur  
vectors Z.  This gives the Schur factorization A = Z*T*(Z**H).  
  
Optionally, it also orders the eigenvalues on the diagonal of the  
Schur form so that selected eigenvalues are at the top left.  
The leading columns of Z then form an orthonormal basis for the  
invariant subspace corresponding to the selected eigenvalues.  
  
A complex matrix is in Schur form if it is upper triangular.  
  
## Parameters  
Jobvs : Character*1 [in]  
> = 'N': Schur vectors are not computed;  
> = 'V': Schur vectors are computed.  
  
Sort : Character*1 [in]  
> Specifies whether or not to order the eigenvalues on the  
> diagonal of the Schur form.  
> = 'N': Eigenvalues are not ordered:  
> = 'S': Eigenvalues are ordered (see SELECT).  
  
Select : a Logical Function of One Complex*16 Argument [in]  
> SELECT must be declared EXTERNAL in the calling subroutine.  
> If SORT = 'S', SELECT is used to select eigenvalues to order  
> to the top left of the Schur form.  
> IF SORT = 'N', SELECT is not referenced.  
> The eigenvalue W(j) is selected if SELECT(W(j)) is true.  
  
N : Integer [in]  
> The order of the matrix A. N >= 0.  
  
A : Complex*16 Array, Dimension (lda,n) [in,out]  
> On entry, the N-by-N matrix A.  
> On exit, A has been overwritten by its Schur form T.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Sdim : Integer [out]  
> If SORT = 'N', SDIM = 0.  
> If SORT = 'S', SDIM = number of eigenvalues for which  
> SELECT is true.  
  
W : Complex*16 Array, Dimension (n) [out]  
> W contains the computed eigenvalues, in the same order that  
> they appear on the diagonal of the output Schur form T.  
  
Vs : Complex*16 Array, Dimension (ldvs,n) [out]  
> If JOBVS = 'V', VS contains the unitary matrix Z of Schur  
> vectors.  
> If JOBVS = 'N', VS is not referenced.  
  
Ldvs : Integer [in]  
> The leading dimension of the array VS.  LDVS >= 1; if  
> JOBVS = 'V', LDVS >= N.  
  
Work : Complex*16 Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> For good performance, LWORK must generally be larger.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Rwork : Double Precision Array, Dimension (n) [out]  
  
Bwork : Logical Array, Dimension (n) [out]  
> Not referenced if SORT = 'N'.  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value.  
> > 0: if INFO = i, and i is  
> <= N:  the QR algorithm failed to compute all the  
> eigenvalues; elements 1:ILO-1 and i+1:N of W  
> contain those eigenvalues which have converged;  
> if JOBVS = 'V', VS contains the matrix which  
> reduces A to its partially converged Schur form.  
> = N+1: the eigenvalues could not be reordered because  
> some eigenvalues were too close to separate (the  
> problem is very ill-conditioned);  
> = N+2: after reordering, roundoff changed values of  
> some complex eigenvalues so that leading  
> eigenvalues in the Schur form no longer satisfy  
> SELECT = .TRUE..  This could also be caused by  
> underflow due to scaling.  
  
