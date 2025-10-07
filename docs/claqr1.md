# CLAQR1

## Function Signature

```fortran
CLAQR1(N, H, LDH, S1, S2, V)
```

## Description


      Given a 2-by-2 or 3-by-3 matrix H, CLAQR1 sets v to a
      scalar multiple of the first column of the product

      (*)  K = (H - s1*I)*(H - s2*I)

      scaling to avoid overflows and most underflows.

      This is useful for starting double implicit shift bulges
      in the QR algorithm.

## Parameters

### N (in)

N is INTEGER Order of the matrix H. N must be either 2 or 3.

### H (in)

H is COMPLEX array, dimension (LDH,N) The 2-by-2 or 3-by-3 matrix H in (*).

### LDH (in)

LDH is INTEGER The leading dimension of H as declared in the calling procedure. LDH >= N

### S1 (in)

S1 is COMPLEX

### S2 (in)

S2 is COMPLEX S1 and S2 are the shifts defining K in (*) above.

### V (out)

V is COMPLEX array, dimension (N) A scalar multiple of the first column of the matrix K in (*).

