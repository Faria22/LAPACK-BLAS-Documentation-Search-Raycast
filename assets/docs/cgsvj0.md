```fortran  
subroutine cgsvj0 (  
jobv,  
m,  
n,  
a,  
lda,  
d,  
sva,  
mv,  
v,  
ldv,  
eps,  
*                          sfmin,  
tol,  
nsweep,  
work,  
lwork,  
info  
)  
```  
  
CGSVJ0 is called from CGESVJ as a pre-processor and that is its main  
purpose. It applies Jacobi rotations in the same way as CGESVJ does, but  
it does not check convergence (stopping criterion). Few tuning  
parameters (marked by [TP]) are available for the implementer.  
  
## Parameters  
Jobv : Character*1 [in]  
> Specifies whether the output from this procedure is used  
> to compute the matrix V:  
> = 'V': the product of the Jacobi rotations is accumulated  
> by postmultiplying the N-by-N array V.  
> (See the description of V.)  
> = 'A': the product of the Jacobi rotations is accumulated  
> by postmultiplying the MV-by-N array V.  
> (See the descriptions of MV and V.)  
> = 'N': the Jacobi rotations are not accumulated.  
  
M : Integer [in]  
> The number of rows of the input matrix A.  M >= 0.  
  
N : Integer [in]  
> The number of columns of the input matrix A.  
> M >= N >= 0.  
  
A : Complex Array, Dimension (lda,n) [in,out]  
> the input matrix.  
> On exit,  
> post-multiplied by a sequence of Jacobi rotations, where the  
> rotation threshold and the total number of sweeps are given in  
> TOL and NSWEEP, respectively.  
> (See the descriptions of D, TOL and NSWEEP.)  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
D : Complex Array, Dimension (n) [in,out]  
> The array D accumulates the scaling factors from the complex scaled  
> Jacobi rotations.  
> post-multiplied by a sequence of Jacobi rotations, where the  
> rotation threshold and the total number of sweeps are given in  
> TOL and NSWEEP, respectively.  
> (See the descriptions of A, TOL and NSWEEP.)  
  
Sva : Real Array, Dimension (n) [in,out]  
> On entry, SVA contains the Euclidean norms of the columns of  
> On exit, SVA contains the Euclidean norms of the columns of  
  
Mv : Integer [in]  
> If JOBV = 'A', then MV rows of V are post-multiplied by a  
> sequence of Jacobi rotations.  
> If JOBV = 'N',   then MV is not referenced.  
  
V : Complex Array, Dimension (ldv,n) [in,out]  
> If JOBV = 'V' then N rows of V are post-multiplied by a  
> sequence of Jacobi rotations.  
> If JOBV = 'A' then MV rows of V are post-multiplied by a  
> sequence of Jacobi rotations.  
> If JOBV = 'N',   then V is not referenced.  
  
Ldv : Integer [in]  
> The leading dimension of the array V,  LDV >= 1.  
> If JOBV = 'V', LDV >= N.  
> If JOBV = 'A', LDV >= MV.  
  
Eps : Real [in]  
> EPS = SLAMCH('Epsilon')  
  
Sfmin : Real [in]  
> SFMIN = SLAMCH('Safe Minimum')  
  
Tol : Real [in]  
> TOL is the threshold for Jacobi rotations. For a pair  
> A(:,p), A(:,q) of pivot columns, the Jacobi rotation is  
> applied only if ABS(COS(angle(A(:,p),A(:,q)))) > TOL.  
  
Nsweep : Integer [in]  
> NSWEEP is the number of sweeps of Jacobi rotations to be  
> performed.  
  
Work : Complex Array, Dimension (lwork) [out]  
  
Lwork : Integer [in]  
> LWORK is the dimension of WORK. LWORK >= M.  
  
Info : Integer [out]  
> = 0:  successful exit.  
> < 0:  if INFO = -i, then the i-th argument had an illegal value  
  
