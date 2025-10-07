# CTGSEN

## Function Signature

```fortran
CTGSEN(IJOB, WANTQ, WANTZ, SELECT, N, A, LDA, B, LDB,
*                          ALPHA, BETA, Q, LDQ, Z, LDZ, M, PL, PR, DIF,
*                          WORK, LWORK, IWORK, LIWORK, INFO)
```

## Description


 CTGSEN reorders the generalized Schur decomposition of a complex
 matrix pair (A, B) (in terms of an unitary equivalence trans-
 formation Q**H * (A, B) * Z), so that a selected cluster of eigenvalues
 appears in the leading diagonal blocks of the pair (A,B). The leading
 columns of Q and Z form unitary bases of the corresponding left and
 right eigenspaces (deflating subspaces). (A, B) must be in
 generalized Schur canonical form, that is, A and B are both upper
 triangular.

 CTGSEN also computes the generalized eigenvalues

          w(j)= ALPHA(j) / BETA(j)

 of the reordered matrix pair (A, B).

 Optionally, the routine computes estimates of reciprocal condition
 numbers for eigenvalues and eigenspaces. These are Difu[(A11,B11),
 (A22,B22)] and Difl[(A11,B11), (A22,B22)], i.e. the separation(s)
 between the matrix pairs (A11, B11) and (A22,B22) that correspond to
 the selected cluster and the eigenvalues outside the cluster, resp.,
 and norms of "projections" onto left and right eigenspaces w.r.t.
 the selected cluster in the (1,1)-block.


## Parameters

### IJOB (in)

IJOB is INTEGER Specifies whether condition numbers are required for the cluster of eigenvalues (PL and PR) or the deflating subspaces (Difu and Difl): =0: Only reorder w.r.t. SELECT. No extras. =1: Reciprocal of norms of "projections" onto left and right eigenspaces w.r.t. the selected cluster (PL and PR). =2: Upper bounds on Difu and Difl. F-norm-based estimate (DIF(1:2)). =3: Estimate of Difu and Difl. 1-norm-based estimate (DIF(1:2)). About 5 times as expensive as IJOB = 2. =4: Compute PL, PR and DIF (i.e. 0, 1 and 2 above): Economic version to get it all. =5: Compute PL, PR and DIF (i.e. 0, 1 and 3 above)

### WANTQ (in)

WANTQ is LOGICAL .TRUE. : update the left transformation matrix Q; .FALSE.: do not update Q.

### WANTZ (in)

WANTZ is LOGICAL .TRUE. : update the right transformation matrix Z; .FALSE.: do not update Z.

### SELECT (in)

SELECT is LOGICAL array, dimension (N) SELECT specifies the eigenvalues in the selected cluster. To select an eigenvalue w(j), SELECT(j) must be set to .TRUE..

### N (in)

N is INTEGER The order of the matrices A and B. N >= 0.

### A (in,out)

A is COMPLEX array, dimension(LDA,N) On entry, the upper triangular matrix A, in generalized Schur canonical form. On exit, A is overwritten by the reordered matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in,out)

B is COMPLEX array, dimension(LDB,N) On entry, the upper triangular matrix B, in generalized Schur canonical form. On exit, B is overwritten by the reordered matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### ALPHA (out)

ALPHA is COMPLEX array, dimension (N)

### BETA (out)

BETA is COMPLEX array, dimension (N) The diagonal elements of A and B, respectively, when the pair (A,B) has been reduced to generalized Schur form. ALPHA(i)/BETA(i) i=1,...,N are the generalized eigenvalues.

### Q (in,out)

Q is COMPLEX array, dimension (LDQ,N) On entry, if WANTQ = .TRUE., Q is an N-by-N matrix. On exit, Q has been postmultiplied by the left unitary transformation matrix which reorder (A, B); The leading M columns of Q form orthonormal bases for the specified pair of left eigenspaces (deflating subspaces). If WANTQ = .FALSE., Q is not referenced.

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= 1. If WANTQ = .TRUE., LDQ >= N.

### Z (in,out)

Z is COMPLEX array, dimension (LDZ,N) On entry, if WANTZ = .TRUE., Z is an N-by-N matrix. On exit, Z has been postmultiplied by the left unitary transformation matrix which reorder (A, B); The leading M columns of Z form orthonormal bases for the specified pair of left eigenspaces (deflating subspaces). If WANTZ = .FALSE., Z is not referenced.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1. If WANTZ = .TRUE., LDZ >= N.

### M (out)

M is INTEGER The dimension of the specified pair of left and right eigenspaces, (deflating subspaces) 0 <= M <= N.

### PL (out)

PL is REAL

### PR (out)

PR is REAL If IJOB = 1, 4 or 5, PL, PR are lower bounds on the reciprocal of the norm of "projections" onto left and right eigenspace with respect to the selected cluster. 0 < PL, PR <= 1. If M = 0 or M = N, PL = PR = 1. If IJOB = 0, 2 or 3 PL, PR are not referenced.

### DIF (out)

DIF is REAL array, dimension (2). If IJOB >= 2, DIF(1:2) store the estimates of Difu and Difl. If IJOB = 2 or 4, DIF(1:2) are F-norm-based upper bounds on Difu and Difl. If IJOB = 3 or 5, DIF(1:2) are 1-norm-based estimates of Difu and Difl, computed using reversed communication with CLACN2. If M = 0 or N, DIF(1:2) = F-norm([A, B]). If IJOB = 0 or 1, DIF is not referenced.

### WORK (out)

WORK is COMPLEX array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= 1 If IJOB = 1, 2 or 4, LWORK >= 2*M*(N-M) If IJOB = 3 or 5, LWORK >= 4*M*(N-M) If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### IWORK (out)

IWORK is INTEGER array, dimension (MAX(1,LIWORK)) On exit, if INFO = 0, IWORK(1) returns the optimal LIWORK.

### LIWORK (in)

LIWORK is INTEGER The dimension of the array IWORK. LIWORK >= 1. If IJOB = 1, 2 or 4, LIWORK >= N+2; If IJOB = 3 or 5, LIWORK >= MAX(N+2, 2*M*(N-M)); If LIWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the IWORK array, returns this value as the first entry of the IWORK array, and no error message related to LIWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER =0: Successful exit. <0: If INFO = -i, the i-th argument had an illegal value. =1: Reordering of (A, B) failed because the transformed matrix pair (A, B) would be too far from generalized Schur form; the problem is very ill-conditioned. (A, B) may have been partially reordered. If requested, 0 is returned in DIF(*), PL and PR.

