# ZTRSNA

## Function Signature

```fortran
ZTRSNA(JOB, HOWMNY, SELECT, N, T, LDT, VL, LDVL, VR,
*                          LDVR, S, SEP, MM, M, WORK, LDWORK, RWORK,
*                          INFO)
```

## Description


 ZTRSNA estimates reciprocal condition numbers for specified
 eigenvalues and/or right eigenvectors of a complex upper triangular
 matrix T (or of any matrix Q*T*Q**H with Q unitary).

## Parameters

### JOB (in)

JOB is CHARACTER*1 Specifies whether condition numbers are required for eigenvalues (S) or eigenvectors (SEP): = 'E': for eigenvalues only (S); = 'V': for eigenvectors only (SEP); = 'B': for both eigenvalues and eigenvectors (S and SEP).

### HOWMNY (in)

HOWMNY is CHARACTER*1 = 'A': compute condition numbers for all eigenpairs; = 'S': compute condition numbers for selected eigenpairs specified by the array SELECT.

### SELECT (in)

SELECT is LOGICAL array, dimension (N) If HOWMNY = 'S', SELECT specifies the eigenpairs for which condition numbers are required. To select condition numbers for the j-th eigenpair, SELECT(j) must be set to .TRUE.. If HOWMNY = 'A', SELECT is not referenced.

### N (in)

N is INTEGER The order of the matrix T. N >= 0.

### T (in)

T is COMPLEX*16 array, dimension (LDT,N) The upper triangular matrix T.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= max(1,N).

### VL (in)

VL is COMPLEX*16 array, dimension (LDVL,M) If JOB = 'E' or 'B', VL must contain left eigenvectors of T (or of any Q*T*Q**H with Q unitary), corresponding to the eigenpairs specified by HOWMNY and SELECT. The eigenvectors must be stored in consecutive columns of VL, as returned by ZHSEIN or ZTREVC. If JOB = 'V', VL is not referenced.

### LDVL (in)

LDVL is INTEGER The leading dimension of the array VL. LDVL >= 1; and if JOB = 'E' or 'B', LDVL >= N.

### VR (in)

VR is COMPLEX*16 array, dimension (LDVR,M) If JOB = 'E' or 'B', VR must contain right eigenvectors of T (or of any Q*T*Q**H with Q unitary), corresponding to the eigenpairs specified by HOWMNY and SELECT. The eigenvectors must be stored in consecutive columns of VR, as returned by ZHSEIN or ZTREVC. If JOB = 'V', VR is not referenced.

### LDVR (in)

LDVR is INTEGER The leading dimension of the array VR. LDVR >= 1; and if JOB = 'E' or 'B', LDVR >= N.

### S (out)

S is DOUBLE PRECISION array, dimension (MM) If JOB = 'E' or 'B', the reciprocal condition numbers of the selected eigenvalues, stored in consecutive elements of the array. Thus S(j), SEP(j), and the j-th columns of VL and VR all correspond to the same eigenpair (but not in general the j-th eigenpair, unless all eigenpairs are selected). If JOB = 'V', S is not referenced.

### SEP (out)

SEP is DOUBLE PRECISION array, dimension (MM) If JOB = 'V' or 'B', the estimated reciprocal condition numbers of the selected eigenvectors, stored in consecutive elements of the array. If JOB = 'E', SEP is not referenced.

### MM (in)

MM is INTEGER The number of elements in the arrays S (if JOB = 'E' or 'B') and/or SEP (if JOB = 'V' or 'B'). MM >= M.

### M (out)

M is INTEGER The number of elements of the arrays S and/or SEP actually used to store the estimated condition numbers. If HOWMNY = 'A', M is set to N.

### WORK (out)

WORK is COMPLEX*16 array, dimension (LDWORK,N+6) If JOB = 'E', WORK is not referenced.

### LDWORK (in)

LDWORK is INTEGER The leading dimension of the array WORK. LDWORK >= 1; and if JOB = 'V' or 'B', LDWORK >= N.

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (N) If JOB = 'E', RWORK is not referenced.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

