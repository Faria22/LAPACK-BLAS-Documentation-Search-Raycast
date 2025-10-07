# CLAQP3RK

## Function Signature

```fortran
CLAQP3RK(M, N, NRHS, IOFFSET, NB, ABSTOL,
*     $                     RELTOL, KP1, MAXC2NRM, A, LDA, DONE, KB,
*     $                     MAXC2NRMK, RELMAXC2NRMK, JPIV, TAU,
*     $                     VN1, VN2, AUXV, F, LDF, IWORK, INFO)
```

## Description


 CLAQP3RK computes a step of truncated QR factorization with column
 pivoting of a complex M-by-N matrix A block A(IOFFSET+1:M,1:N)
 by using Level 3 BLAS as

   A * P(KB) = Q(KB) * R(KB).

 The routine tries to factorize NB columns from A starting from
 the row IOFFSET+1 and updates the residual matrix with BLAS 3
 xGEMM. The number of actually factorized columns is returned
 is smaller than NB.

 Block A(1:IOFFSET,1:N) is accordingly pivoted, but not factorized.

 The routine also overwrites the right-hand-sides B matrix stored
 in A(IOFFSET+1:M,1:N+1:N+NRHS) with Q(KB)**H * B.

 Cases when the number of factorized columns KB < NB:

 (1) In some cases, due to catastrophic cancellations, it cannot
 factorize all NB columns and need to update the residual matrix.
 Hence, the actual number of factorized columns in the block returned
 in KB is smaller than NB. The logical DONE is returned as FALSE.
 The factorization of the whole original matrix A_orig must proceed
 with the next block.

 (2) Whenever the stopping criterion ABSTOL or RELTOL is satisfied,
 the factorization of the whole original matrix A_orig is stopped,
 the logical DONE is returned as TRUE. The number of factorized
 columns which is smaller than NB is returned in KB.

 (3) In case both stopping criteria ABSTOL or RELTOL are not used,
 and when the residual matrix is a zero matrix in some factorization
 step KB, the factorization of the whole original matrix A_orig is
 stopped, the logical DONE is returned as TRUE. The number of
 factorized columns which is smaller than NB is returned in KB.

 (4) Whenever NaN is detected in the matrix A or in the array TAU,
 the factorization of the whole original matrix A_orig is stopped,
 the logical DONE is returned as TRUE. The number of factorized
 columns which is smaller than NB is returned in KB. The INFO
 parameter is set to the column index of the first NaN occurrence.


## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrix B. NRHS >= 0.

### IOFFSET (in)

IOFFSET is INTEGER The number of rows of the matrix A that must be pivoted but not factorized. IOFFSET >= 0. IOFFSET also represents the number of columns of the whole original matrix A_orig that have been factorized in the previous steps.

### NB (in)

NB is INTEGER Factorization block size, i.e the number of columns to factorize in the matrix A. 0 <= NB If NB = 0, then the routine exits immediately. This means that the factorization is not performed, the matrices A and B and the arrays TAU, IPIV are not modified.

### ABSTOL (in)

ABSTOL is REAL, cannot be NaN. The absolute tolerance (stopping threshold) for maximum column 2-norm of the residual matrix. The algorithm converges (stops the factorization) when the maximum column 2-norm of the residual matrix is less than or equal to ABSTOL. a) If ABSTOL < 0.0, then this stopping criterion is not used, the routine factorizes columns depending on NB and RELTOL. This includes the case ABSTOL = -Inf. b) If 0.0 <= ABSTOL then the input value of ABSTOL is used.

### RELTOL (in)

RELTOL is REAL, cannot be NaN. The tolerance (stopping threshold) for the ratio of the maximum column 2-norm of the residual matrix to the maximum column 2-norm of the original matrix A_orig. The algorithm converges (stops the factorization), when this ratio is less than or equal to RELTOL. a) If RELTOL < 0.0, then this stopping criterion is not used, the routine factorizes columns depending on NB and ABSTOL. This includes the case RELTOL = -Inf. d) If 0.0 <= RELTOL then the input value of RELTOL is used.

### KP1 (in)

KP1 is INTEGER The index of the column with the maximum 2-norm in the whole original matrix A_orig determined in the main routine CGEQP3RK. 1 <= KP1 <= N_orig.

### MAXC2NRM (in)

MAXC2NRM is REAL The maximum column 2-norm of the whole original matrix A_orig computed in the main routine CGEQP3RK. MAXC2NRM >= 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N+NRHS) On entry: the M-by-N matrix A and M-by-NRHS matrix B, as in N NRHS array_A = M [ mat_A, mat_B ] On exit: 1. The elements in block A(IOFFSET+1:M,1:KB) below the diagonal together with the array TAU represent the unitary matrix Q(KB) as a product of elementary reflectors. 2. The upper triangular block of the matrix A stored in A(IOFFSET+1:M,1:KB) is the triangular factor obtained. 3. The block of the matrix A stored in A(1:IOFFSET,1:N) has been accordingly pivoted, but not factorized. 4. The rest of the array A, block A(IOFFSET+1:M,KB+1:N+NRHS). The left part A(IOFFSET+1:M,KB+1:N) of this block contains the residual of the matrix A, and, if NRHS > 0, the right part of the block A(IOFFSET+1:M,N+1:N+NRHS) contains the block of the right-hand-side matrix B. Both these blocks have been updated by multiplication from the left by Q(KB)**H.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### DONE (out)

DONE is LOGICAL TRUE: a) if the factorization completed before processing all min(M-IOFFSET,NB,N) columns due to ABSTOL or RELTOL criterion, b) if the factorization completed before processing all min(M-IOFFSET,NB,N) columns due to the residual matrix being a ZERO matrix. c) when NaN was detected in the matrix A or in the array TAU. FALSE: otherwise.

### KB (out)

KB is INTEGER Factorization rank of the matrix A, i.e. the rank of the factor R, which is the same as the number of non-zero rows of the factor R. 0 <= KB <= min(M-IOFFSET,NB,N). KB also represents the number of non-zero Householder vectors.

### MAXC2NRMK (out)

MAXC2NRMK is REAL The maximum column 2-norm of the residual matrix, when the factorization stopped at rank KB. MAXC2NRMK >= 0.

### RELMAXC2NRMK (out)

RELMAXC2NRMK is REAL The ratio MAXC2NRMK / MAXC2NRM of the maximum column 2-norm of the residual matrix (when the factorization stopped at rank KB) to the maximum column 2-norm of the original matrix A_orig. RELMAXC2NRMK >= 0.

### JPIV (out)

JPIV is INTEGER array, dimension (N) Column pivot indices, for 1 <= j <= N, column j of the matrix A was interchanged with column JPIV(j).

### TAU (out)

TAU is COMPLEX array, dimension (min(M-IOFFSET,N)) The scalar factors of the elementary reflectors.

### VN1 (in,out)

VN1 is REAL array, dimension (N) The vector with the partial column norms.

### VN2 (in,out)

VN2 is REAL array, dimension (N) The vector with the exact column norms.

### AUXV (out)

AUXV is COMPLEX array, dimension (NB) Auxiliary vector.

### F (out)

F is COMPLEX array, dimension (LDF,NB) Matrix F**H = L*(Y**H)*A.

### LDF (in)

LDF is INTEGER The leading dimension of the array F. LDF >= max(1,N+NRHS).

### IWORK (out)

IWORK is INTEGER array, dimension (N-1). Is a work array. ( IWORK is used to store indices of "bad" columns for norm downdating in the residual matrix ).

### INFO (out)

INFO is INTEGER 1) INFO = 0: successful exit. 2) If INFO = j_1, where 1 <= j_1 <= N, then NaN was detected and the routine stops the computation. The j_1-th column of the matrix A or the j_1-th element of array TAU contains the first occurrence of NaN in the factorization step KB+1 ( when KB columns have been factorized ). On exit: KB is set to the number of factorized columns without exception. MAXC2NRMK is set to NaN. RELMAXC2NRMK is set to NaN. TAU(KB+1:min(M,N)) is not set and contains undefined elements. If j_1=KB+1, TAU(KB+1) may contain NaN. 3) If INFO = j_2, where N+1 <= j_2 <= 2*N, then no NaN was detected, but +Inf (or -Inf) was detected and the routine continues the computation until completion. The (j_2-N)-th column of the matrix A contains the first occurrence of +Inf (or -Inf) in the actorization step KB+1 ( when KB columns have been factorized ).

