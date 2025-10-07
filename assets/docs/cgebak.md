```fortran
subroutine cgebak (
		job,
		side,
		n,
		ilo,
		ihi,
		scale,
		m,
		v,
		ldv,
		*                          info
)
```

 CGEBAK forms the right or left eigenvectors of a complex general
 matrix by backward transformation on the computed eigenvectors of the
 balanced matrix output by CGEBAL.

## Parameters
Job : Character*1 [in]
> Specifies the type of backward transformation required:
> = 'N': do nothing, return immediately;
> = 'P': do backward transformation for permutation only;
> = 'S': do backward transformation for scaling only;
> = 'B': do backward transformations for both permutation and
> scaling.
> JOB must be the same as the argument JOB supplied to CGEBAL.

Side : Character*1 [in]
> = 'R':  V contains right eigenvectors;
> = 'L':  V contains left eigenvectors.

N : Integer [in]
> The number of rows of the matrix V.  N >= 0.

Ilo : Integer [in]

Ihi : Integer [in]
> The integers ILO and IHI determined by CGEBAL.
> 1 <= ILO <= IHI <= N, if N > 0; ILO=1 and IHI=0, if N=0.

Scale : Real Array, Dimension (n) [in]
> Details of the permutation and scaling factors, as returned
> by CGEBAL.

M : Integer [in]
> The number of columns of the matrix V.  M >= 0.

V : Complex Array, Dimension (ldv,m) [in,out]
> On entry, the matrix of right or left eigenvectors to be
> transformed, as returned by CHSEIN or CTREVC.
> On exit, V is overwritten by the transformed eigenvectors.

Ldv : Integer [in]
> The leading dimension of the array V. LDV >= max(1,N).

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value.

