# DLASY2

## Function Signature

```fortran
DLASY2(LTRANL, LTRANR, ISGN, N1, N2, TL, LDTL, TR,
*                          LDTR, B, LDB, SCALE, X, LDX, XNORM, INFO)
```

## Description


 DLASY2 solves for the N1 by N2 matrix X, 1 <= N1,N2 <= 2, in

        op(TL)*X + ISGN*X*op(TR) = SCALE*B,

 where TL is N1 by N1, TR is N2 by N2, B is N1 by N2, and ISGN = 1 or
 -1.  op(T) = T or T**T, where T**T denotes the transpose of T.

## Parameters

### LTRANL (in)

LTRANL is LOGICAL On entry, LTRANL specifies the op(TL): = .FALSE., op(TL) = TL, = .TRUE., op(TL) = TL**T.

### LTRANR (in)

LTRANR is LOGICAL On entry, LTRANR specifies the op(TR): = .FALSE., op(TR) = TR, = .TRUE., op(TR) = TR**T.

### ISGN (in)

ISGN is INTEGER On entry, ISGN specifies the sign of the equation as described before. ISGN may only be 1 or -1.

### N1 (in)

N1 is INTEGER On entry, N1 specifies the order of matrix TL. N1 may only be 0, 1 or 2.

### N2 (in)

N2 is INTEGER On entry, N2 specifies the order of matrix TR. N2 may only be 0, 1 or 2.

### TL (in)

TL is DOUBLE PRECISION array, dimension (LDTL,2) On entry, TL contains an N1 by N1 matrix.

### LDTL (in)

LDTL is INTEGER The leading dimension of the matrix TL. LDTL >= max(1,N1).

### TR (in)

TR is DOUBLE PRECISION array, dimension (LDTR,2) On entry, TR contains an N2 by N2 matrix.

### LDTR (in)

LDTR is INTEGER The leading dimension of the matrix TR. LDTR >= max(1,N2).

### B (in)

B is DOUBLE PRECISION array, dimension (LDB,2) On entry, the N1 by N2 matrix B contains the right-hand side of the equation.

### LDB (in)

LDB is INTEGER The leading dimension of the matrix B. LDB >= max(1,N1).

### SCALE (out)

SCALE is DOUBLE PRECISION On exit, SCALE contains the scale factor. SCALE is chosen less than or equal to 1 to prevent the solution overflowing.

### X (out)

X is DOUBLE PRECISION array, dimension (LDX,2) On exit, X contains the N1 by N2 solution.

### LDX (in)

LDX is INTEGER The leading dimension of the matrix X. LDX >= max(1,N1).

### XNORM (out)

XNORM is DOUBLE PRECISION On exit, XNORM is the infinity-norm of the solution.

### INFO (out)

INFO is INTEGER On exit, INFO is set to 0: successful exit. 1: TL and TR have too close eigenvalues, so TL or TR is perturbed to get a nonsingular equation. NOTE: In the interests of speed, this routine does not check the inputs for errors.

