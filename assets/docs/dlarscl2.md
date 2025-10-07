```fortran
subroutine dlarscl2 (
		integer m,
		integer n,
		double precision, dimension(*) d,
		double precision, dimension(ldx, *) x,
		integer ldx
)
```

 DLARSCL2 performs a reciprocal diagonal scaling on a matrix:
   x <-- inv(D) * x
 where the diagonal matrix D is stored as a vector.

 Eventually to be replaced by BLAS_dge_diag_scale in the new BLAS
 standard.

## Parameters
M : Integer [in]
> The number of rows of D and X. M >= 0.

N : Integer [in]
> The number of columns of X. N >= 0.

D : Double Precision Array, Dimension (m) [in]
> Diagonal matrix D, stored as a vector of length M.

X : Double Precision Array, Dimension (ldx,n) [in,out]
> On entry, the matrix X to be scaled by D.
> On exit, the scaled matrix.

Ldx : Integer [in]
> The leading dimension of the matrix X. LDX >= M.

