# SGEQP3RK

## Function Signature

```fortran
SGEQP3RK(M, N, NRHS, KMAX, ABSTOL, RELTOL, A, LDA,
*      $                     K, MAXC2NRMK, RELMAXC2NRMK, JPIV, TAU,
*      $                     WORK, LWORK, IWORK, INFO)
```

## Description


 SGEQP3RK performs two tasks simultaneously:

 Task 1: The routine computes a truncated (rank K) or full rank
 Householder QR factorization with column pivoting of a real
 M-by-N matrix A using Level 3 BLAS. K is the number of columns
 that were factorized, i.e. factorization rank of the
 factor R, K <= min(M,N).

  A * P(K) = Q(K) * R(K)  =

        = Q(K) * ( R11(K) R12(K) ) = Q(K) * (   R(K)_approx    )
                 ( 0      R22(K) )          ( 0  R(K)_residual ),

 where:

  P(K)            is an N-by-N permutation matrix;
  Q(K)            is an M-by-M orthogonal matrix;
  R(K)_approx   = ( R11(K), R12(K) ) is a rank K approximation of the
                    full rank factor R with K-by-K upper-triangular
                    R11(K) and K-by-N rectangular R12(K). The diagonal
                    entries of R11(K) appear in non-increasing order
                    of absolute value, and absolute values of all of
                    them exceed the maximum column 2-norm of R22(K)
                    up to roundoff error.
  R(K)_residual = R22(K) is the residual of a rank K approximation
                    of the full rank factor R. It is a
                    an (M-K)-by-(N-K) rectangular matrix;
  0               is a an (M-K)-by-K zero matrix.

 Task 2: At the same time, the routine overwrites a real M-by-NRHS
 matrix B with  Q(K)**T * B  using Level 3 BLAS.

 =====================================================================

 The matrices A and B are stored on input in the array A as
 the left and right blocks A(1:M,1:N) and A(1:M, N+1:N+NRHS)
 respectively.

                                  N     NRHS
             array_A   =   M  [ mat_A, mat_B ]

 The truncation criteria (i.e. when to stop the factorization)
 can be any of the following:

   1) The input parameter KMAX, the maximum number of columns
      KMAX to factorize, i.e. the factorization rank is limited
      to KMAX. If KMAX >= min(M,N), the criterion is not used.

   2) The input parameter ABSTOL, the absolute tolerance for
      the maximum column 2-norm of the residual matrix R22(K). This
      means that the factorization stops if this norm is less or
      equal to ABSTOL. If ABSTOL < 0.0, the criterion is not used.

   3) The input parameter RELTOL, the tolerance for the maximum
      column 2-norm matrix of the residual matrix R22(K) divided
      by the maximum column 2-norm of the original matrix A, which
      is equal to abs(R(1,1)). This means that the factorization stops
      when the ratio of the maximum column 2-norm of R22(K) to
      the maximum column 2-norm of A is less than or equal to RELTOL.
      If RELTOL < 0.0, the criterion is not used.

   4) In case both stopping criteria ABSTOL or RELTOL are not used,
      and when the residual matrix R22(K) is a zero matrix in some
      factorization step K. ( This stopping criterion is implicit. )

  The algorithm stops when any of these conditions is first
  satisfied, otherwise the whole matrix A is factorized.

  To factorize the whole matrix A, use the values
  KMAX >= min(M,N), ABSTOL < 0.0 and RELTOL < 0.0.

  The routine returns:
     a) Q(K), R(K)_approx = ( R11(K), R12(K) ),
        R(K)_residual = R22(K), P(K), i.e. the resulting matrices
        of the factorization; P(K) is represented by JPIV,
        ( if K = min(M,N), R(K)_approx is the full factor R,
        and there is no residual matrix R(K)_residual);
     b) K, the number of columns that were factorized,
        i.e. factorization rank;
     c) MAXC2NRMK, the maximum column 2-norm of the residual
        matrix R(K)_residual = R22(K),
        ( if K = min(M,N), MAXC2NRMK = 0.0 );
     d) RELMAXC2NRMK equals MAXC2NRMK divided by MAXC2NRM, the maximum
        column 2-norm of the original matrix A, which is equal
        to abs(R(1,1)), ( if K = min(M,N), RELMAXC2NRMK = 0.0 );
     e) Q(K)**T * B, the matrix B with the orthogonal
        transformation Q(K)**T applied on the left.

 The N-by-N permutation matrix P(K) is stored in a compact form in
 the integer array JPIV. For 1 <= j <= N, column j
 of the matrix A was interchanged with column JPIV(j).

 The M-by-M orthogonal matrix Q is represented as a product
 of elementary Householder reflectors

     Q(K) = H(1) *  H(2) * . . . * H(K),

 where K is the number of columns that were factorized.

 Each H(j) has the form

     H(j) = I - tau * v * v**T,

 where 1 <= j <= K and
   I    is an M-by-M identity matrix,
   tau  is a real scalar,
   v    is a real vector with v(1:j-1) = 0 and v(j) = 1.

 v(j+1:M) is stored on exit in A(j+1:M,j) and tau in TAU(j).

 See the Further Details section for more information.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e. the number of columns of the matrix B. NRHS >= 0.

### KMAX (in)

KMAX is INTEGER The first factorization stopping criterion. KMAX >= 0. The maximum number of columns of the matrix A to factorize, i.e. the maximum factorization rank. a) If KMAX >= min(M,N), then this stopping criterion is not used, the routine factorizes columns depending on ABSTOL and RELTOL. b) If KMAX = 0, then this stopping criterion is satisfied on input and the routine exits immediately. This means that the factorization is not performed, the matrices A and B are not modified, and the matrix A is itself the residual.

### ABSTOL (in)

ABSTOL is REAL The second factorization stopping criterion, cannot be NaN. The absolute tolerance (stopping threshold) for maximum column 2-norm of the residual matrix R22(K). The algorithm converges (stops the factorization) when the maximum column 2-norm of the residual matrix R22(K) is less than or equal to ABSTOL. Let SAFMIN = SLAMCH('S'). a) If ABSTOL is NaN, then no computation is performed and an error message ( INFO = -5 ) is issued by XERBLA. b) If ABSTOL < 0.0, then this stopping criterion is not used, the routine factorizes columns depending on KMAX and RELTOL. This includes the case ABSTOL = -Inf. c) If 0.0 <= ABSTOL < 2*SAFMIN, then ABSTOL = 2*SAFMIN is used. This includes the case ABSTOL = -0.0. d) If 2*SAFMIN <= ABSTOL then the input value of ABSTOL is used. Let MAXC2NRM be the maximum column 2-norm of the whole original matrix A. If ABSTOL chosen above is >= MAXC2NRM, then this stopping criterion is satisfied on input and routine exits immediately after MAXC2NRM is computed. The routine returns MAXC2NRM in MAXC2NORMK, and 1.0 in RELMAXC2NORMK. This includes the case ABSTOL = +Inf. This means that the factorization is not performed, the matrices A and B are not modified, and the matrix A is itself the residual.

### RELTOL (in)

RELTOL is REAL The third factorization stopping criterion, cannot be NaN. The tolerance (stopping threshold) for the ratio abs(R(K+1,K+1))/abs(R(1,1)) of the maximum column 2-norm of the residual matrix R22(K) to the maximum column 2-norm of the original matrix A. The algorithm converges (stops the factorization), when abs(R(K+1,K+1))/abs(R(1,1)) A is less than or equal to RELTOL. Let EPS = SLAMCH('E'). a) If RELTOL is NaN, then no computation is performed and an error message ( INFO = -6 ) is issued by XERBLA. b) If RELTOL < 0.0, then this stopping criterion is not used, the routine factorizes columns depending on KMAX and ABSTOL. This includes the case RELTOL = -Inf. c) If 0.0 <= RELTOL < EPS, then RELTOL = EPS is used. This includes the case RELTOL = -0.0. d) If EPS <= RELTOL then the input value of RELTOL is used. Let MAXC2NRM be the maximum column 2-norm of the whole original matrix A. If RELTOL chosen above is >= 1.0, then this stopping criterion is satisfied on input and routine exits immediately after MAXC2NRM is computed. The routine returns MAXC2NRM in MAXC2NORMK, and 1.0 in RELMAXC2NORMK. This includes the case RELTOL = +Inf. This means that the factorization is not performed, the matrices A and B are not modified, and the matrix A is itself the residual. NOTE: We recommend that RELTOL satisfy min( max(M,N)*EPS, sqrt(EPS) ) <= RELTOL

### A (in,out)

A is REAL array, dimension (LDA,N+NRHS) On entry: a) The subarray A(1:M,1:N) contains the M-by-N matrix A. b) The subarray A(1:M,N+1:N+NRHS) contains the M-by-NRHS matrix B. N NRHS array_A = M [ mat_A, mat_B ] On exit: a) The subarray A(1:M,1:N) contains parts of the factors of the matrix A: 1) If K = 0, A(1:M,1:N) contains the original matrix A. 2) If K > 0, A(1:M,1:N) contains parts of the factors: 1. The elements below the diagonal of the subarray A(1:M,1:K) together with TAU(1:K) represent the orthogonal matrix Q(K) as a product of K Householder elementary reflectors. 2. The elements on and above the diagonal of the subarray A(1:K,1:N) contain K-by-N upper-trapezoidal matrix R(K)_approx = ( R11(K), R12(K) ). NOTE: If K=min(M,N), i.e. full rank factorization, then R_approx(K) is the full factor R which is upper-trapezoidal. If, in addition, M>=N, then R is upper-triangular. 3. The subarray A(K+1:M,K+1:N) contains (M-K)-by-(N-K) rectangular matrix R(K)_residual = R22(K). b) If NRHS > 0, the subarray A(1:M,N+1:N+NRHS) contains the M-by-NRHS product Q(K)**T * B.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M). This is the leading dimension for both matrices, A and B.

### K (out)

K is INTEGER Factorization rank of the matrix A, i.e. the rank of the factor R, which is the same as the number of non-zero rows of the factor R. 0 <= K <= min(M,KMAX,N). K also represents the number of non-zero Householder vectors. NOTE: If K = 0, a) the arrays A and B are not modified; b) the array TAU(1:min(M,N)) is set to ZERO, if the matrix A does not contain NaN, otherwise the elements TAU(1:min(M,N)) are undefined; c) the elements of the array JPIV are set as follows: for j = 1:N, JPIV(j) = j.

### MAXC2NRMK (out)

MAXC2NRMK is REAL The maximum column 2-norm of the residual matrix R22(K), when the factorization stopped at rank K. MAXC2NRMK >= 0. a) If K = 0, i.e. the factorization was not performed, the matrix A was not modified and is itself a residual matrix, then MAXC2NRMK equals the maximum column 2-norm of the original matrix A. b) If 0 < K < min(M,N), then MAXC2NRMK is returned. c) If K = min(M,N), i.e. the whole matrix A was factorized and there is no residual matrix, then MAXC2NRMK = 0.0. NOTE: MAXC2NRMK in the factorization step K would equal R(K+1,K+1) in the next factorization step K+1.

### RELMAXC2NRMK (out)

RELMAXC2NRMK is REAL The ratio MAXC2NRMK / MAXC2NRM of the maximum column 2-norm of the residual matrix R22(K) (when the factorization stopped at rank K) to the maximum column 2-norm of the whole original matrix A. RELMAXC2NRMK >= 0. a) If K = 0, i.e. the factorization was not performed, the matrix A was not modified and is itself a residual matrix, then RELMAXC2NRMK = 1.0. b) If 0 < K < min(M,N), then RELMAXC2NRMK = MAXC2NRMK / MAXC2NRM is returned. c) If K = min(M,N), i.e. the whole matrix A was factorized and there is no residual matrix, then RELMAXC2NRMK = 0.0. NOTE: RELMAXC2NRMK in the factorization step K would equal abs(R(K+1,K+1))/abs(R(1,1)) in the next factorization step K+1.

### JPIV (out)

JPIV is INTEGER array, dimension (N) Column pivot indices. For 1 <= j <= N, column j of the matrix A was interchanged with column JPIV(j). The elements of the array JPIV(1:N) are always set by the routine, for example, even when no columns were factorized, i.e. when K = 0, the elements are set as JPIV(j) = j for j = 1:N.

### TAU (out)

TAU is REAL array, dimension (min(M,N)) The scalar factors of the elementary reflectors. If 0 < K <= min(M,N), only the elements TAU(1:K) of the array TAU are modified by the factorization. After the factorization computed, if no NaN was found during the factorization, the remaining elements TAU(K+1:min(M,N)) are set to zero, otherwise the elements TAU(K+1:min(M,N)) are not set and therefore undefined. ( If K = 0, all elements of TAU are set to zero, if the matrix A does not contain NaN. )

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= 1, if MIN(M,N) = 0, and LWORK >= (3*N+NRHS-1), otherwise. For optimal performance LWORK >= (2*N + NB*( N+NRHS+1 )), where NB is the optimal block size for SGEQP3RK returned by ILAENV. Minimal block size MINNB=2. NOTE: The decision, whether to use unblocked BLAS 2 or blocked BLAS 3 code is based not only on the dimension LWORK of the availbale workspace WORK, but also also on the matrix A dimension N via crossover point NX returned by ILAENV. (For N less than NX, unblocked code should be used.) If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### IWORK (out)

IWORK is INTEGER array, dimension (N-1). Is a work array. ( IWORK is used to store indices of "bad" columns for norm downdating in the residual matrix in the blocked step auxiliary subroutine SLAQP3RK ).

### INFO (out)

INFO is INTEGER 1) INFO = 0: successful exit. 2) INFO < 0: if INFO = -i, the i-th argument had an illegal value. 3) If INFO = j_1, where 1 <= j_1 <= N, then NaN was detected and the routine stops the computation. The j_1-th column of the matrix A or the j_1-th element of array TAU contains the first occurrence of NaN in the factorization step K+1 ( when K columns have been factorized ). On exit: K is set to the number of factorized columns without exception. MAXC2NRMK is set to NaN. RELMAXC2NRMK is set to NaN. TAU(K+1:min(M,N)) is not set and contains undefined elements. If j_1=K+1, TAU(K+1) may contain NaN. 4) If INFO = j_2, where N+1 <= j_2 <= 2*N, then no NaN was detected, but +Inf (or -Inf) was detected and the routine continues the computation until completion. The (j_2-N)-th column of the matrix A contains the first occurrence of +Inf (or -Inf) in the factorization step K+1 ( when K columns have been factorized ).

