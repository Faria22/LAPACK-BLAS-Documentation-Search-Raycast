```fortran  
subroutine zdrot (  
integer n,  
complex*16, dimension(*) zx,  
integer incx,  
complex*16, dimension(*) zy,  
integer incy,  
double precision c,  
double precision s  
)  
```  
  
Applies a plane rotation, where the cos and sin (c and s) are real  
and the vectors cx and cy are complex.  
jack dongarra, linpack, 3/11/78.  
  
## Parameters  
N : Integer [in]  
> On entry, N specifies the order of the vectors cx and cy.  
> N must be at least zero.  
  
Zx : Complex*16 Array, Dimension At Least [in,out]  
> Before entry, the incremented array ZX must contain the n  
> element vector cx. On exit, ZX is overwritten by the updated  
> vector cx.  
  
Incx : Integer [in]  
> On entry, INCX specifies the increment for the elements of  
> ZX. INCX must not be zero.  
  
Zy : Complex*16 Array, Dimension At Least [in,out]  
> Before entry, the incremented array ZY must contain the n  
> element vector cy. On exit, ZY is overwritten by the updated  
> vector cy.  
  
Incy : Integer [in]  
> On entry, INCY specifies the increment for the elements of  
> ZY. INCY must not be zero.  
  
C : Double Precision [in]  
> On entry, C specifies the cosine, cos.  
  
S : Double Precision [in]  
> On entry, S specifies the sine, sin.  
  
