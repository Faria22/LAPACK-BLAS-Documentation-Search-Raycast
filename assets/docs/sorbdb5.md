```fortran  
subroutine sorbdb5 (  
m1,  
m2,  
n,  
x1,  
incx1,  
x2,  
incx2,  
q1,  
ldq1,  
q2,  
*                           ldq2,  
work,  
lwork,  
info  
)  
```  
  
SORBDB5 orthogonalizes the column vector  
X = [ X1 ]  
[ X2 ]  
with respect to the columns of  
Q = [ Q1 ] .  
[ Q2 ]  
The columns of Q must be orthonormal.  
  
If the projection is zero according to Kahan's "twice is enough"  
criterion, then some other vector from the orthogonal complement  
is returned. This vector is chosen in an arbitrary but deterministic  
way.  
  
  
## Parameters  
M1 : Integer [in]  
> The dimension of X1 and the number of rows in Q1. 0 <= M1.  
  
M2 : Integer [in]  
> The dimension of X2 and the number of rows in Q2. 0 <= M2.  
  
N : Integer [in]  
> The number of columns in Q1 and Q2. 0 <= N.  
  
X1 : Real Array, Dimension (m1) [in,out]  
> On entry, the top part of the vector to be orthogonalized.  
> On exit, the top part of the projected vector.  
  
Incx1 : Integer [in]  
> Increment for entries of X1.  
  
X2 : Real Array, Dimension (m2) [in,out]  
> On entry, the bottom part of the vector to be  
> orthogonalized. On exit, the bottom part of the projected  
> vector.  
  
Incx2 : Integer [in]  
> Increment for entries of X2.  
  
Q1 : Real Array, Dimension (ldq1, N) [in]  
> The top part of the orthonormal basis matrix.  
  
Ldq1 : Integer [in]  
> The leading dimension of Q1. LDQ1 >= M1.  
  
Q2 : Real Array, Dimension (ldq2, N) [in]  
> The bottom part of the orthonormal basis matrix.  
  
Ldq2 : Integer [in]  
> The leading dimension of Q2. LDQ2 >= M2.  
  
Work : Real Array, Dimension (lwork) [out]  
  
Lwork : Integer [in]  
> The dimension of the array WORK. LWORK >= N.  
  
Info : Integer [out]  
> = 0:  successful exit.  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
  
