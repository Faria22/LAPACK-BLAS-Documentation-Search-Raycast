```fortran  
subroutine dlagtm (  
trans,  
n,  
nrhs,  
alpha,  
dl,  
d,  
du,  
x,  
ldx,  
beta,  
*                          b,  
ldb  
)  
```  
  
DLAGTM performs a matrix-matrix product of the form  
  
B := alpha * A * X + beta * B  
  
where A is a tridiagonal matrix of order N, B and X are N by NRHS  
matrices, and alpha and beta are real scalars, each of which may be  
0., 1., or -1.  
  
## Parameters  
Trans : Character*1 [in]  
> Specifies the operation applied to A.  
> = 'C':  Conjugate transpose = Transpose  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrices X and B.  
  
Alpha : Double Precision [in]  
> The scalar alpha.  ALPHA must be 0., 1., or -1.; otherwise,  
> it is assumed to be 0.  
  
Dl : Double Precision Array, Dimension (n-1) [in]  
> The (n-1) sub-diagonal elements of T.  
  
D : Double Precision Array, Dimension (n) [in]  
> The diagonal elements of T.  
  
Du : Double Precision Array, Dimension (n-1) [in]  
> The (n-1) super-diagonal elements of T.  
  
X : Double Precision Array, Dimension (ldx,nrhs) [in]  
> The N by NRHS matrix X.  
  
Ldx : Integer [in]  
> The leading dimension of the array X.  LDX >= max(N,1).  
  
Beta : Double Precision [in]  
> The scalar beta.  BETA must be 0., 1., or -1.; otherwise,  
> it is assumed to be 1.  
  
B : Double Precision Array, Dimension (ldb,nrhs) [in,out]  
> On entry, the N by NRHS matrix B.  
> On exit, B is overwritten by the matrix expression  
  
Ldb : Integer [in]  
> The leading dimension of the array B.  LDB >= max(N,1).  
  
