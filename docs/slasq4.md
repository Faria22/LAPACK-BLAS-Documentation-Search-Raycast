```fortran
subroutine slasq4 (
		i0,
		n0,
		z,
		pp,
		n0in,
		dmin,
		dmin1,
		dmin2,
		dn,
		*                          dn1,
		dn2,
		tau,
		ttype,
		g
)
```

 SLASQ4 computes an approximation TAU to the smallest eigenvalue
 using values of d from the previous transform.

## Parameters
I0 : Integer [in]
> First index.

N0 : Integer [in]
> Last index.

Z : Real Array, Dimension ( 4*n0 ) [in]
> Z holds the qd array.

Pp : Integer [in]
> PP=0 for ping, PP=1 for pong.

N0in : Integer [in]
> The value of N0 at start of EIGTEST.

Dmin : Real [in]
> Minimum value of d.

Dmin1 : Real [in]
> Minimum value of d, excluding D( N0 ).

Dmin2 : Real [in]
> Minimum value of d, excluding D( N0 ) and D( N0-1 ).

Dn : Real [in]
> d(N)

Dn1 : Real [in]
> d(N-1)

Dn2 : Real [in]
> d(N-2)

Tau : Real [out]
> This is the shift.

Ttype : Integer [out]
> Shift type.

G : Real [in,out]
> G is passed as an argument in order to save its value between
> calls to SLASQ4.

