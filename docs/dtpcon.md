```fortran
subroutine dtpcon	(	norm,
		uplo,
		diag,
		n,
		ap,
		rcond,
		work,
		iwork,
		*                          info )
```

 DTPCON estimates the reciprocal of the condition number of a packed
 triangular matrix A, in either the 1-norm or the infinity-norm.

 The norm of A is computed and an estimate is obtained for
 norm(inv(A)), then the reciprocal of the condition number is
 computed as
    RCOND = 1 / ( norm(A) * norm(inv(A)) ).

## Parameters
Norm : Character*1 [in]
> Specifies whether the 1-norm condition number or the
> infinity-norm condition number is required:
> = '1' or 'O':  1-norm;
> = 'I':         Infinity-norm.

Uplo : Character*1 [in]
> = 'U':  A is upper triangular;
> = 'L':  A is lower triangular.

Diag : Character*1 [in]
> = 'N':  A is non-unit triangular;
> = 'U':  A is unit triangular.

N : Integer [in]
> The order of the matrix A.  N >= 0.

Ap : Double Precision Array, Dimension (n*(n+1)/2) [in]
> The upper or lower triangular matrix A, packed columnwise in
> a linear array.  The j-th column of A is stored in the array
> AP as follows:
> if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1<=i<=j;
> if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j<=i<=n.
> If DIAG = 'U', the diagonal elements of A are not referenced
> and are assumed to be 1.

Rcond : Double Precision [out]
> The reciprocal of the condition number of the matrix A,
> computed as RCOND = 1/(norm(A) * norm(inv(A))).

Work : Double Precision Array, Dimension (3*n) [out]

Iwork : Integer Array, Dimension (n) [out]

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

