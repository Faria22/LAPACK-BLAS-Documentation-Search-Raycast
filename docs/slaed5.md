```fortran
subroutine slaed5	(	integer	i,
		real, dimension(2)	d,
		real, dimension(2)	z,
		real, dimension(2)	delta,
		real	rho,
		real	dlam )
```

 This subroutine computes the I-th eigenvalue of a symmetric rank-one
 modification of a 2-by-2 diagonal matrix

            diag( D )  +  RHO * Z * transpose(Z) .

 The diagonal elements in the array D are assumed to satisfy

            D(i) < D(j)  for  i < j .

 We also assume RHO > 0 and that the Euclidean norm of the vector
 Z is one.

## Parameters
I : Integer [in]
> The index of the eigenvalue to be computed.  I = 1 or I = 2.

D : Real Array, Dimension (2) [in]
> The original eigenvalues.  We assume D(1) < D(2).

Z : Real Array, Dimension (2) [in]
> The components of the updating vector.

Delta : Real Array, Dimension (2) [out]
> The vector DELTA contains the information necessary
> to construct the eigenvectors.

Rho : Real [in]
> The scalar in the symmetric updating formula.

Dlam : Real [out]
> The computed lambda_I, the I-th updated eigenvalue.

