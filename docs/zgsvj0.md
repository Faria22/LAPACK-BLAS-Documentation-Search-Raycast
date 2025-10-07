# ZGSVJ0

ZGSVJ0 pre-processor for the routine zgesvj.

## Function Signature

```fortran
ZGSVJ0(JOBV, M, N, A, LDA, D, SVA, MV, V, LDV, EPS,
*                          SFMIN, TOL, NSWEEP, WORK, LWORK, INFO)
```

## Description


 ZGSVJ0 is called from ZGESVJ as a pre-processor and that is its main
 purpose. It applies Jacobi rotations in the same way as ZGESVJ does, but
 it does not check convergence (stopping criterion). Few tuning
 parameters (marked by [TP]) are available for the implementer.

## Parameters

### JOBV (in)

JOBV is CHARACTER*1 Specifies whether the output from this procedure is used to compute the matrix V: = 'V': the product of the Jacobi rotations is accumulated by postmultiplying the N-by-N array V. (See the description of V.) = 'A': the product of the Jacobi rotations is accumulated by postmultiplying the MV-by-N array V. (See the descriptions of MV and V.) = 'N': the Jacobi rotations are not accumulated.

### M (in)

M is INTEGER The number of rows of the input matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the input matrix A. M >= N >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, M-by-N matrix A, such that A*diag(D) represents the input matrix. On exit, A_onexit * diag(D_onexit) represents the input matrix A*diag(D) post-multiplied by a sequence of Jacobi rotations, where the rotation threshold and the total number of sweeps are given in TOL and NSWEEP, respectively. (See the descriptions of D, TOL and NSWEEP.)

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### D (in,out)

D is COMPLEX*16 array, dimension (N) The array D accumulates the scaling factors from the complex scaled Jacobi rotations. On entry, A*diag(D) represents the input matrix. On exit, A_onexit*diag(D_onexit) represents the input matrix post-multiplied by a sequence of Jacobi rotations, where the rotation threshold and the total number of sweeps are given in TOL and NSWEEP, respectively. (See the descriptions of A, TOL and NSWEEP.)

### SVA (in,out)

SVA is DOUBLE PRECISION array, dimension (N) On entry, SVA contains the Euclidean norms of the columns of the matrix A*diag(D). On exit, SVA contains the Euclidean norms of the columns of the matrix A_onexit*diag(D_onexit).

### MV (in)

MV is INTEGER If JOBV = 'A', then MV rows of V are post-multiplied by a sequence of Jacobi rotations. If JOBV = 'N', then MV is not referenced.

### V (in,out)

V is COMPLEX*16 array, dimension (LDV,N) If JOBV = 'V' then N rows of V are post-multiplied by a sequence of Jacobi rotations. If JOBV = 'A' then MV rows of V are post-multiplied by a sequence of Jacobi rotations. If JOBV = 'N', then V is not referenced.

### LDV (in)

LDV is INTEGER The leading dimension of the array V, LDV >= 1. If JOBV = 'V', LDV >= N. If JOBV = 'A', LDV >= MV.

### EPS (in)

EPS is DOUBLE PRECISION EPS = DLAMCH('Epsilon')

### SFMIN (in)

SFMIN is DOUBLE PRECISION SFMIN = DLAMCH('Safe Minimum')

### TOL (in)

TOL is DOUBLE PRECISION TOL is the threshold for Jacobi rotations. For a pair A(:,p), A(:,q) of pivot columns, the Jacobi rotation is applied only if ABS(COS(angle(A(:,p),A(:,q)))) > TOL.

### NSWEEP (in)

NSWEEP is INTEGER NSWEEP is the number of sweeps of Jacobi rotations to be performed.

### WORK (out)

WORK is COMPLEX*16 array, dimension (LWORK)

### LWORK (in)

LWORK is INTEGER LWORK is the dimension of WORK. LWORK >= M.

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, then the i-th argument had an illegal value

