```fortran
subroutine zlarscl2	(	integer	m,
		integer	n,
		double precision, dimension(*)	d,
		complex*16, dimension(ldx, *)	x,
		integer	ldx )
```

 ZLARSCL2 performs a reciprocal diagonal scaling on a matrix:
   x <-- inv(D) * x
 where the DOUBLE PRECISION diagonal matrix D is stored as a vector.

 Eventually to be replaced by BLAS_zge_diag_scale in the new BLAS
 standard.

## Parameters
M : Integer [in]
> The number of rows of D and X. M >= 0.

N : Integer [in]
> The number of columns of X. N >= 0.

D : Double Precision Array, Length M [in]
> Diagonal matrix D, stored as a vector of length M.

X : Complex*16 Array, Dimension (ldx,n) [in,out]
> On entry, the matrix X to be scaled by D.
> On exit, the scaled matrix.

Ldx : Integer [in]
> The leading dimension of the matrix X. LDX >= M.

