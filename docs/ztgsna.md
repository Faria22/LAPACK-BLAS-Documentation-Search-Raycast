# ZTGSNA

## Function Signature

```fortran
ZTGSNA(JOB, HOWMNY, SELECT, N, A, LDA, B, LDB, VL,
*                          LDVL, VR, LDVR, S, DIF, MM, M, WORK, LWORK,
*                          IWORK, INFO)
```

## Description


 ZTGSNA estimates reciprocal condition numbers for specified
 eigenvalues and/or eigenvectors of a matrix pair (A, B).

 (A, B) must be in generalized Schur canonical form, that is, A and
 B are both upper triangular.

## Parameters

### JOB (in)

JOB is CHARACTER*1 Specifies whether condition numbers are required for eigenvalues (S) or eigenvectors (DIF): = 'E': for eigenvalues only (S); = 'V': for eigenvectors only (DIF); = 'B': for both eigenvalues and eigenvectors (S and DIF).

### HOWMNY (in)

HOWMNY is CHARACTER*1 = 'A': compute condition numbers for all eigenpairs; = 'S': compute condition numbers for selected eigenpairs specified by the array SELECT.

### SELECT (in)

SELECT is LOGICAL array, dimension (N) If HOWMNY = 'S', SELECT specifies the eigenpairs for which condition numbers are required. To select condition numbers for the corresponding j-th eigenvalue and/or eigenvector, SELECT(j) must be set to .TRUE.. If HOWMNY = 'A', SELECT is not referenced.

### N (in)

N is INTEGER The order of the square matrix pair (A, B). N >= 0.

### A (in)

A is COMPLEX*16 array, dimension (LDA,N) The upper triangular matrix A in the pair (A,B).

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in)

B is COMPLEX*16 array, dimension (LDB,N) The upper triangular matrix B in the pair (A, B).

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### VL (in)

VL is COMPLEX*16 array, dimension (LDVL,M) IF JOB = 'E' or 'B', VL must contain left eigenvectors of (A, B), corresponding to the eigenpairs specified by HOWMNY and SELECT. The eigenvectors must be stored in consecutive columns of VL, as returned by ZTGEVC. If JOB = 'V', VL is not referenced.

### LDVL (in)

LDVL is INTEGER The leading dimension of the array VL. LDVL >= 1; and If JOB = 'E' or 'B', LDVL >= N.

### VR (in)

VR is COMPLEX*16 array, dimension (LDVR,M) IF JOB = 'E' or 'B', VR must contain right eigenvectors of (A, B), corresponding to the eigenpairs specified by HOWMNY and SELECT. The eigenvectors must be stored in consecutive columns of VR, as returned by ZTGEVC. If JOB = 'V', VR is not referenced.

### LDVR (in)

LDVR is INTEGER The leading dimension of the array VR. LDVR >= 1; If JOB = 'E' or 'B', LDVR >= N.

### S (out)

S is DOUBLE PRECISION array, dimension (MM) If JOB = 'E' or 'B', the reciprocal condition numbers of the selected eigenvalues, stored in consecutive elements of the array. If JOB = 'V', S is not referenced.

### DIF (out)

DIF is DOUBLE PRECISION array, dimension (MM) If JOB = 'V' or 'B', the estimated reciprocal condition numbers of the selected eigenvectors, stored in consecutive elements of the array. If the eigenvalues cannot be reordered to compute DIF(j), DIF(j) is set to 0; this can only occur when the true value would be very small anyway. For each eigenvalue/vector specified by SELECT, DIF stores a Frobenius norm-based estimate of Difl. If JOB = 'E', DIF is not referenced.

### MM (in)

MM is INTEGER The number of elements in the arrays S and DIF. MM >= M.

### M (out)

M is INTEGER The number of elements of the arrays S and DIF used to store the specified condition numbers; for each selected eigenvalue one element is used. If HOWMNY = 'A', M is set to N.

### WORK (out)

WORK is COMPLEX*16 array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= max(1,N). If JOB = 'V' or 'B', LWORK >= max(1,2*N*N).

### IWORK (out)

IWORK is INTEGER array, dimension (N+2) If JOB = 'E', IWORK is not referenced.

### INFO (out)

INFO is INTEGER = 0: Successful exit < 0: If INFO = -i, the i-th argument had an illegal value

