class node{
    int data;
    node left,right;
    node(int a )
    {
        this.data=a;
        this.right=null;
        this.left=null;
    }

}

class bst{
    static node root=null;
    public static void main(String[] args)
    {
        int arr[]={4,2,5,12,7};
        for (int x:arr)
        {
            if(root==null)
            {
                root=new node(x);
            }
            else{
                node temp=new node(x);
                root=insert(root,temp);
            }
        }
        inorder(root);
    }

    static void inorder(node root)
    {
        if(root==null)
        {
            return;
        }
        inorder(root.left);
        System.out.print(root.data+"\t");
        inorder(root.right);
    }
    static node insert(node root,node temp)
    {
        if(root==null)
        {
            root=temp;
        }
        else if(root.data>temp.data)
        {
            root.left=insert(root.left,temp);
        }
        else 
        {
            root.right=insert(root.right,temp);
        }
        return root;

    }


}