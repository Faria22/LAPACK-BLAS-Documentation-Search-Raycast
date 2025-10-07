```fortran  
subroutine zgesvj (  
joba,  
jobu,  
jobv,  
m,  
n,  
a,  
lda,  
sva,  
mv,  
v,  
*                          ldv,  
cwork,  
lwork,  
rwork,  
lrwork,  
info  
)  
```  
  
ZGESVJ computes the singular value decomposition (SVD) of a complex  
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
> Specifies the structure of A.  
> = 'L': The input matrix A is lower triangular;  
> = 'U': The input matrix A is upper triangular;  
> = 'G': The input matrix A is general M-by-N matrix, M >= N.  
  
Jobu : Character*1 [in]  
> Specifies whether to compute the left singular vectors  
> (columns of U):  
> = 'U' or 'F': The left singular vectors corresponding to the nonzero  
> singular values are computed and returned in the leading  
> columns of A. See more details in the description of A.  
> The default numerical orthogonality threshold is set to  
> = 'C': Analogous to JOBU='U', except that user can control the  
> level of numerical orthogonality of the computed left  
> CTOL is given on input in the array WORK.  
> No CTOL smaller than ONE is allowed. CTOL greater  
> than 1 / EPS is meaningless. The option 'C'  
> of the computed left singular vectors, so CTOL=M could  
> save few sweeps of Jacobi rotations.  
> See the descriptions of A and WORK(1).  
> = 'N': The matrix U is not computed. However, see the  
> description of A.  
  
Jobv : Character*1 [in]  
> Specifies whether to compute the right singular vectors, that  
> is, the matrix V:  
> = 'V' or 'J': the matrix V is computed and returned in the array V  
> = 'A':  the Jacobi rotations are applied to the MV-by-N  
> array V. In other words, the right singular vector  
> matrix V is not computed explicitly; instead it is  
> applied to an MV-by-N matrix initially stored in the  
> first MV rows of V.  
> = 'N':  the matrix V is not computed and the array V is not  
> referenced  
  
M : Integer [in]  
> The number of rows of the input matrix A. 1/DLAMCH('E') > M >= 0.  
  
N : Integer [in]  
> The number of columns of the input matrix A.  
> M >= N >= 0.  
  
A : Complex*16 Array, Dimension (lda,n) [in,out]  
> On entry, the M-by-N matrix A.  
> On exit,  
> If JOBU = 'U' .OR. JOBU = 'C':  
> If INFO = 0 :  
> RANKA orthonormal columns of U are returned in the  
> leading RANKA columns of the array A. Here RANKA <= N  
> is the number of computed singular values of A that are  
> above the underflow threshold DLAMCH('S'). The singular  
> vectors corresponding to underflowed or zero singular  
> values are not computed. The value of RANKA is returned  
> in the array RWORK as RANKA=NINT(RWORK(2)). Also see the  
> descriptions of SVA and RWORK. The computed columns of U  
> are mutually numerically orthogonal up to approximately  
> see the description of JOBU.  
> If INFO > 0,  
> the procedure ZGESVJ did not converge in the given number  
> of iterations (sweeps). In that case, the computed  
> columns of U may not be orthogonal up to TOL. The output  
> U (stored in A), SIGMA (given by the computed singular  
> values in SVA(1:N)) and V is still a decomposition of the  
> input matrix A in the sense that the residual  
> If JOBU = 'N':  
> If INFO = 0 :  
> Note that the left singular vectors are 'for free' in the  
> one-sided Jacobi SVD algorithm. However, if only the  
> singular values are needed, the level of numerical  
> orthogonality of U is not an issue and iterations are  
> stopped when the columns of the iterated matrix are  
> on exit, A contains the columns of U scaled with the  
> corresponding singular values.  
> If INFO > 0:  
> the procedure ZGESVJ did not converge in the given number  
> of iterations (sweeps).  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,M).  
  
Sva : Double Precision Array, Dimension (n) [out]  
> On exit,  
> If INFO = 0 :  
> depending on the value SCALE = RWORK(1), we have:  
> If SCALE = ONE:  
> SVA(1:N) contains the computed singular values of A.  
> During the computation SVA contains the Euclidean column  
> norms of the iterated matrices in the array A.  
> If SCALE .NE. ONE:  
> factored representation is due to the fact that some of the  
> singular values of A might underflow or overflow.  
> If INFO > 0:  
> the procedure ZGESVJ did not converge in the given number of  
  
Mv : Integer [in]  
> If JOBV = 'A', then the product of Jacobi rotations in ZGESVJ  
> is applied to the first MV rows of V. See the description of JOBV.  
  
V : Complex*16 Array, Dimension (ldv,n) [in,out]  
> If JOBV = 'V', then V contains on exit the N-by-N matrix of  
> the right singular vectors;  
> If JOBV = 'A', then V contains the product of the computed right  
> singular vector matrix and the initial matrix in  
> the array V.  
> If JOBV = 'N', then V is not referenced.  
  
Ldv : Integer [in]  
> The leading dimension of the array V, LDV >= 1.  
> If JOBV = 'V', then LDV >= MAX(1,N).  
> If JOBV = 'A', then LDV >= MAX(1,MV) .  
  
Cwork : Complex*16 Array, Dimension (max(1,lwork)) [in,out]  
> Used as workspace.  
  
Lwork : Integer. [in]  
> Length of CWORK.  
> LWORK >= 1, if MIN(M,N) = 0, and LWORK >= M+N, otherwise.  
> If on entry LWORK = -1, then a workspace query is assumed and  
> no computation is done; CWORK(1) is set to the minial (and optimal)  
> length of CWORK.  
  
Rwork : Double Precision Array, Dimension (max(6,lrwork)) [in,out]  
> On entry,  
> If JOBU = 'C' :  
> RWORK(1) = CTOL, where CTOL defines the threshold for convergence.  
> The process stops if all columns of A are mutually  
> It is required that CTOL >= ONE, i.e. it is not  
> allowed to force the routine to obtain orthogonality  
> below EPSILON.  
> On exit,  
> are the computed singular values of A.  
> (See description of SVA().)  
> RWORK(2) = NINT(RWORK(2)) is the number of the computed nonzero  
> singular values.  
> RWORK(3) = NINT(RWORK(3)) is the number of the computed singular  
> values that are larger than the underflow threshold.  
> RWORK(4) = NINT(RWORK(4)) is the number of sweeps of Jacobi  
> rotations needed for numerical convergence.  
> RWORK(5) = max_{i.NE.j} |COS(A(:,i),A(:,j))| in the last sweep.  
> This is useful information in cases when ZGESVJ did  
> not converge, as it can be used to estimate whether  
> the output is still useful and for post festum analysis.  
> RWORK(6) = the largest absolute value over all sines of the  
> Jacobi rotation angles in the last sweep. It can be  
> useful for a post festum analysis.  
  
Lrwork : Integer [in]  
> Length of RWORK.  
> LRWORK >= 1, if MIN(M,N) = 0, and LRWORK >= MAX(6,N), otherwise.  
> If on entry LRWORK = -1, then a workspace query is assumed and  
> no computation is done; RWORK(1) is set to the minial (and optimal)  
> length of RWORK.  
  
Info : Integer [out]  
> = 0:  successful exit.  
> < 0:  if INFO = -i, then the i-th argument had an illegal value  
> > 0:  ZGESVJ did not converge in the maximal allowed number  
> (NSWEEP=30) of sweeps. The output may still be useful.  
> See the description of RWORK.  
  
