# DLAQP2RK

## Function Signature

```fortran
DLAQP2RK(M, N, NRHS, IOFFSET, KMAX, ABSTOL, RELTOL,
*     $                     KP1, MAXC2NRM, A, LDA, K, MAXC2NRMK,
*     $                     RELMAXC2NRMK, JPIV, TAU, VN1, VN2, WORK,
*     $                     INFO)
```

## Description


 DLAQP2RK computes a truncated (rank K) or full rank Householder QR
 factorization with column pivoting of a real matrix
 block A(IOFFSET+1:M,1:N) as

   A * P(K) = Q(K) * R(K).

 The routine uses Level 2 BLAS. The block A(1:IOFFSET,1:N)
 is accordingly pivoted, but not factorized.

 The routine also overwrites the right-hand-sides matrix block B
 stored in A(IOFFSET+1:M,N+1:N+NRHS) with Q(K)**T * B.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### IOFFSET (in)

IOFFSET is INTEGER The number of rows of the matrix A that must be pivoted but not factorized. IOFFSET >= 0. IOFFSET also represents the number of columns of the whole original matrix A_orig that have been factorized in the previous steps.

### KMAX (in)

KMAX is INTEGER The first factorization stopping criterion. KMAX >= 0. The maximum number of columns of the matrix A to factorize, i.e. the maximum factorization rank. a) If KMAX >= min(M-IOFFSET,N), then this stopping criterion is not used, factorize columns depending on ABSTOL and RELTOL. b) If KMAX = 0, then this stopping criterion is satisfied on input and the routine exits immediately. This means that the factorization is not performed, the matrices A and B and the arrays TAU, IPIV are not modified.

### ABSTOL (in)

ABSTOL is DOUBLE PRECISION, cannot be NaN. The second factorization stopping criterion. The absolute tolerance (stopping threshold) for maximum column 2-norm of the residual matrix. The algorithm converges (stops the factorization) when the maximum column 2-norm of the residual matrix is less than or equal to ABSTOL. a) If ABSTOL < 0.0, then this stopping criterion is not used, the routine factorizes columns depending on KMAX and RELTOL. This includes the case ABSTOL = -Inf. b) If 0.0 <= ABSTOL then the input value of ABSTOL is used.

### RELTOL (in)

RELTOL is DOUBLE PRECISION, cannot be NaN. The third factorization stopping criterion. The tolerance (stopping threshold) for the ratio of the maximum column 2-norm of the residual matrix to the maximum column 2-norm of the original matrix A_orig. The algorithm converges (stops the factorization), when this ratio is less than or equal to RELTOL. a) If RELTOL < 0.0, then this stopping criterion is not used, the routine factorizes columns depending on KMAX and ABSTOL. This includes the case RELTOL = -Inf. d) If 0.0 <= RELTOL then the input value of RELTOL is used.

### KP1 (in)

KP1 is INTEGER The index of the column with the maximum 2-norm in the whole original matrix A_orig determined in the main routine DGEQP3RK. 1 <= KP1 <= N_orig_mat.

### MAXC2NRM (in)

MAXC2NRM is DOUBLE PRECISION The maximum column 2-norm of the whole original matrix A_orig computed in the main routine DGEQP3RK. MAXC2NRM >= 0.

### A (in,out)

A is DOUBLE PRECISION array, dimension (LDA,N+NRHS) On entry: the M-by-N matrix A and M-by-NRHS matrix B, as in N NRHS array_A = M [ mat_A, mat_B ] On exit: 1. The elements in block A(IOFFSET+1:M,1:K) below the diagonal together with the array TAU represent the orthogonal matrix Q(K) as a product of elementary reflectors. 2. The upper triangular block of the matrix A stored in A(IOFFSET+1:M,1:K) is the triangular factor obtained. 3. The block of the matrix A stored in A(1:IOFFSET,1:N) has been accordingly pivoted, but not factorized. 4. The rest of the array A, block A(IOFFSET+1:M,K+1:N+NRHS). The left part A(IOFFSET+1:M,K+1:N) of this block contains the residual of the matrix A, and, if NRHS > 0, the right part of the block A(IOFFSET+1:M,N+1:N+NRHS) contains the block of the right-hand-side matrix B. Both these blocks have been updated by multiplication from the left by Q(K)**T.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### K (out)

K is INTEGER Factorization rank of the matrix A, i.e. the rank of the factor R, which is the same as the number of non-zero rows of the factor R. 0 <= K <= min(M-IOFFSET,KMAX,N). K also represents the number of non-zero Householder vectors.

### MAXC2NRMK (out)

MAXC2NRMK is DOUBLE PRECISION The maximum column 2-norm of the residual matrix, when the factorization stopped at rank K. MAXC2NRMK >= 0.

### RELMAXC2NRMK (out)

RELMAXC2NRMK is DOUBLE PRECISION The ratio MAXC2NRMK / MAXC2NRM of the maximum column 2-norm of the residual matrix (when the factorization stopped at rank K) to the maximum column 2-norm of the whole original matrix A. RELMAXC2NRMK >= 0.

### JPIV (out)

JPIV is INTEGER array, dimension (N) Column pivot indices, for 1 <= j <= N, column j of the matrix A was interchanged with column JPIV(j).

### TAU (out)

TAU is DOUBLE PRECISION array, dimension (min(M-IOFFSET,N)) The scalar factors of the elementary reflectors.

### VN1 (in,out)

VN1 is DOUBLE PRECISION array, dimension (N) The vector with the partial column norms.

### VN2 (in,out)

VN2 is DOUBLE PRECISION array, dimension (N) The vector with the exact column norms.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (N-1) Used in DLARF1F subroutine to apply an elementary reflector from the left.

### INFO (out)

INFO is INTEGER 1) INFO = 0: successful exit. 2) If INFO = j_1, where 1 <= j_1 <= N, then NaN was detected and the routine stops the computation. The j_1-th column of the matrix A or the j_1-th element of array TAU contains the first occurrence of NaN in the factorization step K+1 ( when K columns have been factorized ). On exit: K is set to the number of factorized columns without exception. MAXC2NRMK is set to NaN. RELMAXC2NRMK is set to NaN. TAU(K+1:min(M,N)) is not set and contains undefined elements. If j_1=K+1, TAU(K+1) may contain NaN. 3) If INFO = j_2, where N+1 <= j_2 <= 2*N, then no NaN was detected, but +Inf (or -Inf) was detected and the routine continues the computation until completion. The (j_2-N)-th column of the matrix A contains the first occurrence of +Inf (or -Inf) in the factorization step K+1 ( when K columns have been factorized ).

