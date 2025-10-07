```fortran  
subroutine sla_gerfsx_extended (  
prec_type,  
trans_type,  
n,  
nrhs,  
a,  
*                                       lda,  
af,  
ldaf,  
ipiv,  
colequ,  
c,  
b,  
*                                       ldb,  
y,  
ldy,  
berr_out,  
n_norms,  
*                                       errs_n,  
errs_c,  
res,  
*                                       ayb,  
dy,  
y_tail,  
rcond,  
ithresh,  
*                                       rthresh,  
dz_ub,  
ignore_cwise,  
*                                       info  
)  
```  
  
SLA_GERFSX_EXTENDED improves the computed solution to a system of  
linear equations by performing extra-precise iterative refinement  
and provides error bounds and backward error estimates for the solution.  
This subroutine is called by SGERFSX to perform iterative refinement.  
In addition to normwise error bound, the code provides maximum  
componentwise error bound if possible. See comments for ERRS_N  
and ERRS_C for details of the error bounds. Note that this  
subroutine is only responsible for setting the second fields of  
ERRS_N and ERRS_C.  
  
## Parameters  
Prec_type : Integer [in]  
> Specifies the intermediate precision to be used in refinement.  
> The value is defined by ILAPREC(P) where P is a CHARACTER and P  
> = 'S':  Single  
> = 'D':  Double  
> = 'I':  Indigenous  
> = 'X' or 'E':  Extra  
  
Trans_type : Integer [in]  
> Specifies the transposition operation on A.  
> The value is defined by ILATRANS(T) where T is a CHARACTER and T  
> = 'N':  No transpose  
> = 'T':  Transpose  
> = 'C':  Conjugate transpose  
  
N : Integer [in]  
> The number of linear equations, i.e., the order of the  
> matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right-hand-sides, i.e., the number of columns of the  
> matrix B.  
  
A : Real Array, Dimension (lda,n) [in]  
> On entry, the N-by-N matrix A.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Af : Real Array, Dimension (ldaf,n) [in]  
> The factors L and U from the factorization  
  
Ldaf : Integer [in]  
> The leading dimension of the array AF.  LDAF >= max(1,N).  
  
Ipiv : Integer Array, Dimension (n) [in]  
> as computed by SGETRF; row i of the matrix was interchanged  
> with row IPIV(i).  
  
Colequ : Logical [in]  
> If .TRUE. then column equilibration was done to A before calling  
> this routine. This is needed to compute the solution and error  
> bounds correctly.  
  
C : Real Array, Dimension (n) [in]  
> The column scale factors for A. If COLEQU = .FALSE., C  
> is not accessed. If C is input, each element of C should be a power  
> of the radix to ensure a reliable solution and error estimates.  
> Scaling by powers of the radix does not cause rounding errors unless  
> the result underflows or overflows. Rounding errors during scaling  
> lead to refining with a matrix that is not equivalent to the  
> input matrix, producing error estimates that may not be  
> reliable.  
  
B : Real Array, Dimension (ldb,nrhs) [in]  
> The right-hand-side matrix B.  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(1,N).  
  
Y : Real Array, Dimension (ldy,nrhs) [in,out]  
> On entry, the solution matrix X, as computed by SGETRS.  
> On exit, the improved solution matrix Y.  
  
Ldy : Integer [in]  
> The leading dimension of the array Y.  LDY >= max(1,N).  
  
Berr_out : Real Array, Dimension (nrhs) [out]  
> On exit, BERR_OUT(j) contains the componentwise relative backward  
> error for right-hand-side j from the formula  
> where abs(Z) is the componentwise absolute value of the matrix  
> or vector Z. This is computed by SLA_LIN_BERR.  
  
N_norms : Integer [in]  
> Determines which error bounds to return (see ERRS_N  
> and ERRS_C).  
> If N_NORMS >= 1 return normwise error bounds.  
> If N_NORMS >= 2 return componentwise error bounds.  
  
Errs_n : Real Array, Dimension (nrhs, N_err_bnds) [in,out]  
> For each right-hand side, this array contains information about  
> various error bounds and condition numbers corresponding to the  
> normwise relative error, which is defined as follows:  
> Normwise relative error in the ith solution vector:  
> max_j (abs(XTRUE(j,i) - X(j,i)))  
> ------------------------------  
> max_j abs(X(j,i))  
> The array is indexed by the type of error information as described  
> below. There currently are up to three pieces of information  
> returned.  
> The first index in ERRS_N(i,:) corresponds to the ith  
> right-hand side.  
> The second index in ERRS_N(:,err) contains the following  
> three fields:  
> err = 1 "Trust/don't trust" boolean. Trust the answer if the  
> reciprocal condition number is less than the threshold  
> err = 2 "Guaranteed" error bound: The estimated forward error,  
> almost certainly within a factor of 10 of the true error  
> so long as the next entry is greater than the threshold  
> be trusted if the previous boolean is true.  
> err = 3  Reciprocal condition number: Estimated normwise  
> reciprocal condition number.  Compared with the threshold  
> estimate is "guaranteed". These reciprocal condition  
> appropriately scaled matrix Z.  
> radix so all absolute row sums of Z are approximately 1.  
> This subroutine is only responsible for setting the second field  
> above.  
> See Lapack Working Note 165 for further details and extra  
> cautions.  
  
Errs_c : Real Array, Dimension (nrhs, N_err_bnds) [in,out]  
> For each right-hand side, this array contains information about  
> various error bounds and condition numbers corresponding to the  
> componentwise relative error, which is defined as follows:  
> Componentwise relative error in the ith solution vector:  
> abs(XTRUE(j,i) - X(j,i))  
> max_j ----------------------  
> abs(X(j,i))  
> The array is indexed by the right-hand side i (on which the  
> componentwise relative error depends), and the type of error  
> information as described below. There currently are up to three  
> pieces of information returned for each right-hand side. If  
> componentwise accuracy is not requested (PARAMS(3) = 0.0), then  
> ERRS_C is not accessed.  If N_ERR_BNDS < 3, then at most  
> the first (:,N_ERR_BNDS) entries are returned.  
> The first index in ERRS_C(i,:) corresponds to the ith  
> right-hand side.  
> The second index in ERRS_C(:,err) contains the following  
> three fields:  
> err = 1 "Trust/don't trust" boolean. Trust the answer if the  
> reciprocal condition number is less than the threshold  
> err = 2 "Guaranteed" error bound: The estimated forward error,  
> almost certainly within a factor of 10 of the true error  
> so long as the next entry is greater than the threshold  
> be trusted if the previous boolean is true.  
> err = 3  Reciprocal condition number: Estimated componentwise  
> reciprocal condition number.  Compared with the threshold  
> estimate is "guaranteed". These reciprocal condition  
> appropriately scaled matrix Z.  
> current right-hand side and S scales each row of  
> sums of Z are approximately 1.  
> This subroutine is only responsible for setting the second field  
> above.  
> See Lapack Working Note 165 for further details and extra  
> cautions.  
  
Res : Real Array, Dimension (n) [in]  
> Workspace to hold the intermediate residual.  
  
Ayb : Real Array, Dimension (n) [in]  
> Workspace. This can be the same workspace passed for Y_TAIL.  
  
Dy : Real Array, Dimension (n) [in]  
> Workspace to hold the intermediate solution.  
  
Y_tail : Real Array, Dimension (n) [in]  
> Workspace to hold the trailing bits of the intermediate solution.  
  
Rcond : Real [in]  
> Reciprocal scaled condition number.  This is an estimate of the  
> reciprocal Skeel condition number of the matrix A after  
> equilibration (if done).  If this is less than the machine  
> precision (in particular, if it is zero), the matrix is singular  
> to working precision.  Note that the error may still be small even  
> if this number is very small and the matrix appears ill-  
> conditioned.  
  
Ithresh : Integer [in]  
> The maximum number of residual computations allowed for  
> refinement. The default is 10. For 'aggressive' set to 100 to  
> permit convergence using approximate factorizations or  
> factorizations other than LU. If the factorization uses a  
> technique other than Gaussian elimination, the guarantees in  
> ERRS_N and ERRS_C may no longer be trustworthy.  
  
Rthresh : Real [in]  
> Determines when to stop refinement if the error estimate stops  
> decreasing. Refinement will stop when the next solution no longer  
> the infinity norm of Z. RTHRESH satisfies 0 < RTHRESH <= 1. The  
> default value is 0.5. For 'aggressive' set to 0.9 to permit  
> convergence on extremely ill-conditioned matrices. See LAWN 165  
> for more details.  
  
Dz_ub : Real [in]  
> Determines when to start considering componentwise convergence.  
> Componentwise convergence is only considered after each component  
> of the solution Y is stable, which we define as the relative  
> change in each component being less than DZ_UB. The default value  
> is 0.25, requiring the first bit to be stable. See LAWN 165 for  
> more details.  
  
Ignore_cwise : Logical [in]  
> If .TRUE. then ignore componentwise convergence. Default value  
> is .FALSE..  
  
Info : Integer [out]  
> = 0:  Successful exit.  
> < 0:  if INFO = -i, the ith argument to SGETRS had an illegal  
> value  
  
