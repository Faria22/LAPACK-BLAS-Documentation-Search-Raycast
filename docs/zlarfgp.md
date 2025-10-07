# ZLARFGP

## Function Signature

```fortran
ZLARFGP(N, ALPHA, X, INCX, TAU)
```

## Description


 ZLARFGP generates a complex elementary reflector H of order n, such
 that

       H**H * ( alpha ) = ( beta ),   H**H * H = I.
              (   x   )   (   0  )

 where alpha and beta are scalars, beta is real and non-negative, and
 x is an (n-1)-element complex vector.  H is represented in the form

       H = I - tau * ( 1 ) * ( 1 v**H ) ,
                     ( v )

 where tau is a complex scalar and v is a complex (n-1)-element
 vector. Note that H is not hermitian.

 If the elements of x are all zero and alpha is real, then tau = 0
 and H is taken to be the unit matrix.

## Parameters

### N (in)

N is INTEGER The order of the elementary reflector.

### ALPHA (in,out)

ALPHA is COMPLEX*16 On entry, the value alpha. On exit, it is overwritten with the value beta.

### X (in,out)

X is COMPLEX*16 array, dimension (1+(N-2)*abs(INCX)) On entry, the vector x. On exit, it is overwritten with the vector v.

### INCX (in)

INCX is INTEGER The increment between elements of X. INCX > 0.

### TAU (out)

TAU is COMPLEX*16 The value tau.

