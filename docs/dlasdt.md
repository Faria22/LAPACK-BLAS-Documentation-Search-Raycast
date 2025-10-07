```fortran
subroutine dlasdt	(	integer	n,
		integer	lvl,
		integer	nd,
		integer, dimension(*)	inode,
		integer, dimension(*)	ndiml,
		integer, dimension(*)	ndimr,
		integer	msub )
```

 DLASDT creates a tree of subproblems for bidiagonal divide and
 conquer.

## Parameters
N : Integer [in]
> On entry, the number of diagonal elements of the
> bidiagonal matrix.

Lvl : Integer [out]
> On exit, the number of levels on the computation tree.

Nd : Integer [out]
> On exit, the number of nodes on the tree.

Inode : Integer Array, Dimension ( N ) [out]
> On exit, centers of subproblems.

Ndiml : Integer Array, Dimension ( N ) [out]
> On exit, row dimensions of left children.

Ndimr : Integer Array, Dimension ( N ) [out]
> On exit, row dimensions of right children.

Msub : Integer [in]
> On entry, the maximum row dimension each subproblem at the
> bottom of the tree can be of.

