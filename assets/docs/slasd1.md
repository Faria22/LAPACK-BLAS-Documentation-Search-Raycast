```fortran  
subroutine slasd1 (  
nl,  
nr,  
sqre,  
d,  
alpha,  
beta,  
u,  
ldu,  
vt,  
ldvt,  
*                          idxq,  
iwork,  
work,  
info  
)  
```  
  
SLASD1 computes the SVD of an upper bidiagonal N-by-M matrix B,  
where N = NL + NR + 1 and M = N + SQRE. SLASD1 is called from SLASD0.  
  
A related subroutine SLASD7 handles the case in which the singular  
values (and the singular vectors in factored form) are desired.  
  
SLASD1 computes the SVD as follows:  
  
( D1(in)    0    0       0 )  
B = U(in) * (   Z1**T   a   Z2**T    b ) * VT(in)  
(   0       0   D2(in)   0 )  
  
= U(out) * ( D(out) 0) * VT(out)  
  
where Z**T = (Z1**T a Z2**T b) = u**T VT**T, and u is a vector of dimension M  
with ALPHA and BETA in the NL+1 and NL+2 th entries and zeros  
elsewhere; and the entry b is empty if SQRE = 0.  
  
The left singular vectors of the original matrix are stored in U, and  
the transpose of the right singular vectors are stored in VT, and the  
singular values are in D.  The algorithm consists of three stages:  
  
The first stage consists of deflating the size of the problem  
when there are multiple singular values or when there are zeros in  
the Z vector.  For each such occurrence the dimension of the  
secular equation problem is reduced by one.  This stage is  
performed by the routine SLASD2.  
  
The second stage consists of calculating the updated  
singular values. This is done by finding the square roots of the  
roots of the secular equation via the routine SLASD4 (as called  
by SLASD3). This routine also calculates the singular vectors of  
the current problem.  
  
The final stage consists of computing the updated singular vectors  
directly using the updated singular values.  The singular vectors  
for the current problem are multiplied with the singular vectors  
from the overall problem.  
  
## Parameters  
Nl : Integer [in]  
> The row dimension of the upper block.  NL >= 1.  
  
Nr : Integer [in]  
> The row dimension of the lower block.  NR >= 1.  
  
Sqre : Integer [in]  
> = 0: the lower block is an NR-by-NR square matrix.  
> = 1: the lower block is an NR-by-(NR+1) rectangular matrix.  
> The bidiagonal matrix has row dimension N = NL + NR + 1,  
> and column dimension M = N + SQRE.  
  
D : Real Array, Dimension (nl+nr+1). [in,out]  
> N = NL+NR+1  
> On entry D(1:NL,1:NL) contains the singular values of the  
> upper block; and D(NL+2:N) contains the singular values of  
> the lower block. On exit D(1:N) contains the singular values  
> of the modified matrix.  
  
Alpha : Real [in,out]  
> Contains the diagonal element associated with the added row.  
  
Beta : Real [in,out]  
> Contains the off-diagonal element associated with the added  
> row.  
  
U : Real Array, Dimension (ldu,n) [in,out]  
> On entry U(1:NL, 1:NL) contains the left singular vectors of  
> the upper block; U(NL+2:N, NL+2:N) contains the left singular  
> vectors of the lower block. On exit U contains the left  
> singular vectors of the bidiagonal matrix.  
  
Ldu : Integer [in]  
> The leading dimension of the array U.  LDU >= max( 1, N ).  
  
Vt : Real Array, Dimension (ldvt,m) [in,out]  
> where M = N + SQRE.  
> the right singular vectors of the lower block. On exit  
> bidiagonal matrix.  
  
Ldvt : Integer [in]  
> The leading dimension of the array VT.  LDVT >= max( 1, M ).  
  
Idxq : Integer Array, Dimension (n) [in,out]  
> This contains the permutation which will reintegrate the  
> subproblem just solved back into sorted order, i.e.  
> D( IDXQ( I = 1, N ) ) will be in ascending order.  
  
Iwork : Integer Array, Dimension (4*n) [out]  
  
Work : Real Array, Dimension (3*m**2+2*m) [out]  
  
Info : Integer [out]  
> = 0:  successful exit.  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
> > 0:  if INFO = 1, a singular value did not converge  
  
