# ZGSVJ1

## Function Signature

```fortran
ZGSVJ1(JOBV, M, N, N1, A, LDA, D, SVA, MV, V, LDV,
*                          EPS, SFMIN, TOL, NSWEEP, WORK, LWORK, INFO)
```

## Description


 ZGSVJ1 is called from ZGESVJ as a pre-processor and that is its main
 purpose. It applies Jacobi rotations in the same way as ZGESVJ does, but
 it targets only particular pivots and it does not check convergence
 (stopping criterion). Few tuning parameters (marked by [TP]) are
 available for the implementer.

 Further Details
 ~~~~~~~~~~~~~~~
 ZGSVJ1 applies few sweeps of Jacobi rotations in the column space of
 the input M-by-N matrix A. The pivot pairs are taken from the (1,2)
 off-diagonal block in the corresponding N-by-N Gram matrix A^T * A. The
 block-entries (tiles) of the (1,2) off-diagonal block are marked by the
 [x]'s in the following scheme:

    | *  *  * [x] [x] [x]|
    | *  *  * [x] [x] [x]|    Row-cycling in the nblr-by-nblc [x] blocks.
    | *  *  * [x] [x] [x]|    Row-cyclic pivoting inside each [x] block.
    |[x] [x] [x] *  *  * |
    |[x] [x] [x] *  *  * |
    |[x] [x] [x] *  *  * |

 In terms of the columns of A, the first N1 columns are rotated 'against'
 the remaining N-N1 columns, trying to increase the angle between the
 corresponding subspaces. The off-diagonal block is N1-by(N-N1) and it is
 tiled using quadratic tiles of side KBL. Here, KBL is a tuning parameter.
 The number of sweeps is given in NSWEEP and the orthogonality threshold
 is given in TOL.

## Parameters

### JOBV (in)

JOBV is CHARACTER*1 Specifies whether the output from this procedure is used to compute the matrix V: = 'V': the product of the Jacobi rotations is accumulated by postmultiplying the N-by-N array V. (See the description of V.) = 'A': the product of the Jacobi rotations is accumulated by postmultiplying the MV-by-N array V. (See the descriptions of MV and V.) = 'N': the Jacobi rotations are not accumulated.

### M (in)

M is INTEGER The number of rows of the input matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the input matrix A. M >= N >= 0.

### N1 (in)

N1 is INTEGER N1 specifies the 2 x 2 block partition, the first N1 columns are rotated 'against' the remaining N-N1 columns of A.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, M-by-N matrix A, such that A*diag(D) represents the input matrix. On exit, A_onexit * D_onexit represents the input matrix A*diag(D) post-multiplied by a sequence of Jacobi rotations, where the rotation threshold and the total number of sweeps are given in TOL and NSWEEP, respectively. (See the descriptions of N1, D, TOL and NSWEEP.)

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### D (in,out)

D is COMPLEX*16 array, dimension (N) The array D accumulates the scaling factors from the fast scaled Jacobi rotations. On entry, A*diag(D) represents the input matrix. On exit, A_onexit*diag(D_onexit) represents the input matrix post-multiplied by a sequence of Jacobi rotations, where the rotation threshold and the total number of sweeps are given in TOL and NSWEEP, respectively. (See the descriptions of N1, A, TOL and NSWEEP.)

### SVA (in,out)

SVA is DOUBLE PRECISION array, dimension (N) On entry, SVA contains the Euclidean norms of the columns of the matrix A*diag(D). On exit, SVA contains the Euclidean norms of the columns of the matrix onexit*diag(D_onexit).

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

