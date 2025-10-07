```fortran
subroutine sggbak (
		job,
		side,
		n,
		ilo,
		ihi,
		lscale,
		rscale,
		m,
		v,
		*                          ldv,
		info
)
```

 SGGBAK forms the right or left eigenvectors of a real generalized
 eigenvalue problem A*x = lambda*B*x, by backward transformation on
 the computed eigenvectors of the balanced pair of matrices output by
 SGGBAL.

## Parameters
Job : Character*1 [in]
> Specifies the type of backward transformation required:
> = 'N':  do nothing, return immediately;
> = 'P':  do backward transformation for permutation only;
> = 'S':  do backward transformation for scaling only;
> = 'B':  do backward transformations for both permutation and
> scaling.
> JOB must be the same as the argument JOB supplied to SGGBAL.

Side : Character*1 [in]
> = 'R':  V contains right eigenvectors;
> = 'L':  V contains left eigenvectors.

N : Integer [in]
> The number of rows of the matrix V.  N >= 0.

Ilo : Integer [in]

Ihi : Integer [in]
> The integers ILO and IHI determined by SGGBAL.
> 1 <= ILO <= IHI <= N, if N > 0; ILO=1 and IHI=0, if N=0.

Lscale : Real Array, Dimension (n) [in]
> Details of the permutations and/or scaling factors applied
> to the left side of A and B, as returned by SGGBAL.

Rscale : Real Array, Dimension (n) [in]
> Details of the permutations and/or scaling factors applied
> to the right side of A and B, as returned by SGGBAL.

M : Integer [in]
> The number of columns of the matrix V.  M >= 0.

V : Real Array, Dimension (ldv,m) [in,out]
> On entry, the matrix of right or left eigenvectors to be
> transformed, as returned by STGEVC.
> On exit, V is overwritten by the transformed eigenvectors.

Ldv : Integer [in]
> The leading dimension of the matrix V. LDV >= max(1,N).

Info : Integer [out]
> = 0:  successful exit.
> < 0:  if INFO = -i, the i-th argument had an illegal value.

