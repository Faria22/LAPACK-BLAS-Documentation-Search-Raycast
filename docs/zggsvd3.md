# ZGGSVD3

ZGGSVD3 computes the singular value decomposition (SVD) for OTHER matrices

## Function Signature

```fortran
ZGGSVD3(JOBU, JOBV, JOBQ, M, N, P, K, L, A, LDA, B,
*                           LDB, ALPHA, BETA, U, LDU, V, LDV, Q, LDQ, WORK,
*                           LWORK, RWORK, IWORK, INFO)
```

## Description


 ZGGSVD3 computes the generalized singular value decomposition (GSVD)
 of an M-by-N complex matrix A and P-by-N complex matrix B:

       U**H*A*Q = D1*( 0 R ),    V**H*B*Q = D2*( 0 R )

 where U, V and Q are unitary matrices.
 Let K+L = the effective numerical rank of the
 matrix (A**H,B**H)**H, then R is a (K+L)-by-(K+L) nonsingular upper
 triangular matrix, D1 and D2 are M-by-(K+L) and P-by-(K+L) "diagonal"
 matrices and of the following structures, respectively:

 If M-K-L >= 0,

                     K  L
        D1 =     K ( I  0 )
                 L ( 0  C )
             M-K-L ( 0  0 )

                   K  L
        D2 =   L ( 0  S )
             P-L ( 0  0 )

                 N-K-L  K    L
   ( 0 R ) = K (  0   R11  R12 )
             L (  0    0   R22 )
 where

   C = diag( ALPHA(K+1), ... , ALPHA(K+L) ),
   S = diag( BETA(K+1),  ... , BETA(K+L) ),
   C**2 + S**2 = I.

   R is stored in A(1:K+L,N-K-L+1:N) on exit.

 If M-K-L < 0,

                   K M-K K+L-M
        D1 =   K ( I  0    0   )
             M-K ( 0  C    0   )

                     K M-K K+L-M
        D2 =   M-K ( 0  S    0  )
             K+L-M ( 0  0    I  )
               P-L ( 0  0    0  )

                    N-K-L  K   M-K  K+L-M
   ( 0 R ) =     K ( 0    R11  R12  R13  )
               M-K ( 0     0   R22  R23  )
             K+L-M ( 0     0    0   R33  )

 where

   C = diag( ALPHA(K+1), ... , ALPHA(M) ),
   S = diag( BETA(K+1),  ... , BETA(M) ),
   C**2 + S**2 = I.

   (R11 R12 R13 ) is stored in A(1:M, N-K-L+1:N), and R33 is stored
   ( 0  R22 R23 )
   in B(M-K+1:L,N+M-K-L+1:N) on exit.

 The routine computes C, S, R, and optionally the unitary
 transformation matrices U, V and Q.

 In particular, if B is an N-by-N nonsingular matrix, then the GSVD of
 A and B implicitly gives the SVD of A*inv(B):
                      A*inv(B) = U*(D1*inv(D2))*V**H.
 If ( A**H,B**H)**H has orthonormal columns, then the GSVD of A and B is also
 equal to the CS decomposition of A and B. Furthermore, the GSVD can
 be used to derive the solution of the eigenvalue problem:
                      A**H*A x = lambda* B**H*B x.
 In some literature, the GSVD of A and B is presented in the form
                  U**H*A*X = ( 0 D1 ),   V**H*B*X = ( 0 D2 )
 where U and V are orthogonal and X is nonsingular, and D1 and D2 are
 ``diagonal''.  The former GSVD form can be converted to the latter
 form by taking the nonsingular matrix X as

                       X = Q*(  I   0    )
                             (  0 inv(R) )

## Parameters

### JOBU (in)

JOBU is CHARACTER*1 = 'U': Unitary matrix U is computed; = 'N': U is not computed.

### JOBV (in)

JOBV is CHARACTER*1 = 'V': Unitary matrix V is computed; = 'N': V is not computed.

### JOBQ (in)

JOBQ is CHARACTER*1 = 'Q': Unitary matrix Q is computed; = 'N': Q is not computed.

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrices A and B. N >= 0.

### P (in)

P is INTEGER The number of rows of the matrix B. P >= 0.

### K (out)

K is INTEGER

### L (out)

L is INTEGER On exit, K and L specify the dimension of the subblocks described in Purpose. K + L = effective numerical rank of (A**H,B**H)**H.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the M-by-N matrix A. On exit, A contains the triangular matrix R, or part of R. See Purpose for details.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,N) On entry, the P-by-N matrix B. On exit, B contains part of the triangular matrix R if M-K-L < 0. See Purpose for details.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,P).

### ALPHA (out)

ALPHA is DOUBLE PRECISION array, dimension (N)

### BETA (out)

BETA is DOUBLE PRECISION array, dimension (N) On exit, ALPHA and BETA contain the generalized singular value pairs of A and B; ALPHA(1:K) = 1, BETA(1:K) = 0, and if M-K-L >= 0, ALPHA(K+1:K+L) = C, BETA(K+1:K+L) = S, or if M-K-L < 0, ALPHA(K+1:M)=C, ALPHA(M+1:K+L)=0 BETA(K+1:M) =S, BETA(M+1:K+L) =1 and ALPHA(K+L+1:N) = 0 BETA(K+L+1:N) = 0

### U (out)

U is COMPLEX*16 array, dimension (LDU,M) If JOBU = 'U', U contains the M-by-M unitary matrix U. If JOBU = 'N', U is not referenced.

### LDU (in)

LDU is INTEGER The leading dimension of the array U. LDU >= max(1,M) if JOBU = 'U'; LDU >= 1 otherwise.

### V (out)

V is COMPLEX*16 array, dimension (LDV,P) If JOBV = 'V', V contains the P-by-P unitary matrix V. If JOBV = 'N', V is not referenced.

### LDV (in)

LDV is INTEGER The leading dimension of the array V. LDV >= max(1,P) if JOBV = 'V'; LDV >= 1 otherwise.

### Q (out)

Q is COMPLEX*16 array, dimension (LDQ,N) If JOBQ = 'Q', Q contains the N-by-N unitary matrix Q. If JOBQ = 'N', Q is not referenced.

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= max(1,N) if JOBQ = 'Q'; LDQ >= 1 otherwise.

### WORK (out)

WORK is COMPLEX*16 array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= 1. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (2*N)

### IWORK (out)

IWORK is INTEGER array, dimension (N) On exit, IWORK stores the sorting information. More precisely, the following loop will sort ALPHA for I = K+1, min(M,K+L) swap ALPHA(I) and ALPHA(IWORK(I)) endfor such that ALPHA(1) >= ALPHA(2) >= ... >= ALPHA(N).

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value. > 0: if INFO = 1, the Jacobi-type procedure failed to converge. For further details, see subroutine ZTGSJA.

