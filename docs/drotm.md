```fortran
subroutine drotm (
		integer n,
		double precision, dimension(*) dx,
		integer incx,
		double precision, dimension(*) dy,
		integer incy,
		double precision, dimension(5) dparam
)
```

    APPLY THE MODIFIED GIVENS TRANSFORMATION, H, TO THE 2 BY N MATRIX

    (DX**T) , WHERE **T INDICATES TRANSPOSE. THE ELEMENTS OF DX ARE IN
    (DY**T)

    DX(LX+I*INCX), I = 0 TO N-1, WHERE LX = 1 IF INCX .GE. 0, ELSE
    LX = (-INCX)*N, AND SIMILARLY FOR SY USING LY AND INCY.
    WITH DPARAM(1)=DFLAG, H HAS ONE OF THE FOLLOWING FORMS..

    DFLAG=-1.D0     DFLAG=0.D0        DFLAG=1.D0     DFLAG=-2.D0

      (DH11  DH12)    (1.D0  DH12)    (DH11  1.D0)    (1.D0  0.D0)
    H=(          )    (          )    (          )    (          )
      (DH21  DH22),   (DH21  1.D0),   (-1.D0 DH22),   (0.D0  1.D0).
    SEE DROTMG FOR A DESCRIPTION OF DATA STORAGE IN DPARAM.

    IF DFLAG IS NOT ONE OF THE LISTED ABOVE, THE BEHAVIOR IS UNDEFINED.
    NANS IN DFLAG MAY NOT PROPAGATE TO THE OUTPUT.


## Parameters
N : Integer [in]
> number of elements in input vector(s)

Dx : Double Precision Array, Dimension ( 1 + ( N - 1 )*abs( Incx ) ) [in,out]

Incx : Integer [in]
> storage spacing between elements of DX

Dy : Double Precision Array, Dimension ( 1 + ( N - 1 )*abs( Incy ) ) [in,out]

Incy : Integer [in]
> storage spacing between elements of DY

Dparam : Double Precision Array, Dimension (5) [in]
> DPARAM(1)=DFLAG
> DPARAM(2)=DH11
> DPARAM(3)=DH21
> DPARAM(4)=DH12
> DPARAM(5)=DH22

