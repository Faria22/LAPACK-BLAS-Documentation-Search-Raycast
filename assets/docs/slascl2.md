```fortran  
subroutine slascl2 (  
integer m,  
integer n,  
real, dimension(*) d,  
real, dimension(ldx, *) x,  
integer ldx  
)  
```  
  
SLASCL2 performs a diagonal scaling on a matrix:  
x <-- D * x  
where the diagonal matrix D is stored as a vector.  
  
Eventually to be replaced by BLAS_sge_diag_scale in the new BLAS  
standard.  
  
## Parameters  
M : Integer [in]  
> The number of rows of D and X. M >= 0.  
  
N : Integer [in]  
> The number of columns of X. N >= 0.  
  
D : Real Array, Length M [in]  
> Diagonal matrix D, stored as a vector of length M.  
  
X : Real Array, Dimension (ldx,n) [in,out]  
> On entry, the matrix X to be scaled by D.  
> On exit, the scaled matrix.  
  
Ldx : Integer [in]  
> The leading dimension of the matrix X. LDX >= M.  
  
