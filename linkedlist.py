#include<stdio.h>

struct Node    #definition of structure
{
    int data ;
    struct node*next ;

};

  #old name     NEW NAME
typedef struct Node NODE;
typedef struct * PNODE ;
typedef struct ** PPNODE ;
