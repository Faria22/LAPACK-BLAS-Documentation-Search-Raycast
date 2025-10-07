```fortran  
subroutine slasq2 (  
integer n,  
real, dimension(*) z,  
integer info  
)  
```  
  
SLASQ2 computes all the eigenvalues of the symmetric positive  
definite tridiagonal matrix associated with the qd array Z to high  
relative accuracy are computed to high relative accuracy, in the  
absence of denormalization, underflow and overflow.  
  
To see the relation of Z to the tridiagonal matrix, let L be a  
unit lower bidiagonal matrix with subdiagonals Z(2,4,6,,..) and  
let U be an upper bidiagonal matrix with 1's above and diagonal  
Z(1,3,5,,..). The tridiagonal is L*U or, if you prefer, the  
symmetric tridiagonal to which it is similar.  
  
Note : SLASQ2 defines a logical variable, IEEE, which is true  
on machines which follow ieee-754 floating-point standard in their  
handling of infinities and NaNs, and false otherwise. This variable  
is passed to SLASQ3.  
  
## Parameters  
N : Integer [in]  
> The number of rows and columns in the matrix. N >= 0.  
  
Z : Real Array, Dimension ( 4*n ) [in,out]  
> On entry Z holds the qd array. On exit, entries 1 to N hold  
> shifts that failed.  
  
Info : Integer [out]  
> = 0: successful exit  
> < 0: if the i-th argument is a scalar and had an illegal  
> value, then INFO = -i, if the i-th argument is an  
> array and the j-entry had an illegal value, then  
> > 0: the algorithm failed  
> = 1, a split was marked by a positive value in E  
> iterations (in inner while loop).  On exit Z holds  
> a qd array with the same eigenvalues as the given Z.  
> = 3, termination criterion of outer while loop not met  
> (program created more than N unreduced blocks)  
  
