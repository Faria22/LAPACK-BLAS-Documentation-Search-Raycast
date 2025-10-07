# ZLARTV

## Function Signature

```fortran
ZLARTV(N, X, INCX, Y, INCY, C, S, INCC)
```

## Description


 ZLARTV applies a vector of complex plane rotations with real cosines
 to elements of the complex vectors x and y. For i = 1,2,...,n

    ( x(i) ) := (        c(i)   s(i) ) ( x(i) )
    ( y(i) )    ( -conjg(s(i))  c(i) ) ( y(i) )

## Parameters

### N (in)

N is INTEGER The number of plane rotations to be applied.

### X (in,out)

X is COMPLEX*16 array, dimension (1+(N-1)*INCX) The vector x.

### INCX (in)

INCX is INTEGER The increment between elements of X. INCX > 0.

### Y (in,out)

Y is COMPLEX*16 array, dimension (1+(N-1)*INCY) The vector y.

### INCY (in)

INCY is INTEGER The increment between elements of Y. INCY > 0.

### C (in)

C is DOUBLE PRECISION array, dimension (1+(N-1)*INCC) The cosines of the plane rotations.

### S (in)

S is COMPLEX*16 array, dimension (1+(N-1)*INCC) The sines of the plane rotations.

### INCC (in)

INCC is INTEGER The increment between elements of C and S. INCC > 0.

