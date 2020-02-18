#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *left;
    struct node *right;
};
struct node *root = NULL;
struct node* newnode(int x)
{
    struct node* temp=(struct node*)malloc(sizeof(struct node));
    temp->data=x;
    temp->left=NULL;
    temp->right=NULL;
    return temp;
}

struct node *insert(struct node *root, struct node *x)
{
    if(root==NULL)
    {
        root=x;
        
    }
    else if(root->data>x->data)
    {
        root->left=insert(root->left,x);
    }
    else{
        root->right=insert(root->right,x);
    }
    return root;
}
void inorder(struct node* root)
{
    if(root!=NULL){
    inorder(root->left);
    printf("%d\t",root->data);
    inorder(root->right);
    }
    
  return;
}
int main()
{
    int size;
    printf("enter size of the array u nibba:");
    scanf("%d", &size);
    int arr[20];
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &arr[i]);
    }
    for (int i=0;i<size;i++)
    {
        struct node* x=newnode(arr[i]);
        if(root==NULL)
        {
            root=x;
        }
        else{
            root=insert(root,x);
        }
    }
    inorder(root);
    printf("\n");
    return 0;
}