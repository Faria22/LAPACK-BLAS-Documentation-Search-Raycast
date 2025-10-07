# SGGSVP3

## Function Signature

```fortran
SGGSVP3(JOBU, JOBV, JOBQ, M, P, N, A, LDA, B, LDB,
*                           TOLA, TOLB, K, L, U, LDU, V, LDV, Q, LDQ,
*                           IWORK, TAU, WORK, LWORK, INFO)
```

## Description


 SGGSVP3 computes orthogonal matrices U, V and Q such that

                    N-K-L  K    L
  U**T*A*Q =     K ( 0    A12  A13 )  if M-K-L >= 0;
                 L ( 0     0   A23 )
             M-K-L ( 0     0    0  )

                  N-K-L  K    L
         =     K ( 0    A12  A13 )  if M-K-L < 0;
             M-K ( 0     0   A23 )

                  N-K-L  K    L
  V**T*B*Q =   L ( 0     0   B13 )
             P-L ( 0     0    0  )

 where the K-by-K matrix A12 and L-by-L matrix B13 are nonsingular
 upper triangular; A23 is L-by-L upper triangular if M-K-L >= 0,
 otherwise A23 is (M-K)-by-L upper trapezoidal.  K+L = the effective
 numerical rank of the (M+P)-by-N matrix (A**T,B**T)**T.

 This decomposition is the preprocessing step for computing the
 Generalized Singular Value Decomposition (GSVD), see subroutine
 SGGSVD3.

## Parameters

### JOBU (in)

JOBU is CHARACTER*1 = 'U': Orthogonal matrix U is computed; = 'N': U is not computed.

### JOBV (in)

JOBV is CHARACTER*1 = 'V': Orthogonal matrix V is computed; = 'N': V is not computed.

### JOBQ (in)

JOBQ is CHARACTER*1 = 'Q': Orthogonal matrix Q is computed; = 'N': Q is not computed.

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### P (in)

P is INTEGER The number of rows of the matrix B. P >= 0.

### N (in)

N is INTEGER The number of columns of the matrices A and B. N >= 0.

### A (in,out)

A is REAL array, dimension (LDA,N) On entry, the M-by-N matrix A. On exit, A contains the triangular (or trapezoidal) matrix described in the Purpose section.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### B (in,out)

B is REAL array, dimension (LDB,N) On entry, the P-by-N matrix B. On exit, B contains the triangular matrix described in the Purpose section.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,P).

### TOLA (in)

TOLA is REAL

### TOLB (in)

TOLB is REAL TOLA and TOLB are the thresholds to determine the effective numerical rank of matrix B and a subblock of A. Generally, they are set to TOLA = MAX(M,N)*norm(A)*MACHEPS, TOLB = MAX(P,N)*norm(B)*MACHEPS. The size of TOLA and TOLB may affect the size of backward errors of the decomposition.

### K (out)

K is INTEGER

### L (out)

L is INTEGER On exit, K and L specify the dimension of the subblocks described in Purpose section. K + L = effective numerical rank of (A**T,B**T)**T.

### U (out)

U is REAL array, dimension (LDU,M) If JOBU = 'U', U contains the orthogonal matrix U. If JOBU = 'N', U is not referenced.

### LDU (in)

LDU is INTEGER The leading dimension of the array U. LDU >= max(1,M) if JOBU = 'U'; LDU >= 1 otherwise.

### V (out)

V is REAL array, dimension (LDV,P) If JOBV = 'V', V contains the orthogonal matrix V. If JOBV = 'N', V is not referenced.

### LDV (in)

LDV is INTEGER The leading dimension of the array V. LDV >= max(1,P) if JOBV = 'V'; LDV >= 1 otherwise.

### Q (out)

Q is REAL array, dimension (LDQ,N) If JOBQ = 'Q', Q contains the orthogonal matrix Q. If JOBQ = 'N', Q is not referenced.

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= max(1,N) if JOBQ = 'Q'; LDQ >= 1 otherwise.

### IWORK (out)

IWORK is INTEGER array, dimension (N)

### TAU (out)

TAU is REAL array, dimension (N)

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= 1. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value.

