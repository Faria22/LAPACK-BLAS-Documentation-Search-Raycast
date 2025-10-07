```fortran  
subroutine sgeev (  
jobvl,  
jobvr,  
n,  
a,  
lda,  
wr,  
wi,  
vl,  
ldvl,  
vr,  
*                         ldvr,  
work,  
lwork,  
info  
)  
```  
  
SGEEV computes for an N-by-N real nonsymmetric matrix A, the  
eigenvalues and, optionally, the left and/or right eigenvectors.  
  
The right eigenvector v(j) of A satisfies  
A * v(j) = lambda(j) * v(j)  
where lambda(j) is its eigenvalue.  
The left eigenvector u(j) of A satisfies  
u(j)**H * A = lambda(j) * u(j)**H  
where u(j)**H denotes the conjugate-transpose of u(j).  
  
The computed eigenvectors are normalized to have Euclidean norm  
equal to 1 and largest component real.  
  
## Parameters  
Jobvl : Character*1 [in]  
> = 'N': left eigenvectors of A are not computed;  
> = 'V': left eigenvectors of A are computed.  
  
Jobvr : Character*1 [in]  
> = 'N': right eigenvectors of A are not computed;  
> = 'V': right eigenvectors of A are computed.  
  
N : Integer [in]  
> The order of the matrix A. N >= 0.  
  
A : Real Array, Dimension (lda,n) [in,out]  
> On entry, the N-by-N matrix A.  
> On exit, A has been overwritten.  
  
Lda : Integer [in]  
> The leading dimension of the array A.  LDA >= max(1,N).  
  
Wr : Real Array, Dimension (n) [out]  
  
Wi : Real Array, Dimension (n) [out]  
> WR and WI contain the real and imaginary parts,  
> respectively, of the computed eigenvalues.  Complex  
> conjugate pairs of eigenvalues appear consecutively  
> with the eigenvalue having the positive imaginary part  
> first.  
  
Vl : Real Array, Dimension (ldvl,n) [out]  
> If JOBVL = 'V', the left eigenvectors u(j) are stored one  
> after another in the columns of VL, in the same order  
> as their eigenvalues.  
> If JOBVL = 'N', VL is not referenced.  
> If the j-th eigenvalue is real, then u(j) = VL(:,j),  
> the j-th column of VL.  
> If the j-th and (j+1)-st eigenvalues form a complex  
  
Ldvl : Integer [in]  
> The leading dimension of the array VL.  LDVL >= 1; if  
> JOBVL = 'V', LDVL >= N.  
  
Vr : Real Array, Dimension (ldvr,n) [out]  
> If JOBVR = 'V', the right eigenvectors v(j) are stored one  
> after another in the columns of VR, in the same order  
> as their eigenvalues.  
> If JOBVR = 'N', VR is not referenced.  
> If the j-th eigenvalue is real, then v(j) = VR(:,j),  
> the j-th column of VR.  
> If the j-th and (j+1)-st eigenvalues form a complex  
  
Ldvr : Integer [in]  
> The leading dimension of the array VR.  LDVR >= 1; if  
> JOBVR = 'V', LDVR >= N.  
  
Work : Real Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> performance, LWORK must generally be larger.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
> > 0:  if INFO = i, the QR algorithm failed to compute all the  
> eigenvalues, and no eigenvectors have been computed;  
> elements i+1:N of WR and WI contain eigenvalues which  
> have converged.  
  
