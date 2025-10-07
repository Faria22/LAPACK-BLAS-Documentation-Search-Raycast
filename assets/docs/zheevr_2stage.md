```fortran  
subroutine zheevr_2stage (  
jobz,  
range,  
uplo,  
n,  
a,  
lda,  
vl,  
vu,  
*                                 il,  
iu,  
abstol,  
m,  
w,  
z,  
ldz,  
isuppz,  
*                                 work,  
lwork,  
rwork,  
lrwork,  
iwork,  
*                                 liwork,  
info  
)  
```  
  
ZHEEVR_2STAGE computes selected eigenvalues and, optionally, eigenvectors  
of a complex Hermitian matrix A using the 2stage technique for  
the reduction to tridiagonal.  Eigenvalues and eigenvectors can  
be selected by specifying either a range of values or a range of  
indices for the desired eigenvalues.  
  
ZHEEVR_2STAGE first reduces the matrix A to tridiagonal form T with a call  
to ZHETRD.  Then, whenever possible, ZHEEVR_2STAGE calls ZSTEMR to compute  
eigenspectrum using Relatively Robust Representations.  ZSTEMR  
computes eigenvalues by the dqds algorithm, while orthogonal  
eigenvectors are computed from various "good" L D L^T representations  
(also known as Relatively Robust Representations). Gram-Schmidt  
orthogonalization is avoided as far as possible. More specifically,  
the various steps of the algorithm are as follows.  
  
For each unreduced block (submatrix) of T,  
(a) Compute T - sigma I  = L D L^T, so that L and D  
define all the wanted eigenvalues to high relative accuracy.  
This means that small relative changes in the entries of D and L  
cause only small relative changes in the eigenvalues and  
eigenvectors. The standard (unfactored) representation of the  
tridiagonal matrix T does not have this property in general.  
(b) Compute the eigenvalues to suitable accuracy.  
If the eigenvectors are desired, the algorithm attains full  
accuracy of the computed eigenvalues only right before  
the corresponding vectors have to be computed, see steps c) and d).  
(c) For each cluster of close eigenvalues, select a new  
shift close to the cluster, find a new factorization, and refine  
the shifted eigenvalues to suitable accuracy.  
(d) For each eigenvalue with a large enough relative separation compute  
the corresponding eigenvector by forming a rank revealing twisted  
factorization. Go back to (c) for any clusters that remain.  
  
The desired accuracy of the output can be specified by the input  
parameter ABSTOL.  
  
For more details, see ZSTEMR's documentation and:  
- Inderjit S. Dhillon and Beresford N. Parlett: "Multiple representations  
to compute orthogonal eigenvectors of symmetric tridiagonal matrices,"  
Linear Algebra and its Applications, 387(1), pp. 1-28, August 2004.  
- Inderjit Dhillon and Beresford Parlett: "Orthogonal Eigenvectors and  
Relative Gaps," SIAM Journal on Matrix Analysis and Applications, Vol. 25,  
2004.  Also LAPACK Working Note 154.  
- Inderjit Dhillon: "A new O(n^2) algorithm for the symmetric  
tridiagonal eigenvalue/eigenvector problem",  
Computer Science Division Technical Report No. UCB/CSD-97-971,  
UC Berkeley, May 1997.  
  
  
Note 1 : ZHEEVR_2STAGE calls ZSTEMR when the full spectrum is requested  
on machines which conform to the ieee-754 floating point standard.  
ZHEEVR_2STAGE calls DSTEBZ and ZSTEIN on non-ieee machines and  
when partial spectrum requests are made.  
  
Normal execution of ZSTEMR may create NaNs and infinities and  
hence may abort due to a floating point exception in environments  
which do not handle NaNs and infinities in the ieee standard default  
manner.  
  
## Parameters  
Jobz : Character*1 [in]  
> = 'N':  Compute eigenvalues only;  
> = 'V':  Compute eigenvalues and eigenvectors.  
> Not available in this release.  
  
Range : Character*1 [in]  
> = 'A': all eigenvalues will be found.  
> = 'V': all eigenvalues in the half-open interval (VL,VU]  
> will be found.  
> = 'I': the IL-th through IU-th eigenvalues will be found.  
> For RANGE = 'V' or 'I' and IU - IL < N - 1, DSTEBZ and  
> ZSTEIN are called  
  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
A : Complex*16 Array, Dimension (lda, N) [in,out]  
> On entry, the Hermitian matrix A.  If UPLO = 'U', the  
> leading N-by-N upper triangular part of A contains the  
> upper triangular part of the matrix A.  If UPLO = 'L',  
> the leading N-by-N lower triangular part of A contains  
> the lower triangular part of the matrix A.  
> On exit, the lower triangle (if UPLO='L') or the upper  
> triangle (if UPLO='U') of A, including the diagonal, is  
> destroyed.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Vl : Double Precision [in]  
> If RANGE='V', the lower bound of the interval to  
> be searched for eigenvalues. VL < VU.  
> Not referenced if RANGE = 'A' or 'I'.  
  
Vu : Double Precision [in]  
> If RANGE='V', the upper bound of the interval to  
> be searched for eigenvalues. VL < VU.  
> Not referenced if RANGE = 'A' or 'I'.  
  
Il : Integer [in]  
> If RANGE='I', the index of the  
> smallest eigenvalue to be returned.  
> 1 <= IL <= IU <= N, if N > 0; IL = 1 and IU = 0 if N = 0.  
> Not referenced if RANGE = 'A' or 'V'.  
  
Iu : Integer [in]  
> If RANGE='I', the index of the  
> largest eigenvalue to be returned.  
> 1 <= IL <= IU <= N, if N > 0; IL = 1 and IU = 0 if N = 0.  
> Not referenced if RANGE = 'A' or 'V'.  
  
Abstol : Double Precision [in]  
> The absolute error tolerance for the eigenvalues.  
> An approximate eigenvalue is accepted as converged  
> when it is determined to lie in an interval [a,b]  
> of width less than or equal to  
> where EPS is the machine precision.  If ABSTOL is less than  
> where |T| is the 1-norm of the tridiagonal matrix obtained  
> by reducing A to tridiagonal form.  
> See "Computing Small Singular Values of Bidiagonal Matrices  
> with Guaranteed High Relative Accuracy," by Demmel and  
> Kahan, LAPACK Working Note #3.  
> If high relative accuracy is important, set ABSTOL to  
> DLAMCH( 'Safe minimum' ).  Doing so will guarantee that  
> eigenvalues are computed to high relative accuracy when  
> possible in future releases.  The current code does not  
> make any guarantees about high relative accuracy, but  
> future releases will. See J. Barlow and J. Demmel,  
> "Computing Accurate Eigensystems of Scaled Diagonally  
> Dominant Matrices", LAPACK Working Note #7, for a discussion  
> of which matrices define their eigenvalues to high relative  
> accuracy.  
  
M : Integer [out]  
> The total number of eigenvalues found.  0 <= M <= N.  
> If RANGE = 'A', M = N, and if RANGE = 'I', M = IU-IL+1.  
  
W : Double Precision Array, Dimension (n) [out]  
> The first M elements contain the selected eigenvalues in  
> ascending order.  
  
Z : Complex*16 Array, Dimension (ldz, Max(1,m)) [out]  
> If JOBZ = 'V', then if INFO = 0, the first M columns of Z  
> contain the orthonormal eigenvectors of the matrix A  
> corresponding to the selected eigenvalues, with the i-th  
> column of Z holding the eigenvector associated with W(i).  
> If JOBZ = 'N', then Z is not referenced.  
> Note: the user must ensure that at least max(1,M) columns are  
> supplied in the array Z; if RANGE = 'V', the exact value of M  
> is not known in advance and an upper bound must be used.  
  
Ldz : Integer [in]  
> The leading dimension of the array Z.  LDZ >= 1, and if  
> JOBZ = 'V', LDZ >= max(1,N).  
  
Isuppz : Integer Array, Dimension ( 2*max(1,m) ) [out]  
> The support of the eigenvectors in Z, i.e., the indices  
> indicating the nonzero elements in Z. The i-th eigenvector  
> matrix). The support of the eigenvectors of A is typically  
> 1:N because of the unitary transformations applied by ZUNMTR.  
> Implemented only for RANGE = 'A' or 'I' and IU - IL = N - 1  
  
Work : Complex*16 Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK.  
> If N <= 1,               LWORK must be at least 1.  
> If JOBZ = 'N' and N > 1, LWORK must be queried.  
> where KD is the blocking size of the reduction,  
> FACTOPTNB is the blocking used by the QR or LQ  
> algorithm, usually FACTOPTNB=128 is a good choice  
> NTHREADS is the number of threads used when  
> openMP compilation is enabled, otherwise =1.  
> If JOBZ = 'V' and N > 1, LWORK must be queried. Not yet available  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal sizes of the WORK, RWORK and  
> IWORK arrays, returns these values as the first entries of  
> the WORK, RWORK and IWORK arrays, and no error message  
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.  
  
Rwork : Double Precision Array, Dimension (max(1,lrwork)) [out]  
> On exit, if INFO = 0, RWORK(1) returns the optimal  
> (and minimal) LRWORK.  
  
Lrwork : Integer [in]  
> The length of the array RWORK.  
> If LRWORK = -1, then a workspace query is assumed; the  
> routine only calculates the optimal sizes of the WORK, RWORK  
> and IWORK arrays, returns these values as the first entries  
> of the WORK, RWORK and IWORK arrays, and no error message  
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.  
  
Iwork : Integer Array, Dimension (max(1,liwork)) [out]  
> On exit, if INFO = 0, IWORK(1) returns the optimal  
> (and minimal) LIWORK.  
  
Liwork : Integer [in]  
> The dimension of the array IWORK.  
> If LIWORK = -1, then a workspace query is assumed; the  
> routine only calculates the optimal sizes of the WORK, RWORK  
> and IWORK arrays, returns these values as the first entries  
> of the WORK, RWORK and IWORK arrays, and no error message  
> related to LWORK or LRWORK or LIWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  Internal error  
  
