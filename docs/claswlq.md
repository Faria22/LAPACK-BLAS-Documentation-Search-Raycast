# CLASWLQ

## Function Signature

```fortran
CLASWLQ(M, N, MB, NB, A, LDA, T, LDT, WORK,
*                            LWORK, INFO)
```

## Description


 CLASWLQ computes a blocked Tall-Skinny LQ factorization of
 a complex M-by-N matrix A for M <= N:

    A = ( L 0 ) *  Q,

 where:

    Q is a n-by-N orthogonal matrix, stored on exit in an implicit
    form in the elements above the diagonal of the array A and in
    the elements of the array T;
    L is a lower-triangular M-by-M matrix stored on exit in
    the elements on and below the diagonal of the array A.
    0 is a M-by-(N-M) zero matrix, if M < N, and is not stored.


## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= M >= 0.

### MB (in)

MB is INTEGER The row block size to be used in the blocked QR. M >= MB >= 1

### NB (in)

NB is INTEGER The column block size to be used in the blocked QR. NB > 0.

### A (in,out)

A is COMPLEX array, dimension (LDA,N) On entry, the M-by-N matrix A. On exit, the elements on and below the diagonal of the array contain the N-by-N lower triangular matrix L; the elements above the diagonal represent Q by the rows of blocked V (see Further Details).

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### T (out)

T is COMPLEX array, dimension (LDT, N * Number_of_row_blocks) where Number_of_row_blocks = CEIL((N-M)/(NB-M)) The blocked upper triangular block reflectors stored in compact form as a sequence of upper triangular blocks. See Further Details below.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= MB.

### WORK (out)

(workspace) COMPLEX array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the minimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= 1, if MIN(M,N) = 0, and LWORK >= MB*M, otherwise. If LWORK = -1, then a workspace query is assumed; the routine only calculates the minimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

