# SROTM

## Function Signature

```fortran
SROTM(N,SX,INCX,SY,INCY,SPARAM)
```

## Description


    APPLY THE MODIFIED GIVENS TRANSFORMATION, H, TO THE 2 BY N MATRIX

    (SX**T) , WHERE **T INDICATES TRANSPOSE. THE ELEMENTS OF SX ARE IN
    (SX**T)

    SX(LX+I*INCX), I = 0 TO N-1, WHERE LX = 1 IF INCX .GE. 0, ELSE
    LX = (-INCX)*N, AND SIMILARLY FOR SY USING USING LY AND INCY.
    WITH SPARAM(1)=SFLAG, H HAS ONE OF THE FOLLOWING FORMS..

    SFLAG=-1.E0     SFLAG=0.E0        SFLAG=1.E0     SFLAG=-2.E0

      (SH11  SH12)    (1.E0  SH12)    (SH11  1.E0)    (1.E0  0.E0)
    H=(          )    (          )    (          )    (          )
      (SH21  SH22),   (SH21  1.E0),   (-1.E0 SH22),   (0.E0  1.E0).
    SEE  SROTMG FOR A DESCRIPTION OF DATA STORAGE IN SPARAM.

    IF SFLAG IS NOT ONE OF THE LISTED ABOVE, THE BEHAVIOR IS UNDEFINED.
    NANS IN SFLAG MAY NOT PROPAGATE TO THE OUTPUT.


## Parameters

### N (in)

N is INTEGER number of elements in input vector(s)

### SX (in,out)

SX is REAL array, dimension ( 1 + ( N - 1 )*abs( INCX ) )

### INCX (in)

INCX is INTEGER storage spacing between elements of SX

### SY (in,out)

SY is REAL array, dimension ( 1 + ( N - 1 )*abs( INCY ) )

### INCY (in)

INCY is INTEGER storage spacing between elements of SY

### SPARAM (in)

SPARAM is REAL array, dimension (5) SPARAM(1)=SFLAG SPARAM(2)=SH11 SPARAM(3)=SH21 SPARAM(4)=SH12 SPARAM(5)=SH22

