# SLARZT

## Function Signature

```fortran
SLARZT(DIRECT, STOREV, N, K, V, LDV, TAU, T, LDT)
```

## Description


 SLARZT forms the triangular factor T of a real block reflector
 H of order > n, which is defined as a product of k elementary
 reflectors.

 If DIRECT = 'F', H = H(1) H(2) . . . H(k) and T is upper triangular;

 If DIRECT = 'B', H = H(k) . . . H(2) H(1) and T is lower triangular.

 If STOREV = 'C', the vector which defines the elementary reflector
 H(i) is stored in the i-th column of the array V, and

    H  =  I - V * T * V**T

 If STOREV = 'R', the vector which defines the elementary reflector
 H(i) is stored in the i-th row of the array V, and

    H  =  I - V**T * T * V

 Currently, only STOREV = 'R' and DIRECT = 'B' are supported.

## Parameters

### DIRECT (in)

DIRECT is CHARACTER*1 Specifies the order in which the elementary reflectors are multiplied to form the block reflector: = 'F': H = H(1) H(2) . . . H(k) (Forward, not supported yet) = 'B': H = H(k) . . . H(2) H(1) (Backward)

### STOREV (in)

STOREV is CHARACTER*1 Specifies how the vectors which define the elementary reflectors are stored (see also Further Details): = 'C': columnwise (not supported yet) = 'R': rowwise

### N (in)

N is INTEGER The order of the block reflector H. N >= 0.

### K (in)

K is INTEGER The order of the triangular factor T (= the number of elementary reflectors). K >= 1.

### V (in,out)

V is REAL array, dimension (LDV,K) if STOREV = 'C' (LDV,N) if STOREV = 'R' The matrix V. See further details.

### LDV (in)

LDV is INTEGER The leading dimension of the array V. If STOREV = 'C', LDV >= max(1,N); if STOREV = 'R', LDV >= K.

### TAU (in)

TAU is REAL array, dimension (K) TAU(i) must contain the scalar factor of the elementary reflector H(i).

### T (out)

T is REAL array, dimension (LDT,K) The k by k triangular factor T of the block reflector. If DIRECT = 'F', T is upper triangular; if DIRECT = 'B', T is lower triangular. The rest of the array is not used.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= K.

