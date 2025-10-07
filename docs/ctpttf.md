```fortran
subroutine ctpttf	(	character	transr,
		character	uplo,
		integer	n,
		complex, dimension(0: *)	ap,
		complex, dimension(0: *)	arf,
		integer	info )
```

 CTPTTF copies a triangular matrix A from standard packed format (TP)
 to rectangular full packed format (TF).

## Parameters
Transr : Character*1 [in]
> = 'N':  ARF in Normal format is wanted;
> = 'C':  ARF in Conjugate-transpose format is wanted.

Uplo : Character*1 [in]
> = 'U':  A is upper triangular;
> = 'L':  A is lower triangular.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Ap : Complex Array, Dimension ( N*(n+1)/2 ), [in]
> On entry, the upper or lower triangular matrix A, packed
> columnwise in a linear array. The j-th column of A is stored
> in the array AP as follows:
> if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j;
> if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j<=i<=n.

Arf : Complex Array, Dimension ( N*(n+1)/2 ), [out]
> On exit, the upper or lower triangular matrix A stored in
> RFP format. For a further discussion see Notes below.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

