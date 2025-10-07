# DROTM

## Function Signature

```fortran
DROTM(N,DX,INCX,DY,INCY,DPARAM)
```

## Description


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

### N (in)

N is INTEGER number of elements in input vector(s)

### DX (in,out)

DX is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of DX

### DY (in,out)

DY is DOUBLE PRECISION array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of DY

### DPARAM (in)

DPARAM is DOUBLE PRECISION array, dimension (5) DPARAM(1)=DFLAG DPARAM(2)=DH11 DPARAM(3)=DH21 DPARAM(4)=DH12 DPARAM(5)=DH22

