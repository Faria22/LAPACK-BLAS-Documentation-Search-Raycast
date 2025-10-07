# SLARTV

## Function Signature

```fortran
SLARTV(N, X, INCX, Y, INCY, C, S, INCC)
```

## Description


 SLARTV applies a vector of real plane rotations to elements of the
 real vectors x and y. For i = 1,2,...,n

    ( x(i) ) := (  c(i)  s(i) ) ( x(i) )
    ( y(i) )    ( -s(i)  c(i) ) ( y(i) )

## Parameters

### N (in)

N is INTEGER The number of plane rotations to be applied.

### X (in,out)

X is REAL array, dimension (1+(N-1)*INCX) The vector x.

### INCX (in)

INCX is INTEGER The increment between elements of X. INCX > 0.

### Y (in,out)

Y is REAL array, dimension (1+(N-1)*INCY) The vector y.

### INCY (in)

INCY is INTEGER The increment between elements of Y. INCY > 0.

### C (in)

C is REAL array, dimension (1+(N-1)*INCC) The cosines of the plane rotations.

### S (in)

S is REAL array, dimension (1+(N-1)*INCC) The sines of the plane rotations.

### INCC (in)

INCC is INTEGER The increment between elements of C and S. INCC > 0.

