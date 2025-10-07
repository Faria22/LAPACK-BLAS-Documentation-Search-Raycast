# SLAQTR

## Function Signature

```fortran
SLAQTR(LTRAN, LREAL, N, T, LDT, B, W, SCALE, X, WORK,
*                          INFO)
```

## Description


 SLAQTR solves the real quasi-triangular system

              op(T)*p = scale*c,               if LREAL = .TRUE.

 or the complex quasi-triangular systems

            op(T + iB)*(p+iq) = scale*(c+id),  if LREAL = .FALSE.

 in real arithmetic, where T is upper quasi-triangular.
 If LREAL = .FALSE., then the first diagonal block of T must be
 1 by 1, B is the specially structured matrix

                B = [ b(1) b(2) ... b(n) ]
                    [       w            ]
                    [           w        ]
                    [              .     ]
                    [                 w  ]

 op(A) = A or A**T, A**T denotes the transpose of
 matrix A.

 On input, X = [ c ].  On output, X = [ p ].
               [ d ]                  [ q ]

 This subroutine is designed for the condition number estimation
 in routine STRSNA.

## Parameters

### LTRAN (in)

LTRAN is LOGICAL On entry, LTRAN specifies the option of conjugate transpose: = .FALSE., op(T+i*B) = T+i*B, = .TRUE., op(T+i*B) = (T+i*B)**T.

### LREAL (in)

LREAL is LOGICAL On entry, LREAL specifies the input matrix structure: = .FALSE., the input is complex = .TRUE., the input is real

### N (in)

N is INTEGER On entry, N specifies the order of T+i*B. N >= 0.

### T (in)

T is REAL array, dimension (LDT,N) On entry, T contains a matrix in Schur canonical form. If LREAL = .FALSE., then the first diagonal block of T must be 1 by 1.

### LDT (in)

LDT is INTEGER The leading dimension of the matrix T. LDT >= max(1,N).

### B (in)

B is REAL array, dimension (N) On entry, B contains the elements to form the matrix B as described above. If LREAL = .TRUE., B is not referenced.

### W (in)

W is REAL On entry, W is the diagonal element of the matrix B. If LREAL = .TRUE., W is not referenced.

### SCALE (out)

SCALE is REAL On exit, SCALE is the scale factor.

### X (in,out)

X is REAL array, dimension (2*N) On entry, X contains the right hand side of the system. On exit, X is overwritten by the solution.

### WORK (out)

WORK is REAL array, dimension (N)

### INFO (out)

INFO is INTEGER On exit, INFO is set to 0: successful exit. 1: the some diagonal 1 by 1 block has been perturbed by a small number SMIN to keep nonsingularity. 2: the some diagonal 2 by 2 block has been perturbed by a small number in SLALN2 to keep nonsingularity. NOTE: In the interests of speed, this routine does not check the inputs for errors.

