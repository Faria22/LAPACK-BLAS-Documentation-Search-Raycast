```fortran
subroutine dstev	(	character	jobz,
		integer	n,
		double precision, dimension(*)	d,
		double precision, dimension(*)	e,
		double precision, dimension(ldz, *)	z,
		integer	ldz,
		double precision, dimension(*)	work,
		integer	info )
```

 DSTEV computes all eigenvalues and, optionally, eigenvectors of a
 real symmetric tridiagonal matrix A.

## Parameters
Jobz : Character*1 [in]
> = 'N':  Compute eigenvalues only;
> = 'V':  Compute eigenvalues and eigenvectors.

N : Integer [in]
> The order of the matrix.  N >= 0.

D : Double Precision Array, Dimension (n) [in,out]
> On entry, the n diagonal elements of the tridiagonal matrix
> A.
> On exit, if INFO = 0, the eigenvalues in ascending order.

E : Double Precision Array, Dimension (n-1) [in,out]
> On entry, the (n-1) subdiagonal elements of the tridiagonal
> matrix A, stored in elements 1 to N-1 of E.
> On exit, the contents of E are destroyed.

Z : Double Precision Array, Dimension (ldz, N) [out]
> If JOBZ = 'V', then if INFO = 0, Z contains the orthonormal
> eigenvectors of the matrix A, with the i-th column of Z
> holding the eigenvector associated with D(i).
> If JOBZ = 'N', then Z is not referenced.

Ldz : Integer [in]
> The leading dimension of the array Z.  LDZ >= 1, and if
> JOBZ = 'V', LDZ >= max(1,N).

Work : Double Precision Array, Dimension (max(1,2*n-2)) [out]
> If JOBZ = 'N', WORK is not referenced.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value
> > 0:  if INFO = i, the algorithm failed to converge; i
> off-diagonal elements of E did not converge to zero.

