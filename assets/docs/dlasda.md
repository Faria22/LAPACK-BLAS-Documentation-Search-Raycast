```fortran  
subroutine dlasda (  
icompq,  
smlsiz,  
n,  
sqre,  
d,  
e,  
u,  
ldu,  
vt,  
k,  
*                          difl,  
difr,  
z,  
poles,  
givptr,  
givcol,  
ldgcol,  
*                          perm,  
givnum,  
c,  
s,  
work,  
iwork,  
info  
)  
```  
  
Using a divide and conquer approach, DLASDA computes the singular  
value decomposition (SVD) of a real upper bidiagonal N-by-M matrix  
B with diagonal D and offdiagonal E, where M = N + SQRE. The  
algorithm computes the singular values in the SVD B = U * S * VT.  
The orthogonal matrices U and VT are optionally computed in  
compact form.  
  
A related subroutine, DLASD0, computes the singular values and  
the singular vectors in explicit form.  
  
## Parameters  
Icompq : Integer [in]  
> Specifies whether singular vectors are to be computed  
> in compact form, as follows  
> = 0: Compute singular values only.  
> = 1: Compute singular vectors of upper bidiagonal  
> matrix in compact form.  
  
Smlsiz : Integer [in]  
> The maximum size of the subproblems at the bottom of the  
> computation tree.  
  
N : Integer [in]  
> The row dimension of the upper bidiagonal matrix. This is  
> also the dimension of the main diagonal array D.  
  
Sqre : Integer [in]  
> Specifies the column dimension of the bidiagonal matrix.  
> = 0: The bidiagonal matrix has column dimension M = N;  
> = 1: The bidiagonal matrix has column dimension M = N + 1.  
  
D : Double Precision Array, Dimension ( N ) [in,out]  
> On entry D contains the main diagonal of the bidiagonal  
> matrix. On exit D, if INFO = 0, contains its singular values.  
  
E : Double Precision Array, Dimension ( M-1 ) [in]  
> Contains the subdiagonal entries of the bidiagonal matrix.  
> On exit, E has been destroyed.  
  
U : Double Precision Array, [out]  
> dimension ( LDU, SMLSIZ ) if ICOMPQ = 1, and not referenced  
> if ICOMPQ = 0. If ICOMPQ = 1, on exit, U contains the left  
> singular vector matrices of all subproblems at the bottom  
> level.  
  
Ldu : Integer, Ldu = > N. [in]  
> The leading dimension of arrays U, VT, DIFL, DIFR, POLES,  
> GIVNUM, and Z.  
  
Vt : Double Precision Array, [out]  
> dimension ( LDU, SMLSIZ+1 ) if ICOMPQ = 1, and not referenced  
> singular vector matrices of all subproblems at the bottom  
> level.  
  
K : Integer Array, [out]  
> dimension ( N ) if ICOMPQ = 1 and dimension 1 if ICOMPQ = 0.  
> If ICOMPQ = 1, on exit, K(I) is the dimension of the I-th  
> secular equation on the computation tree.  
  
Difl : Double Precision Array, Dimension ( Ldu, Nlvl ), [out]  
> where NLVL = floor(log_2 (N/SMLSIZ))).  
  
Difr : Double Precision Array, [out]  
> dimension ( N ) if ICOMPQ = 0.  
> record distances between singular values on the I-th  
> level and singular values on the (I -1)-th level, and  
> the right singular vector matrix. See DLASD8 for details.  
  
Z : Double Precision Array, [out]  
> dimension ( LDU, NLVL ) if ICOMPQ = 1 and  
> dimension ( N ) if ICOMPQ = 0.  
> The first K elements of Z(1, I) contain the components of  
> the deflation-adjusted updating row vector for subproblems  
> on the I-th level.  
  
Poles : Double Precision Array, [out]  
> involved in the secular equations on the I-th level.  
  
Givptr : Integer Array, [out]  
> dimension ( N ) if ICOMPQ = 1, and not referenced if  
> ICOMPQ = 0. If ICOMPQ = 1, on exit, GIVPTR( I ) records  
> the number of Givens rotations performed on the I-th  
> problem on the computation tree.  
  
Givcol : Integer Array, [out]  
> referenced if ICOMPQ = 0. If ICOMPQ = 1, on exit, for each I,  
> of Givens rotations performed on the I-th level on the  
> computation tree.  
  
Ldgcol : Integer, Ldgcol = > N. [in]  
> The leading dimension of arrays GIVCOL and PERM.  
  
Perm : Integer Array, [out]  
> dimension ( LDGCOL, NLVL ) if ICOMPQ = 1, and not referenced  
> if ICOMPQ = 0. If ICOMPQ = 1, on exit, PERM(1, I) records  
> permutations done on the I-th level of the computation tree.  
  
Givnum : Double Precision Array, [out]  
> referenced if ICOMPQ = 0. If ICOMPQ = 1, on exit, for each I,  
> values of Givens rotations performed on the I-th level on  
> the computation tree.  
  
C : Double Precision Array, [out]  
> dimension ( N ) if ICOMPQ = 1, and dimension 1 if ICOMPQ = 0.  
> If ICOMPQ = 1 and the I-th subproblem is not square, on exit,  
> C( I ) contains the C-value of a Givens rotation related to  
> the right null space of the I-th subproblem.  
  
S : Double Precision Array, Dimension ( N ) If [out]  
> ICOMPQ = 1, and dimension 1 if ICOMPQ = 0. If ICOMPQ = 1  
> and the I-th subproblem is not square, on exit, S( I )  
> contains the S-value of a Givens rotation related to  
> the right null space of the I-th subproblem.  
  
Work : Double Precision Array, Dimension [out]  
  
Iwork : Integer Array, Dimension (7*n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit.  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
> > 0:  if INFO = 1, a singular value did not converge  
  
