# DLARGV

## Function Signature

```fortran
DLARGV(N, X, INCX, Y, INCY, C, INCC)
```

## Description


 DLARGV generates a vector of real plane rotations, determined by
 elements of the real vectors x and y. For i = 1,2,...,n

    (  c(i)  s(i) ) ( x(i) ) = ( a(i) )
    ( -s(i)  c(i) ) ( y(i) ) = (   0  )

## Parameters

### N (in)

N is INTEGER The number of plane rotations to be generated.

### X (in,out)

X is DOUBLE PRECISION array, dimension (1+(N-1)*INCX) On entry, the vector x. On exit, x(i) is overwritten by a(i), for i = 1,...,n.

### INCX (in)

INCX is INTEGER The increment between elements of X. INCX > 0.

### Y (in,out)

Y is DOUBLE PRECISION array, dimension (1+(N-1)*INCY) On entry, the vector y. On exit, the sines of the plane rotations.

### INCY (in)

INCY is INTEGER The increment between elements of Y. INCY > 0.

### C (out)

C is DOUBLE PRECISION array, dimension (1+(N-1)*INCC) The cosines of the plane rotations.

### INCC (in)

INCC is INTEGER The increment between elements of C. INCC > 0.

