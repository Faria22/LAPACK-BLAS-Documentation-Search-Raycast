# DLAQR1

## Function Signature

```fortran
DLAQR1(N, H, LDH, SR1, SI1, SR2, SI2, V)
```

## Description


      Given a 2-by-2 or 3-by-3 matrix H, DLAQR1 sets v to a
      scalar multiple of the first column of the product

      (*)  K = (H - (sr1 + i*si1)*I)*(H - (sr2 + i*si2)*I)

      scaling to avoid overflows and most underflows. It
      is assumed that either

              1) sr1 = sr2 and si1 = -si2
          or
              2) si1 = si2 = 0.

      This is useful for starting double implicit shift bulges
      in the QR algorithm.

## Parameters

### N (in)

N is INTEGER Order of the matrix H. N must be either 2 or 3.

### H (in)

H is DOUBLE PRECISION array, dimension (LDH,N) The 2-by-2 or 3-by-3 matrix H in (*).

### LDH (in)

LDH is INTEGER The leading dimension of H as declared in the calling procedure. LDH >= N

### SR1 (in)

SR1 is DOUBLE PRECISION

### SI1 (in)

SI1 is DOUBLE PRECISION

### SR2 (in)

SR2 is DOUBLE PRECISION

### SI2 (in)

SI2 is DOUBLE PRECISION The shifts in (*).

### V (out)

V is DOUBLE PRECISION array, dimension (N) A scalar multiple of the first column of the matrix K in (*).

