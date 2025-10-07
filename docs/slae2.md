```fortran
subroutine slae2	(	real	a,
		real	b,
		real	c,
		real	rt1,
		real	rt2 )
```

 SLAE2  computes the eigenvalues of a 2-by-2 symmetric matrix
    [  A   B  ]
    [  B   C  ].
 On return, RT1 is the eigenvalue of larger absolute value, and RT2
 is the eigenvalue of smaller absolute value.

## Parameters
A : Real [in]
> The (1,1) element of the 2-by-2 matrix.

B : Real [in]
> The (1,2) and (2,1) elements of the 2-by-2 matrix.

C : Real [in]
> The (2,2) element of the 2-by-2 matrix.

Rt1 : Real [out]
> The eigenvalue of larger absolute value.

Rt2 : Real [out]
> The eigenvalue of smaller absolute value.

