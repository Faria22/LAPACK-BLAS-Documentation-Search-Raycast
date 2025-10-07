# ZDROT

## Function Signature

```fortran
ZDROT(N, ZX, INCX, ZY, INCY, C, S)
```

## Description


 Applies a plane rotation, where the cos and sin (c and s) are real
 and the vectors cx and cy are complex.
 jack dongarra, linpack, 3/11/78.

## Parameters

### N (in)

N is INTEGER On entry, N specifies the order of the vectors cx and cy. N must be at least zero.

### ZX (in,out)

ZX is COMPLEX*16 array, dimension at least ( 1 + ( N - 1 )*abs( INCX ) ). Before entry, the incremented array ZX must contain the n element vector cx. On exit, ZX is overwritten by the updated vector cx.

### INCX (in)

INCX is INTEGER On entry, INCX specifies the increment for the elements of ZX. INCX must not be zero.

### ZY (in,out)

ZY is COMPLEX*16 array, dimension at least ( 1 + ( N - 1 )*abs( INCY ) ). Before entry, the incremented array ZY must contain the n element vector cy. On exit, ZY is overwritten by the updated vector cy.

### INCY (in)

INCY is INTEGER On entry, INCY specifies the increment for the elements of ZY. INCY must not be zero.

### C (in)

C is DOUBLE PRECISION On entry, C specifies the cosine, cos.

### S (in)

S is DOUBLE PRECISION On entry, S specifies the sine, sin.

