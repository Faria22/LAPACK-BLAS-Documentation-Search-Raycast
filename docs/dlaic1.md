# DLAIC1

## Function Signature

```fortran
DLAIC1(JOB, J, X, SEST, W, GAMMA, SESTPR, S, C)
```

## Description


 DLAIC1 applies one step of incremental condition estimation in
 its simplest version:

 Let x, twonorm(x) = 1, be an approximate singular vector of an j-by-j
 lower triangular matrix L, such that
          twonorm(L*x) = sest
 Then DLAIC1 computes sestpr, s, c such that
 the vector
                 [ s*x ]
          xhat = [  c  ]
 is an approximate singular vector of
                 [ L       0  ]
          Lhat = [ w**T gamma ]
 in the sense that
          twonorm(Lhat*xhat) = sestpr.

 Depending on JOB, an estimate for the largest or smallest singular
 value is computed.

 Note that [s c]**T and sestpr**2 is an eigenpair of the system

     diag(sest*sest, 0) + [alpha  gamma] * [ alpha ]
                                           [ gamma ]

 where  alpha =  x**T*w.

## Parameters

### JOB (in)

JOB is INTEGER = 1: an estimate for the largest singular value is computed. = 2: an estimate for the smallest singular value is computed.

### J (in)

J is INTEGER Length of X and W

### X (in)

X is DOUBLE PRECISION array, dimension (J) The j-vector x.

### SEST (in)

SEST is DOUBLE PRECISION Estimated singular value of j by j matrix L

### W (in)

W is DOUBLE PRECISION array, dimension (J) The j-vector w.

### GAMMA (in)

GAMMA is DOUBLE PRECISION The diagonal element gamma.

### SESTPR (out)

SESTPR is DOUBLE PRECISION Estimated singular value of (j+1) by (j+1) matrix Lhat.

### S (out)

S is DOUBLE PRECISION Sine needed in forming xhat.

### C (out)

C is DOUBLE PRECISION Cosine needed in forming xhat.

