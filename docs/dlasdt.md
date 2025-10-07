# DLASDT

## Function Signature

```fortran
DLASDT(N, LVL, ND, INODE, NDIML, NDIMR, MSUB)
```

## Description


 DLASDT creates a tree of subproblems for bidiagonal divide and
 conquer.

## Parameters

### N (in)

N is INTEGER On entry, the number of diagonal elements of the bidiagonal matrix.

### LVL (out)

LVL is INTEGER On exit, the number of levels on the computation tree.

### ND (out)

ND is INTEGER On exit, the number of nodes on the tree.

### INODE (out)

INODE is INTEGER array, dimension ( N ) On exit, centers of subproblems.

### NDIML (out)

NDIML is INTEGER array, dimension ( N ) On exit, row dimensions of left children.

### NDIMR (out)

NDIMR is INTEGER array, dimension ( N ) On exit, row dimensions of right children.

### MSUB (in)

MSUB is INTEGER On entry, the maximum row dimension each subproblem at the bottom of the tree can be of.

