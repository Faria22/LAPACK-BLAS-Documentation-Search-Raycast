```fortran
subroutine slaed6 (
		integer kniter,
		logical orgati,
		real rho,
		real, dimension(3) d,
		real, dimension(3) z,
		real finit,
		real tau,
		integer info
)
```

 SLAED6 computes the positive or negative root (closest to the origin)
 of
                  z(1)        z(2)        z(3)
 f(x) =   rho + --------- + ---------- + ---------
                 d(1)-x      d(2)-x      d(3)-x

 It is assumed that

       if ORGATI = .true. the root is between d(2) and d(3);
       otherwise it is between d(1) and d(2)

 This routine will be called by SLAED4 when necessary. In most cases,
 the root sought is the smallest in magnitude, though it might not be
 in some extremely rare situations.

## Parameters
Kniter : Integer [in]
> Refer to SLAED4 for its significance.

Orgati : Logical [in]
> If ORGATI is true, the needed root is between d(2) and
> d(3); otherwise it is between d(1) and d(2).  See
> SLAED4 for further details.

Rho : Real [in]
> Refer to the equation f(x) above.

D : Real Array, Dimension (3) [in]
> D satisfies d(1) < d(2) < d(3).

Z : Real Array, Dimension (3) [in]
> Each of the elements in z must be positive.

Finit : Real [in]
> The value of f at 0. It is more accurate than the one
> evaluated inside this routine (if someone wants to do
> so).

Tau : Real [out]
> The root of the equation f(x).

Info : Integer [out]
> = 0: successful exit
> > 0: if INFO = 1, failure to converge

