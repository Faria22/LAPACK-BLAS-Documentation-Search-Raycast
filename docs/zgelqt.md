```fortran
subroutine zgelqt	(	integer	m,
		integer	n,
		integer	mb,
		complex*16, dimension(lda, *)	a,
		integer	lda,
		complex*16, dimension(ldt, *)	t,
		integer	ldt,
		complex*16, dimension(*)	work,
		integer	info )
```

 ZGELQT computes a blocked LQ factorization of a complex M-by-N matrix A
 using the compact WY representation of Q.

## Parameters
M : Integer [in]
> The number of rows of the matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the matrix A.  N >= 0.

Mb : Integer [in]
> The block size to be used in the blocked LQ.  MIN(M,N) >= MB >= 1.

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry, the M-by-N matrix A.
> On exit, the elements on and below the diagonal of the array
> contain the M-by-MIN(M,N) lower trapezoidal matrix L (L is
> lower triangular if M <= N); the elements above the diagonal
> are the rows of V.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

T : Complex*16 Array, Dimension (ldt,min(m,n)) [out]
> The upper triangular block reflectors stored in compact form
> as a sequence of upper triangular blocks.  See below
> for further details.

Ldt : Integer [in]
> The leading dimension of the array T.  LDT >= MB.

Work : Complex*16 Array, Dimension (mb*m). [out]
> Note: A smaller workspace of MB*(M-MB) may also be sufficient, but
> that is yet to be proven. MB*M is a conservative estimate and the
> recommended value to use.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

