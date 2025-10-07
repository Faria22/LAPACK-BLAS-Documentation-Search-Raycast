```fortran
subroutine slasq3 (
		i0,
		n0,
		z,
		pp,
		dmin,
		sigma,
		desig,
		qmax,
		nfail,
		*                          iter,
		ndiv,
		ieee,
		ttype,
		dmin1,
		dmin2,
		dn,
		dn1,
		*                          dn2,
		g,
		tau
)
```

 SLASQ3 checks for deflation, computes a shift (TAU) and calls dqds.
 In case of failure it changes shifts, and tries again until output
 is positive.

## Parameters
I0 : Integer [in]
> First index.

N0 : Integer [in,out]
> Last index.

Z : Real Array, Dimension ( 4*n0 ) [in,out]
> Z holds the qd array.

Pp : Integer [in,out]
> PP=0 for ping, PP=1 for pong.
> PP=2 indicates that flipping was applied to the Z array
> and that the initial tests for deflation should not be
> performed.

Dmin : Real [out]
> Minimum value of d.

Sigma : Real [out]
> Sum of shifts used in current segment.

Desig : Real [in,out]
> Lower order part of SIGMA

Qmax : Real [in]
> Maximum value of q.

Nfail : Integer [in,out]
> Increment NFAIL by 1 each time the shift was too big.

Iter : Integer [in,out]
> Increment ITER by 1 for each iteration.

Ndiv : Integer [in,out]
> Increment NDIV by 1 for each division.

Ieee : Logical [in]
> Flag for IEEE or non IEEE arithmetic (passed to SLASQ5).

Ttype : Integer [in,out]
> Shift type.

Dmin1 : Real [in,out]

Dmin2 : Real [in,out]

Dn : Real [in,out]

Dn1 : Real [in,out]

Dn2 : Real [in,out]

G : Real [in,out]

Tau : Real [in,out]
> These are passed as arguments in order to save their values
> between calls to SLASQ3.

