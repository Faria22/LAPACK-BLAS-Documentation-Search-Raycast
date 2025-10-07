```fortran
subroutine zlaqhp (
		character uplo,
		integer n,
		complex*16, dimension(*) ap,
		double precision, dimension(*) s,
		double precision scond,
		double precision amax,
		character equed
)
```

 ZLAQHP equilibrates a Hermitian matrix A using the scaling factors
 in the vector S.

## Parameters
Uplo : Character*1 [in]
> Specifies whether the upper or lower triangular part of the
> Hermitian matrix A is stored.
> = 'U':  Upper triangular
> = 'L':  Lower triangular

N : Integer [in]
> The order of the matrix A.  N >= 0.

Ap : Complex*16 Array, Dimension (n*(n+1)/2) [in,out]
> On entry, the upper or lower triangle of the Hermitian matrix
> A, packed columnwise in a linear array.  The j-th column of A
> is stored in the array AP as follows:
> if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j;
> if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j<=i<=n.
> On exit, the equilibrated matrix:  diag(S) * A * diag(S), in
> the same storage format as A.

S : Double Precision Array, Dimension (n) [in]
> The scale factors for A.

Scond : Double Precision [in]
> Ratio of the smallest S(i) to the largest S(i).

Amax : Double Precision [in]
> Absolute value of largest matrix entry.

Equed : Character*1 [out]
> Specifies whether or not equilibration was done.
> = 'N':  No equilibration.
> = 'Y':  Equilibration was done, i.e., A has been replaced by
> diag(S) * A * diag(S).

