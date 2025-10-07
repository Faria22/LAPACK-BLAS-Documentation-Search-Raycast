# SLAR2V

## Function Signature

```fortran
SLAR2V(N, X, Y, Z, INCX, C, S, INCC)
```

## Description


 SLAR2V applies a vector of real plane rotations from both sides to
 a sequence of 2-by-2 real symmetric matrices, defined by the elements
 of the vectors x, y and z. For i = 1,2,...,n

    ( x(i)  z(i) ) := (  c(i)  s(i) ) ( x(i)  z(i) ) ( c(i) -s(i) )
    ( z(i)  y(i) )    ( -s(i)  c(i) ) ( z(i)  y(i) ) ( s(i)  c(i) )

## Parameters

### N (in)

N is INTEGER The number of plane rotations to be applied.

### X (in,out)

X is REAL array, dimension (1+(N-1)*INCX) The vector x.

### Y (in,out)

Y is REAL array, dimension (1+(N-1)*INCX) The vector y.

### Z (in,out)

Z is REAL array, dimension (1+(N-1)*INCX) The vector z.

### INCX (in)

INCX is INTEGER The increment between elements of X, Y and Z. INCX > 0.

### C (in)

C is REAL array, dimension (1+(N-1)*INCC) The cosines of the plane rotations.

### S (in)

S is REAL array, dimension (1+(N-1)*INCC) The sines of the plane rotations.

### INCC (in)

INCC is INTEGER The increment between elements of C and S. INCC > 0.

