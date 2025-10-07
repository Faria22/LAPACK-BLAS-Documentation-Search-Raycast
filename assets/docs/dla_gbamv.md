```fortran  
subroutine dla_gbamv (  
trans,  
m,  
n,  
kl,  
ku,  
alpha,  
ab,  
ldab,  
x,  
*                             incx,  
beta,  
y,  
incy  
)  
```  
  
DLA_GBAMV  performs one of the matrix-vector operations  
  
y := alpha*abs(A)*abs(x) + beta*abs(y),  
or   y := alpha*abs(A)**T*abs(x) + beta*abs(y),  
  
where alpha and beta are scalars, x and y are vectors and A is an  
m by n matrix.  
  
This function is primarily used in calculating error bounds.  
To protect against underflow during evaluation, components in  
the resulting vector are perturbed away from zero by (N+1)  
times the underflow threshold.  To prevent unnecessarily large  
errors for block-structure embedded in general matrices,  
"symbolically" zero components are not perturbed.  A zero  
entry is considered "symbolic" if all multiplications involved  
in computing that entry have at least one zero multiplicand.  
  
## Parameters  
Trans : Integer [in]  
> On entry, TRANS specifies the operation to be performed as  
> follows:  
> Unchanged on exit.  
  
M : Integer [in]  
> On entry, M specifies the number of rows of the matrix A.  
> M must be at least zero.  
> Unchanged on exit.  
  
N : Integer [in]  
> On entry, N specifies the number of columns of the matrix A.  
> N must be at least zero.  
> Unchanged on exit.  
  
Kl : Integer [in]  
> The number of subdiagonals within the band of A.  KL >= 0.  
  
Ku : Integer [in]  
> The number of superdiagonals within the band of A.  KU >= 0.  
  
Alpha : Double Precision [in]  
> On entry, ALPHA specifies the scalar alpha.  
> Unchanged on exit.  
  
Ab : Double Precision Array, Dimension ( Ldab, N ) [in]  
> Before entry, the leading m by n part of the array AB must  
> contain the matrix of coefficients.  
> Unchanged on exit.  
  
Ldab : Integer [in]  
> On entry, LDA specifies the first dimension of AB as declared  
> in the calling (sub) program. LDAB must be at least  
> max( 1, m ).  
> Unchanged on exit.  
  
X : Double Precision Array, Dimension [in]  
> and at least  
> Before entry, the incremented array X must contain the  
> vector x.  
> Unchanged on exit.  
  
Incx : Integer [in]  
> On entry, INCX specifies the increment for the elements of  
> X. INCX must not be zero.  
> Unchanged on exit.  
  
Beta : Double Precision [in]  
> On entry, BETA specifies the scalar beta. When BETA is  
> supplied as zero then Y need not be set on input.  
> Unchanged on exit.  
  
Y : Double Precision Array, Dimension [in,out]  
> and at least  
> Before entry with BETA non-zero, the incremented array Y  
> must contain the vector y. On exit, Y is overwritten by the  
> updated vector y.  
> If either m or n is zero, then Y not referenced and the function  
> performs a quick return.  
  
Incy : Integer [in]  
> On entry, INCY specifies the increment for the elements of  
> Y. INCY must not be zero.  
> Unchanged on exit.  
> Level 2 Blas routine.  
  
