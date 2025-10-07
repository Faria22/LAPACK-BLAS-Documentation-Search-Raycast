# ZLACRT

## Function Signature

```fortran
ZLACRT(N, CX, INCX, CY, INCY, C, S)
```

## Description


 ZLACRT performs the operation

    (  c  s )( x )  ==> ( x )
    ( -s  c )( y )      ( y )

 where c and s are complex and the vectors x and y are complex.

## Parameters

### N (in)

N is INTEGER The number of elements in the vectors CX and CY.

### CX (in,out)

CX is COMPLEX*16 array, dimension (N) On input, the vector x. On output, CX is overwritten with c*x + s*y.

### INCX (in)

INCX is INTEGER The increment between successive values of CX. INCX <> 0.

### CY (in,out)

CY is COMPLEX*16 array, dimension (N) On input, the vector y. On output, CY is overwritten with -s*x + c*y.

### INCY (in)

INCY is INTEGER The increment between successive values of CY. INCY <> 0.

### C (in)

C is COMPLEX*16

### S (in)

S is COMPLEX*16 C and S define the matrix [ C S ]. [ -S C ]

