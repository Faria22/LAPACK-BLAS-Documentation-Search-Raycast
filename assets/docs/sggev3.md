```fortran  
subroutine sggev3 (  
jobvl,  
jobvr,  
n,  
a,  
lda,  
b,  
ldb,  
alphar,  
*      $                   alphai,  
beta,  
vl,  
ldvl,  
vr,  
ldvr,  
work,  
lwork,  
*      $                   info  
)  
```  
  
SGGEV3 computes for a pair of N-by-N real nonsymmetric matrices (A,B)  
the generalized eigenvalues, and optionally, the left and/or right  
generalized eigenvectors.  
  
A generalized eigenvalue for a pair of matrices (A,B) is a scalar  
lambda or a ratio alpha/beta = lambda, such that A - lambda*B is  
singular. It is usually represented as the pair (alpha,beta), as  
there is a reasonable interpretation for beta=0, and even for both  
being zero.  
  
The right eigenvector v(j) corresponding to the eigenvalue lambda(j)  
of (A,B) satisfies  
  
A * v(j) = lambda(j) * B * v(j).  
  
The left eigenvector u(j) corresponding to the eigenvalue lambda(j)  
of (A,B) satisfies  
  
u(j)**H * A  = lambda(j) * u(j)**H * B .  
  
where u(j)**H is the conjugate-transpose of u(j).  
  
  
## Parameters  
Jobvl : Character*1 [in]  
> = 'N':  do not compute the left generalized eigenvectors;  
> = 'V':  compute the left generalized eigenvectors.  
  
Jobvr : Character*1 [in]  
> = 'N':  do not compute the right generalized eigenvectors;  
> = 'V':  compute the right generalized eigenvectors.  
  
N : Integer [in]  
> The order of the matrices A, B, VL, and VR.  N >= 0.  
  
A : Real Array, Dimension (lda, N) [in,out]  
> On entry, the matrix A in the pair (A,B).  
> On exit, A has been overwritten.  
  
Lda : Integer [in]  
> The leading dimension of A.  LDA >= max(1,N).  
  
B : Real Array, Dimension (ldb, N) [in,out]  
> On entry, the matrix B in the pair (A,B).  
> On exit, B has been overwritten.  
  
Ldb : Integer [in]  
> The leading dimension of B.  LDB >= max(1,N).  
  
Alphar : Real Array, Dimension (n) [out]  
  
Alphai : Real Array, Dimension (n) [out]  
  
Beta : Real Array, Dimension (n) [out]  
> be the generalized eigenvalues.  If ALPHAI(j) is zero, then  
> the j-th eigenvalue is real; if positive, then the j-th and  
> (j+1)-st eigenvalues are a complex conjugate pair, with  
> ALPHAI(j+1) negative.  
> Note: the quotients ALPHAR(j)/BETA(j) and ALPHAI(j)/BETA(j)  
> may easily over- or underflow, and BETA(j) may even be zero.  
> Thus, the user should avoid naively computing the ratio  
> alpha/beta.  However, ALPHAR and ALPHAI will be always less  
> than and usually comparable with norm(A) in magnitude, and  
> BETA always less than and usually comparable with norm(B).  
  
Vl : Real Array, Dimension (ldvl,n) [out]  
> If JOBVL = 'V', the left eigenvectors u(j) are stored one  
> after another in the columns of VL, in the same order as  
> their eigenvalues. If the j-th eigenvalue is real, then  
> u(j) = VL(:,j), the j-th column of VL. If the j-th and  
> (j+1)-th eigenvalues form a complex conjugate pair, then  
> Each eigenvector is scaled so the largest component has  
> abs(real part)+abs(imag. part)=1.  
> Not referenced if JOBVL = 'N'.  
  
Ldvl : Integer [in]  
> The leading dimension of the matrix VL. LDVL >= 1, and  
> if JOBVL = 'V', LDVL >= N.  
  
Vr : Real Array, Dimension (ldvr,n) [out]  
> If JOBVR = 'V', the right eigenvectors v(j) are stored one  
> after another in the columns of VR, in the same order as  
> their eigenvalues. If the j-th eigenvalue is real, then  
> v(j) = VR(:,j), the j-th column of VR. If the j-th and  
> (j+1)-th eigenvalues form a complex conjugate pair, then  
> Each eigenvector is scaled so the largest component has  
> abs(real part)+abs(imag. part)=1.  
> Not referenced if JOBVR = 'N'.  
  
Ldvr : Integer [in]  
> The leading dimension of the matrix VR. LDVR >= 1, and  
> if JOBVR = 'V', LDVR >= N.  
  
Work : Real Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> For good performance, LWORK should generally be larger.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
> = 1,...,N:  
> The QZ iteration failed.  No eigenvectors have been  
> calculated, but ALPHAR(j), ALPHAI(j), and BETA(j)  
> should be correct for j=INFO+1,...,N.  
> > N:  =N+1: other than QZ iteration failed in SLAQZ0.  
> =N+2: error return from STGEVC.  
  
