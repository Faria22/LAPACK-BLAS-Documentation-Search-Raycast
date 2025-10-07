# CLAR2V

## Function Signature

```fortran
CLAR2V(N, X, Y, Z, INCX, C, S, INCC)
```

## Description


 CLAR2V applies a vector of complex plane rotations with real cosines
 from both sides to a sequence of 2-by-2 complex Hermitian matrices,
 defined by the elements of the vectors x, y and z. For i = 1,2,...,n

    (       x(i)  z(i) ) :=
    ( conjg(z(i)) y(i) )

      (  c(i) conjg(s(i)) ) (       x(i)  z(i) ) ( c(i) -conjg(s(i)) )
      ( -s(i)       c(i)  ) ( conjg(z(i)) y(i) ) ( s(i)        c(i)  )

## Parameters

### N (in)

N is INTEGER The number of plane rotations to be applied.

### X (in,out)

X is COMPLEX array, dimension (1+(N-1)*INCX) The vector x; the elements of x are assumed to be real.

### Y (in,out)

Y is COMPLEX array, dimension (1+(N-1)*INCX) The vector y; the elements of y are assumed to be real.

### Z (in,out)

Z is COMPLEX array, dimension (1+(N-1)*INCX) The vector z.

### INCX (in)

INCX is INTEGER The increment between elements of X, Y and Z. INCX > 0.

### C (in)

C is REAL array, dimension (1+(N-1)*INCC) The cosines of the plane rotations.

### S (in)

S is COMPLEX array, dimension (1+(N-1)*INCC) The sines of the plane rotations.

### INCC (in)

INCC is INTEGER The increment between elements of C and S. INCC > 0.

