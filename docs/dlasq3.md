```fortran
subroutine dlasq3	(	i0,
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
		tau )
```

 DLASQ3 checks for deflation, computes a shift (TAU) and calls dqds.
 In case of failure it changes shifts, and tries again until output
 is positive.

## Parameters
I0 : Integer [in]
> First index.

N0 : Integer [in,out]
> Last index.

Z : Double Precision Array, Dimension ( 4*n0 ) [in,out]
> Z holds the qd array.

Pp : Integer [in,out]
> PP=0 for ping, PP=1 for pong.
> PP=2 indicates that flipping was applied to the Z array
> and that the initial tests for deflation should not be
> performed.

Dmin : Double Precision [out]
> Minimum value of d.

Sigma : Double Precision [out]
> Sum of shifts used in current segment.

Desig : Double Precision [in,out]
> Lower order part of SIGMA

Qmax : Double Precision [in]
> Maximum value of q.

Nfail : Integer [in,out]
> Increment NFAIL by 1 each time the shift was too big.

Iter : Integer [in,out]
> Increment ITER by 1 for each iteration.

Ndiv : Integer [in,out]
> Increment NDIV by 1 for each division.

Ieee : Logical [in]
> Flag for IEEE or non IEEE arithmetic (passed to DLASQ5).

Ttype : Integer [in,out]
> Shift type.

Dmin1 : Double Precision [in,out]

Dmin2 : Double Precision [in,out]

Dn : Double Precision [in,out]

Dn1 : Double Precision [in,out]

Dn2 : Double Precision [in,out]

G : Double Precision [in,out]

Tau : Double Precision [in,out]
> These are passed as arguments in order to save their values
> between calls to DLASQ3.

