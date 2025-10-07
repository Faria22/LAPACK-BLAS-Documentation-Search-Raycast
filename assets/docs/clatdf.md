```fortran  
subroutine clatdf (  
ijob,  
n,  
z,  
ldz,  
rhs,  
rdsum,  
rdscal,  
ipiv,  
*                          jpiv  
)  
```  
  
CLATDF computes the contribution to the reciprocal Dif-estimate  
by solving for x in Z * x = b, where b is chosen such that the norm  
of x is as large as possible. It is assumed that LU decomposition  
of Z has been computed by CGETC2. On entry RHS = f holds the  
contribution from earlier solved sub-systems, and on return RHS = x.  
  
The factorization of Z returned by CGETC2 has the form  
Z = P * L * U * Q, where P and Q are permutation matrices. L is lower  
triangular with unit diagonal elements and U is upper triangular.  
  
## Parameters  
Ijob : Integer [in]  
> IJOB = 2: First compute an approximative null-vector e  
> of Z using CGECON, e is normalized and solve for  
> Zx = +-e - f with the sign giving the greater value of  
> 2-norm(x).  About 5 times as expensive as Default.  
> IJOB .ne. 2: Local look ahead strategy where  
> all entries of the r.h.s. b is chosen as either +1 or  
> -1.  Default.  
  
N : Integer [in]  
> The number of columns of the matrix Z.  
  
Z : Complex Array, Dimension (ldz, N) [in]  
> On entry, the LU part of the factorization of the n-by-n  
  
Ldz : Integer [in]  
> The leading dimension of the array Z.  LDA >= max(1, N).  
  
Rhs : Complex Array, Dimension (n). [in,out]  
> On entry, RHS contains contributions from other subsystems.  
> On exit, RHS contains the solution of the subsystem with  
> entries according to the value of IJOB (see above).  
  
Rdsum : Real [in,out]  
> On entry, the sum of squares of computed contributions to  
> the Dif-estimate under computation by CTGSYL, where the  
> scaling factor RDSCAL (see below) has been factored out.  
> On exit, the corresponding sum of squares updated with the  
> contributions from the current sub-system.  
> If TRANS = 'T' RDSUM is not touched.  
> NOTE: RDSUM only makes sense when CTGSY2 is called by CTGSYL.  
  
Rdscal : Real [in,out]  
> On entry, scaling factor used to prevent overflow in RDSUM.  
> On exit, RDSCAL is updated w.r.t. the current contributions  
> in RDSUM.  
> If TRANS = 'T', RDSCAL is not touched.  
> NOTE: RDSCAL only makes sense when CTGSY2 is called by  
> CTGSYL.  
  
Ipiv : Integer Array, Dimension (n). [in]  
> The pivot indices; for 1 <= i <= N, row i of the  
> matrix has been interchanged with row IPIV(i).  
  
Jpiv : Integer Array, Dimension (n). [in]  
> The pivot indices; for 1 <= j <= N, column j of the  
> matrix has been interchanged with column JPIV(j).  
  
