```fortran  
subroutine dbdsdc (  
uplo,  
compq,  
n,  
d,  
e,  
u,  
ldu,  
vt,  
ldvt,  
q,  
iq,  
*                          work,  
iwork,  
info  
)  
```  
  
DBDSDC computes the singular value decomposition (SVD) of a real  
N-by-N (upper or lower) bidiagonal matrix B:  B = U * S * VT,  
using a divide and conquer method, where S is a diagonal matrix  
with non-negative diagonal elements (the singular values of B), and  
U and VT are orthogonal matrices of left and right singular vectors,  
respectively. DBDSDC can be used to compute all singular values,  
and optionally, singular vectors or singular vectors in compact form.  
  
The code currently calls DLASDQ if singular values only are desired.  
However, it can be slightly modified to compute singular values  
using the divide and conquer method.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  B is upper bidiagonal.  
> = 'L':  B is lower bidiagonal.  
  
Compq : Character*1 [in]  
> Specifies whether singular vectors are to be computed  
> as follows:  
> = 'N':  Compute singular values only;  
> = 'P':  Compute singular values and compute singular  
> vectors in compact form;  
> = 'I':  Compute singular values and singular vectors.  
  
N : Integer [in]  
> The order of the matrix B.  N >= 0.  
  
D : Double Precision Array, Dimension (n) [in,out]  
> On entry, the n diagonal elements of the bidiagonal matrix B.  
> On exit, if INFO=0, the singular values of B.  
  
E : Double Precision Array, Dimension (n-1) [in,out]  
> On entry, the elements of E contain the offdiagonal  
> elements of the bidiagonal matrix whose SVD is desired.  
> On exit, E has been destroyed.  
  
U : Double Precision Array, Dimension (ldu,n) [out]  
> If  COMPQ = 'I', then:  
> On exit, if INFO = 0, U contains the left singular vectors  
> of the bidiagonal matrix.  
> For other values of COMPQ, U is not referenced.  
  
Ldu : Integer [in]  
> The leading dimension of the array U.  LDU >= 1.  
> If singular vectors are desired, then LDU >= max( 1, N ).  
  
Vt : Double Precision Array, Dimension (ldvt,n) [out]  
> If  COMPQ = 'I', then:  
> vectors of the bidiagonal matrix.  
> For other values of COMPQ, VT is not referenced.  
  
Ldvt : Integer [in]  
> The leading dimension of the array VT.  LDVT >= 1.  
> If singular vectors are desired, then LDVT >= max( 1, N ).  
  
Q : Double Precision Array, Dimension (ldq) [out]  
> If  COMPQ = 'P', then:  
> On exit, if INFO = 0, Q and IQ contain the left  
> and right singular vectors in a compact form,  
> In particular, Q contains all the DOUBLE PRECISION data in  
> words of memory, where SMLSIZ is returned by ILAENV and  
> is equal to the maximum size of the subproblems at the  
> bottom of the computation tree (usually about 25).  
> For other values of COMPQ, Q is not referenced.  
  
Iq : Integer Array, Dimension (ldiq) [out]  
> If  COMPQ = 'P', then:  
> On exit, if INFO = 0, Q and IQ contain the left  
> and right singular vectors in a compact form,  
> In particular, IQ contains all INTEGER data in  
> words of memory, where SMLSIZ is returned by ILAENV and  
> is equal to the maximum size of the subproblems at the  
> bottom of the computation tree (usually about 25).  
> For other values of COMPQ, IQ is not referenced.  
  
Work : Double Precision Array, Dimension (max(1,lwork)) [out]  
  
Iwork : Integer Array, Dimension (8*n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit.  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
> > 0:  The algorithm failed to compute a singular value.  
> The update process of divide and conquer failed.  
  
