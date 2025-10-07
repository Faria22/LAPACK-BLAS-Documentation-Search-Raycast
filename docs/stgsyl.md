# STGSYL

## Function Signature

```fortran
STGSYL(TRANS, IJOB, M, N, A, LDA, B, LDB, C, LDC, D,
*                          LDD, E, LDE, F, LDF, SCALE, DIF, WORK, LWORK,
*                          IWORK, INFO)
```

## Description


 STGSYL solves the generalized Sylvester equation:

             A * R - L * B = scale * C                 (1)
             D * R - L * E = scale * F

 where R and L are unknown m-by-n matrices, (A, D), (B, E) and
 (C, F) are given matrix pairs of size m-by-m, n-by-n and m-by-n,
 respectively, with real entries. (A, D) and (B, E) must be in
 generalized (real) Schur canonical form, i.e. A, B are upper quasi
 triangular and D, E are upper triangular.

 The solution (R, L) overwrites (C, F). 0 <= SCALE <= 1 is an output
 scaling factor chosen to avoid overflow.

 In matrix notation (1) is equivalent to solve  Zx = scale b, where
 Z is defined as

            Z = [ kron(In, A)  -kron(B**T, Im) ]         (2)
                [ kron(In, D)  -kron(E**T, Im) ].

 Here Ik is the identity matrix of size k and X**T is the transpose of
 X. kron(X, Y) is the Kronecker product between the matrices X and Y.

 If TRANS = 'T', STGSYL solves the transposed system Z**T*y = scale*b,
 which is equivalent to solve for R and L in

             A**T * R + D**T * L = scale * C           (3)
             R * B**T + L * E**T = scale * -F

 This case (TRANS = 'T') is used to compute an one-norm-based estimate
 of Dif[(A,D), (B,E)], the separation between the matrix pairs (A,D)
 and (B,E), using SLACON.

 If IJOB >= 1, STGSYL computes a Frobenius norm-based estimate
 of Dif[(A,D),(B,E)]. That is, the reciprocal of a lower bound on the
 reciprocal of the smallest singular value of Z. See [1-2] for more
 information.

 This is a level 3 BLAS algorithm.

## Parameters

### TRANS (in)

TRANS is CHARACTER*1 = 'N': solve the generalized Sylvester equation (1). = 'T': solve the 'transposed' system (3).

### IJOB (in)

IJOB is INTEGER Specifies what kind of functionality to be performed. = 0: solve (1) only. = 1: The functionality of 0 and 3. = 2: The functionality of 0 and 4. = 3: Only an estimate of Dif[(A,D), (B,E)] is computed. (look ahead strategy IJOB = 1 is used). = 4: Only an estimate of Dif[(A,D), (B,E)] is computed. ( SGECON on sub-systems is used ). Not referenced if TRANS = 'T'.

### M (in)

M is INTEGER The order of the matrices A and D, and the row dimension of the matrices C, F, R and L.

### N (in)

N is INTEGER The order of the matrices B and E, and the column dimension of the matrices C, F, R and L.

### A (in)

A is REAL array, dimension (LDA, M) The upper quasi triangular matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1, M).

### B (in)

B is REAL array, dimension (LDB, N) The upper quasi triangular matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1, N).

### C (in,out)

C is REAL array, dimension (LDC, N) On entry, C contains the right-hand-side of the first matrix equation in (1) or (3). On exit, if IJOB = 0, 1 or 2, C has been overwritten by the solution R. If IJOB = 3 or 4 and TRANS = 'N', C holds R, the solution achieved during the computation of the Dif-estimate.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1, M).

### D (in)

D is REAL array, dimension (LDD, M) The upper triangular matrix D.

### LDD (in)

LDD is INTEGER The leading dimension of the array D. LDD >= max(1, M).

### E (in)

E is REAL array, dimension (LDE, N) The upper triangular matrix E.

### LDE (in)

LDE is INTEGER The leading dimension of the array E. LDE >= max(1, N).

### F (in,out)

F is REAL array, dimension (LDF, N) On entry, F contains the right-hand-side of the second matrix equation in (1) or (3). On exit, if IJOB = 0, 1 or 2, F has been overwritten by the solution L. If IJOB = 3 or 4 and TRANS = 'N', F holds L, the solution achieved during the computation of the Dif-estimate.

### LDF (in)

LDF is INTEGER The leading dimension of the array F. LDF >= max(1, M).

### DIF (out)

DIF is REAL On exit DIF is the reciprocal of a lower bound of the reciprocal of the Dif-function, i.e. DIF is an upper bound of Dif[(A,D), (B,E)] = sigma_min(Z), where Z as in (2). IF IJOB = 0 or TRANS = 'T', DIF is not touched.

### SCALE (out)

SCALE is REAL On exit SCALE is the scaling factor in (1) or (3). If 0 < SCALE < 1, C and F hold the solutions R and L, resp., to a slightly perturbed system but the input matrices A, B, D and E have not been changed. If SCALE = 0, C and F hold the solutions R and L, respectively, to the homogeneous system with C = F = 0. Normally, SCALE = 1.

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK > = 1. If IJOB = 1 or 2 and TRANS = 'N', LWORK >= max(1,2*M*N). If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### IWORK (out)

IWORK is INTEGER array, dimension (M+N+6)

### INFO (out)

INFO is INTEGER =0: successful exit <0: If INFO = -i, the i-th argument had an illegal value. >0: (A, D) and (B, E) have common or close eigenvalues.

