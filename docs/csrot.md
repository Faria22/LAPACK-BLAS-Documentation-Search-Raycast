# CSROT

## Function Signature

```fortran
CSROT(N, CX, INCX, CY, INCY, C, S)
```

## Description


 CSROT applies a plane rotation, where the cos and sin (c and s) are real
 and the vectors cx and cy are complex.
 jack dongarra, linpack, 3/11/78.

## Parameters

### N (in)

N is INTEGER On entry, N specifies the order of the vectors cx and cy. N must be at least zero.

### CX (in,out)

CX is COMPLEX array, dimension at least ( 1 + ( N - 1 )*abs( INCX ) ). Before entry, the incremented array CX must contain the n element vector cx. On exit, CX is overwritten by the updated vector cx.

### INCX (in)

INCX is INTEGER On entry, INCX specifies the increment for the elements of CX. INCX must not be zero.

### CY (in,out)

CY is COMPLEX array, dimension at least ( 1 + ( N - 1 )*abs( INCY ) ). Before entry, the incremented array CY must contain the n element vector cy. On exit, CY is overwritten by the updated vector cy.

### INCY (in)

INCY is INTEGER On entry, INCY specifies the increment for the elements of CY. INCY must not be zero.

### C (in)

C is REAL On entry, C specifies the cosine, cos.

### S (in)

S is REAL On entry, S specifies the sine, sin.

