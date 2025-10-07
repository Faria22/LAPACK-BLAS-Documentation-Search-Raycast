```fortran
subroutine slasq6	(	i0,
		n0,
		z,
		pp,
		dmin,
		dmin1,
		dmin2,
		dn,
		*                          dnm1,
		dnm2 )
```

 SLASQ6 computes one dqd (shift equal to zero) transform in
 ping-pong form, with protection against underflow and overflow.

## Parameters
I0 : Integer [in]
> First index.

N0 : Integer [in]
> Last index.

Z : Real Array, Dimension ( 4*n ) [in]
> Z holds the qd array. EMIN is stored in Z(4*N0) to avoid
> an extra argument.

Pp : Integer [in]
> PP=0 for ping, PP=1 for pong.

Dmin : Real [out]
> Minimum value of d.

Dmin1 : Real [out]
> Minimum value of d, excluding D( N0 ).

Dmin2 : Real [out]
> Minimum value of d, excluding D( N0 ) and D( N0-1 ).

Dn : Real [out]
> d(N0), the last value of d.

Dnm1 : Real [out]
> d(N0-1).

Dnm2 : Real [out]
> d(N0-2).

