```fortran
subroutine dlaed3	(	k,
		n,
		n1,
		d,
		q,
		ldq,
		rho,
		dlambda,
		q2,
		indx,
		*                          ctot,
		w,
		s,
		info )
```

 DLAED3 finds the roots of the secular equation, as defined by the
 values in D, W, and RHO, between 1 and K.  It makes the
 appropriate calls to DLAED4 and then updates the eigenvectors by
 multiplying the matrix of eigenvectors of the pair of eigensystems
 being combined by the matrix of eigenvectors of the K-by-K system
 which is solved here.


## Parameters
K : Integer [in]
> The number of terms in the rational function to be solved by
> DLAED4.  K >= 0.

N : Integer [in]
> The number of rows and columns in the Q matrix.
> N >= K (deflation may result in N>K).

N1 : Integer [in]
> The location of the last eigenvalue in the leading submatrix.
> min(1,N) <= N1 <= N/2.

D : Double Precision Array, Dimension (n) [out]
> D(I) contains the updated eigenvalues for
> 1 <= I <= K.

Q : Double Precision Array, Dimension (ldq,n) [out]
> Initially the first K columns are used as workspace.
> On output the columns 1 to K contain
> the updated eigenvectors.

Ldq : Integer [in]
> The leading dimension of the array Q.  LDQ >= max(1,N).

Rho : Double Precision [in]
> The value of the parameter in the rank one update equation.
> RHO >= 0 required.

Dlambda : Double Precision Array, Dimension (k) [in]
> The first K elements of this array contain the old roots
> of the deflated updating problem.  These are the poles
> of the secular equation.

Q2 : Double Precision Array, Dimension (ldq2*n) [in]
> The first K columns of this matrix contain the non-deflated
> eigenvectors for the split problem.

Indx : Integer Array, Dimension (n) [in]
> The permutation used to arrange the columns of the deflated
> Q matrix into three groups (see DLAED2).
> The rows of the eigenvectors found by DLAED4 must be likewise
> permuted before the matrix multiply can take place.

Ctot : Integer Array, Dimension (4) [in]
> A count of the total number of the various types of columns
> in Q, as described in INDX.  The fourth column type is any
> column which has been deflated.

W : Double Precision Array, Dimension (k) [in,out]
> The first K elements of this array contain the components
> of the deflation-adjusted updating vector. Destroyed on
> output.

S : Double Precision Array, Dimension (n1 + 1)*k [out]
> Will contain the eigenvectors of the repaired matrix which
> will be multiplied by the previously accumulated eigenvectors
> to update the system.

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.
> > 0:  if INFO = 1, an eigenvalue did not converge

