```fortran  
subroutine dtrsyl (  
trana,  
tranb,  
isgn,  
m,  
n,  
a,  
lda,  
b,  
ldb,  
c,  
*                          ldc,  
scale,  
info  
)  
```  
  
DTRSYL solves the real Sylvester matrix equation:  
  
op(A)*X + X*op(B) = scale*C or  
op(A)*X - X*op(B) = scale*C,  
  
where op(A) = A or A**T, and  A and B are both upper quasi-  
triangular. A is M-by-M and B is N-by-N; the right hand side C and  
the solution X are M-by-N; and scale is an output scale factor, set  
<= 1 to avoid overflow in X.  
  
A and B must be in Schur canonical form (as returned by DHSEQR), that  
is, block upper triangular with 1-by-1 and 2-by-2 diagonal blocks;  
each 2-by-2 diagonal block has its diagonal elements equal and its  
off-diagonal elements of opposite sign.  
  
## Parameters  
Trana : Character*1 [in]  
> Specifies the option op(A):  
> = 'N': op(A) = A    (No transpose)  
  
Tranb : Character*1 [in]  
> Specifies the option op(B):  
> = 'N': op(B) = B    (No transpose)  
  
Isgn : Integer [in]  
> Specifies the sign in the equation:  
  
M : Integer [in]  
> The order of the matrix A, and the number of rows in the  
> matrices X and C. M >= 0.  
  
N : Integer [in]  
> The order of the matrix B, and the number of columns in the  
> matrices X and C. N >= 0.  
  
A : Double Precision Array, Dimension (lda,m) [in]  
> The upper quasi-triangular matrix A, in Schur canonical form.  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >= max(1,M).  
  
B : Double Precision Array, Dimension (ldb,n) [in]  
> The upper quasi-triangular matrix B, in Schur canonical form.  
  
Ldb : Integer [in]  
> The leading dimension of the array B. LDB >= max(1,N).  
  
C : Double Precision Array, Dimension (ldc,n) [in,out]  
> On entry, the M-by-N right hand side matrix C.  
> On exit, C is overwritten by the solution matrix X.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >= max(1,M)  
  
Scale : Double Precision [out]  
> The scale factor, scale, set <= 1 to avoid overflow in X.  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if INFO = -i, the i-th argument had an illegal value  
> = 1: A and B have common or very close eigenvalues; perturbed  
> values were used to solve the equation (but the matrices  
> A and B are unchanged).  
  
