```fortran
subroutine zlaqge	(	m,
		n,
		a,
		lda,
		r,
		c,
		rowcnd,
		colcnd,
		amax,
		*                          equed )
```

 ZLAQGE equilibrates a general M by N matrix A using the row and
 column scaling factors in the vectors R and C.

## Parameters
M : Integer [in]
> The number of rows of the matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the matrix A.  N >= 0.

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry, the M by N matrix A.
> On exit, the equilibrated matrix.  See EQUED for the form of
> the equilibrated matrix.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(M,1).

R : Double Precision Array, Dimension (m) [in]
> The row scale factors for A.

C : Double Precision Array, Dimension (n) [in]
> The column scale factors for A.

Rowcnd : Double Precision [in]
> Ratio of the smallest R(i) to the largest R(i).

Colcnd : Double Precision [in]
> Ratio of the smallest C(i) to the largest C(i).

Amax : Double Precision [in]
> Absolute value of largest matrix entry.

Equed : Character*1 [out]
> Specifies the form of equilibration that was done.
> = 'N':  No equilibration
> = 'R':  Row equilibration, i.e., A has been premultiplied by
> diag(R).
> = 'C':  Column equilibration, i.e., A has been postmultiplied
> by diag(C).
> = 'B':  Both row and column equilibration, i.e., A has been
> replaced by diag(R) * A * diag(C).

