```fortran  
subroutine dtgsna (  
job,  
howmny,  
select,  
n,  
a,  
lda,  
b,  
ldb,  
vl,  
*                          ldvl,  
vr,  
ldvr,  
s,  
dif,  
mm,  
m,  
work,  
lwork,  
*                          iwork,  
info  
)  
```  
  
DTGSNA estimates reciprocal condition numbers for specified  
eigenvalues and/or eigenvectors of a matrix pair (A, B) in  
generalized real Schur canonical form (or of any matrix pair  
(Q*A*Z**T, Q*B*Z**T) with orthogonal matrices Q and Z, where  
Z**T denotes the transpose of Z.  
  
(A, B) must be in generalized real Schur form (as returned by DGGES),  
i.e. A is block upper triangular with 1-by-1 and 2-by-2 diagonal  
blocks. B is upper triangular.  
  
  
## Parameters  
Job : Character*1 [in]  
> Specifies whether condition numbers are required for  
> eigenvalues (S) or eigenvectors (DIF):  
> = 'E': for eigenvalues only (S);  
> = 'V': for eigenvectors only (DIF);  
> = 'B': for both eigenvalues and eigenvectors (S and DIF).  
  
Howmny : Character*1 [in]  
> = 'A': compute condition numbers for all eigenpairs;  
> = 'S': compute condition numbers for selected eigenpairs  
> specified by the array SELECT.  
  
Select : Logical Array, Dimension (n) [in]  
> If HOWMNY = 'S', SELECT specifies the eigenpairs for which  
> condition numbers are required. To select condition numbers  
> for the eigenpair corresponding to a real eigenvalue w(j),  
> SELECT(j) must be set to .TRUE.. To select condition numbers  
> corresponding to a complex conjugate pair of eigenvalues w(j)  
> and w(j+1), either SELECT(j) or SELECT(j+1) or both, must be  
> set to .TRUE..  
> If HOWMNY = 'A', SELECT is not referenced.  
  
N : Integer [in]  
> The order of the square matrix pair (A, B). N >= 0.  
  
A : Double Precision Array, Dimension (lda,n) [in]  
> The upper quasi-triangular matrix A in the pair (A,B).  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >= max(1,N).  
  
B : Double Precision Array, Dimension (ldb,n) [in]  
> The upper triangular matrix B in the pair (A,B).  
  
Ldb : Integer [in]  
> The leading dimension of the array B. LDB >= max(1,N).  
  
Vl : Double Precision Array, Dimension (ldvl,m) [in]  
> If JOB = 'E' or 'B', VL must contain left eigenvectors of  
> (A, B), corresponding to the eigenpairs specified by HOWMNY  
> and SELECT. The eigenvectors must be stored in consecutive  
> columns of VL, as returned by DTGEVC.  
> If JOB = 'V', VL is not referenced.  
  
Ldvl : Integer [in]  
> The leading dimension of the array VL. LDVL >= 1.  
> If JOB = 'E' or 'B', LDVL >= N.  
  
Vr : Double Precision Array, Dimension (ldvr,m) [in]  
> If JOB = 'E' or 'B', VR must contain right eigenvectors of  
> (A, B), corresponding to the eigenpairs specified by HOWMNY  
> and SELECT. The eigenvectors must be stored in consecutive  
> columns ov VR, as returned by DTGEVC.  
> If JOB = 'V', VR is not referenced.  
  
Ldvr : Integer [in]  
> The leading dimension of the array VR. LDVR >= 1.  
> If JOB = 'E' or 'B', LDVR >= N.  
  
S : Double Precision Array, Dimension (mm) [out]  
> If JOB = 'E' or 'B', the reciprocal condition numbers of the  
> selected eigenvalues, stored in consecutive elements of the  
> array. For a complex conjugate pair of eigenvalues two  
> consecutive elements of S are set to the same value. Thus  
> S(j), DIF(j), and the j-th columns of VL and VR all  
> correspond to the same eigenpair (but not in general the  
> j-th eigenpair, unless all eigenpairs are selected).  
> If JOB = 'V', S is not referenced.  
  
Dif : Double Precision Array, Dimension (mm) [out]  
> If JOB = 'V' or 'B', the estimated reciprocal condition  
> numbers of the selected eigenvectors, stored in consecutive  
> elements of the array. For a complex eigenvector two  
> consecutive elements of DIF are set to the same value. If  
> the eigenvalues cannot be reordered to compute DIF(j), DIF(j)  
> is set to 0; this can only occur when the true value would be  
> very small anyway.  
> If JOB = 'E', DIF is not referenced.  
  
Mm : Integer [in]  
> The number of elements in the arrays S and DIF. MM >= M.  
  
M : Integer [out]  
> The number of elements of the arrays S and DIF used to store  
> the specified condition numbers; for each selected real  
> eigenvalue one element is used, and for each selected complex  
> conjugate pair of eigenvalues, two elements are used.  
> If HOWMNY = 'A', M is set to N.  
  
Work : Double Precision Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK. LWORK >= max(1,N).  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Iwork : Integer Array, Dimension (n + 6) [out]  
> If JOB = 'E', IWORK is not referenced.  
  
Info : Integer [out]  
> =0: Successful exit  
> <0: If INFO = -i, the i-th argument had an illegal value  
  
