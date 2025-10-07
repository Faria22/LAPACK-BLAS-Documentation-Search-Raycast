# STRSNA

## Function Signature

```fortran
STRSNA(JOB, HOWMNY, SELECT, N, T, LDT, VL, LDVL, VR,
*                          LDVR, S, SEP, MM, M, WORK, LDWORK, IWORK,
*                          INFO)
```

## Description


 STRSNA estimates reciprocal condition numbers for specified
 eigenvalues and/or right eigenvectors of a real upper
 quasi-triangular matrix T (or of any matrix Q*T*Q**T with Q
 orthogonal).

 T must be in Schur canonical form (as returned by SHSEQR), that is,
 block upper triangular with 1-by-1 and 2-by-2 diagonal blocks; each
 2-by-2 diagonal block has its diagonal elements equal and its
 off-diagonal elements of opposite sign.

## Parameters

### JOB (in)

JOB is CHARACTER*1 Specifies whether condition numbers are required for eigenvalues (S) or eigenvectors (SEP): = 'E': for eigenvalues only (S); = 'V': for eigenvectors only (SEP); = 'B': for both eigenvalues and eigenvectors (S and SEP).

### HOWMNY (in)

HOWMNY is CHARACTER*1 = 'A': compute condition numbers for all eigenpairs; = 'S': compute condition numbers for selected eigenpairs specified by the array SELECT.

### SELECT (in)

SELECT is LOGICAL array, dimension (N) If HOWMNY = 'S', SELECT specifies the eigenpairs for which condition numbers are required. To select condition numbers for the eigenpair corresponding to a real eigenvalue w(j), SELECT(j) must be set to .TRUE.. To select condition numbers corresponding to a complex conjugate pair of eigenvalues w(j) and w(j+1), either SELECT(j) or SELECT(j+1) or both, must be set to .TRUE.. If HOWMNY = 'A', SELECT is not referenced.

### N (in)

N is INTEGER The order of the matrix T. N >= 0.

### T (in)

T is REAL array, dimension (LDT,N) The upper quasi-triangular matrix T, in Schur canonical form.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= max(1,N).

### VL (in)

VL is REAL array, dimension (LDVL,M) If JOB = 'E' or 'B', VL must contain left eigenvectors of T (or of any Q*T*Q**T with Q orthogonal), corresponding to the eigenpairs specified by HOWMNY and SELECT. The eigenvectors must be stored in consecutive columns of VL, as returned by SHSEIN or STREVC. If JOB = 'V', VL is not referenced.

### LDVL (in)

LDVL is INTEGER The leading dimension of the array VL. LDVL >= 1; and if JOB = 'E' or 'B', LDVL >= N.

### VR (in)

VR is REAL array, dimension (LDVR,M) If JOB = 'E' or 'B', VR must contain right eigenvectors of T (or of any Q*T*Q**T with Q orthogonal), corresponding to the eigenpairs specified by HOWMNY and SELECT. The eigenvectors must be stored in consecutive columns of VR, as returned by SHSEIN or STREVC. If JOB = 'V', VR is not referenced.

### LDVR (in)

LDVR is INTEGER The leading dimension of the array VR. LDVR >= 1; and if JOB = 'E' or 'B', LDVR >= N.

### S (out)

S is REAL array, dimension (MM) If JOB = 'E' or 'B', the reciprocal condition numbers of the selected eigenvalues, stored in consecutive elements of the array. For a complex conjugate pair of eigenvalues two consecutive elements of S are set to the same value. Thus S(j), SEP(j), and the j-th columns of VL and VR all correspond to the same eigenpair (but not in general the j-th eigenpair, unless all eigenpairs are selected). If JOB = 'V', S is not referenced.

### SEP (out)

SEP is REAL array, dimension (MM) If JOB = 'V' or 'B', the estimated reciprocal condition numbers of the selected eigenvectors, stored in consecutive elements of the array. For a complex eigenvector two consecutive elements of SEP are set to the same value. If the eigenvalues cannot be reordered to compute SEP(j), SEP(j) is set to 0; this can only occur when the true value would be very small anyway. If JOB = 'E', SEP is not referenced.

### MM (in)

MM is INTEGER The number of elements in the arrays S (if JOB = 'E' or 'B') and/or SEP (if JOB = 'V' or 'B'). MM >= M.

### M (out)

M is INTEGER The number of elements of the arrays S and/or SEP actually used to store the estimated condition numbers. If HOWMNY = 'A', M is set to N.

### WORK (out)

WORK is REAL array, dimension (LDWORK,N+6) If JOB = 'E', WORK is not referenced.

### LDWORK (in)

LDWORK is INTEGER The leading dimension of the array WORK. LDWORK >= 1; and if JOB = 'V' or 'B', LDWORK >= N.

### IWORK (out)

IWORK is INTEGER array, dimension (2*(N-1)) If JOB = 'E', IWORK is not referenced.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

