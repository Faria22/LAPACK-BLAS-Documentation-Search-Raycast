```fortran  
subroutine dtgsen (  
ijob,  
wantq,  
wantz,  
select,  
n,  
a,  
lda,  
b,  
ldb,  
*                          alphar,  
alphai,  
beta,  
q,  
ldq,  
z,  
ldz,  
m,  
pl,  
*                          pr,  
dif,  
work,  
lwork,  
iwork,  
liwork,  
info  
)  
```  
  
DTGSEN reorders the generalized real Schur decomposition of a real  
matrix pair (A, B) (in terms of an orthonormal equivalence trans-  
formation Q**T * (A, B) * Z), so that a selected cluster of eigenvalues  
appears in the leading diagonal blocks of the upper quasi-triangular  
matrix A and the upper triangular B. The leading columns of Q and  
Z form orthonormal bases of the corresponding left and right eigen-  
spaces (deflating subspaces). (A, B) must be in generalized real  
Schur canonical form (as returned by DGGES), i.e. A is block upper  
triangular with 1-by-1 and 2-by-2 diagonal blocks. B is upper  
triangular.  
  
DTGSEN also computes the generalized eigenvalues  
  
w(j) = (ALPHAR(j) + i*ALPHAI(j))/BETA(j)  
  
of the reordered matrix pair (A, B).  
  
Optionally, DTGSEN computes the estimates of reciprocal condition  
numbers for eigenvalues and eigenspaces. These are Difu[(A11,B11),  
(A22,B22)] and Difl[(A11,B11), (A22,B22)], i.e. the separation(s)  
between the matrix pairs (A11, B11) and (A22,B22) that correspond to  
the selected cluster and the eigenvalues outside the cluster, resp.,  
and norms of "projections" onto left and right eigenspaces w.r.t.  
the selected cluster in the (1,1)-block.  
  
## Parameters  
Ijob : Integer [in]  
> Specifies whether condition numbers are required for the  
> cluster of eigenvalues (PL and PR) or the deflating subspaces  
> (Difu and Difl):  
> =0: Only reorder w.r.t. SELECT. No extras.  
> =1: Reciprocal of norms of "projections" onto left and right  
> eigenspaces w.r.t. the selected cluster (PL and PR).  
> =2: Upper bounds on Difu and Difl. F-norm-based estimate  
> (DIF(1:2)).  
> =3: Estimate of Difu and Difl. 1-norm-based estimate  
> (DIF(1:2)).  
> About 5 times as expensive as IJOB = 2.  
> =4: Compute PL, PR and DIF (i.e. 0, 1 and 2 above): Economic  
> version to get it all.  
> =5: Compute PL, PR and DIF (i.e. 0, 1 and 3 above)  
  
Wantq : Logical [in]  
> .TRUE. : update the left transformation matrix Q;  
> .FALSE.: do not update Q.  
  
Wantz : Logical [in]  
> .TRUE. : update the right transformation matrix Z;  
> .FALSE.: do not update Z.  
  
Select : Logical Array, Dimension (n) [in]  
> SELECT specifies the eigenvalues in the selected cluster.  
> To select a real eigenvalue w(j), SELECT(j) must be set to  
> .TRUE.. To select a complex conjugate pair of eigenvalues  
> w(j) and w(j+1), corresponding to a 2-by-2 diagonal block,  
> either SELECT(j) or SELECT(j+1) or both must be set to  
> .TRUE.; a complex conjugate pair of eigenvalues must be  
> either both included in the cluster or both excluded.  
  
N : Integer [in]  
> The order of the matrices A and B. N >= 0.  
  
A : Double Precision Array, Dimension(lda,n) [in,out]  
> On entry, the upper quasi-triangular matrix A, with (A, B) in  
> generalized real Schur canonical form.  
> On exit, A is overwritten by the reordered matrix A.  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >= max(1,N).  
  
B : Double Precision Array, Dimension(ldb,n) [in,out]  
> On entry, the upper triangular matrix B, with (A, B) in  
> generalized real Schur canonical form.  
> On exit, B is overwritten by the reordered matrix B.  
  
Ldb : Integer [in]  
> The leading dimension of the array B. LDB >= max(1,N).  
  
Alphar : Double Precision Array, Dimension (n) [out]  
  
Alphai : Double Precision Array, Dimension (n) [out]  
  
Beta : Double Precision Array, Dimension (n) [out]  
> and BETA(j),j=1,...,N  are the diagonals of the complex Schur  
> form (S,T) that would result if the 2-by-2 diagonal blocks of  
> the real generalized Schur form of (A,B) were further reduced  
> to triangular form using complex unitary transformations.  
> If ALPHAI(j) is zero, then the j-th eigenvalue is real; if  
> positive, then the j-th and (j+1)-st eigenvalues are a  
> complex conjugate pair, with ALPHAI(j+1) negative.  
  
Q : Double Precision Array, Dimension (ldq,n) [in,out]  
> On entry, if WANTQ = .TRUE., Q is an N-by-N matrix.  
> On exit, Q has been postmultiplied by the left orthogonal  
> transformation matrix which reorder (A, B); The leading M  
> columns of Q form orthonormal bases for the specified pair of  
> left eigenspaces (deflating subspaces).  
> If WANTQ = .FALSE., Q is not referenced.  
  
Ldq : Integer [in]  
> The leading dimension of the array Q.  LDQ >= 1;  
> and if WANTQ = .TRUE., LDQ >= N.  
  
Z : Double Precision Array, Dimension (ldz,n) [in,out]  
> On entry, if WANTZ = .TRUE., Z is an N-by-N matrix.  
> On exit, Z has been postmultiplied by the left orthogonal  
> transformation matrix which reorder (A, B); The leading M  
> columns of Z form orthonormal bases for the specified pair of  
> left eigenspaces (deflating subspaces).  
> If WANTZ = .FALSE., Z is not referenced.  
  
Ldz : Integer [in]  
> The leading dimension of the array Z. LDZ >= 1;  
> If WANTZ = .TRUE., LDZ >= N.  
  
M : Integer [out]  
> The dimension of the specified pair of left and right eigen-  
> spaces (deflating subspaces). 0 <= M <= N.  
  
Pl : Double Precision [out]  
  
Pr : Double Precision [out]  
> If IJOB = 1, 4 or 5, PL, PR are lower bounds on the  
> reciprocal of the norm of "projections" onto left and right  
> eigenspaces with respect to the selected cluster.  
> 0 < PL, PR <= 1.  
> If M = 0 or M = N, PL = PR  = 1.  
> If IJOB = 0, 2 or 3, PL and PR are not referenced.  
  
Dif : Double Precision Array, Dimension (2). [out]  
> If IJOB >= 2, DIF(1:2) store the estimates of Difu and Difl.  
> If IJOB = 2 or 4, DIF(1:2) are F-norm-based upper bounds on  
> Difu and Difl. If IJOB = 3 or 5, DIF(1:2) are 1-norm-based  
> estimates of Difu and Difl.  
> If M = 0 or N, DIF(1:2) = F-norm([A, B]).  
> If IJOB = 0 or 1, DIF is not referenced.  
  
Work : Double Precision Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Iwork : Integer Array, Dimension (max(1,liwork)) [out]  
> On exit, if INFO = 0, IWORK(1) returns the optimal LIWORK.  
  
Liwork : Integer [in]  
> The dimension of the array IWORK. LIWORK >= 1.  
> If IJOB = 1, 2 or 4, LIWORK >=  N+6.  
> If LIWORK = -1, then a workspace query is assumed; the  
> routine only calculates the optimal size of the IWORK array,  
> returns this value as the first entry of the IWORK array, and  
> no error message related to LIWORK is issued by XERBLA.  
  
Info : Integer [out]  
> =0: Successful exit.  
> <0: If INFO = -i, the i-th argument had an illegal value.  
> =1: Reordering of (A, B) failed because the transformed  
> matrix pair (A, B) would be too far from generalized  
> Schur form; the problem is very ill-conditioned.  
> (A, B) may have been partially reordered.  
  
