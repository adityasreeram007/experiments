class balance{
    static int stack[]=new int[100];
    static int top=-1;
    static int[] except=new int[10];
    static int head=0;
    public static void main(String args[])
    {
        String pattern="(ab())))";
        int m=pattern.length();
        for(int i=0;i<m;i++)
        {
            if(pattern.charAt(i)=='(')
            {
                push(i);
            }
            else if(pattern.charAt(i)==')')
            {
                if(top==-1)
                {
                    except[head]=i;
                    head+=1;
                    
                }
                else if(pattern.charAt(stack[top])=='(')
                {
                    pop();
                }
                else{
                    except[head]=stack[top];
                    head+=1;
                    pop();
                    
                    
                }
            }
        }
       
        while(top>-1)
        {
            except[head]=stack[top];
            head+=1;
            System.out.println(stack[top]);
            top-=1;
        }
        for (int j=0;j<head;j++)
        {
            System.out.println("head "+except[j]);
        }
        
        for(int i=0;i<head;i++)
        {
            pattern.charAt(i);
        }
        System.out.println(pattern);

    }
    static void  push(int charr)
    {
        if(top==-1)
        {
            top=0;
        }
        else{
            top+=1;
        }
        stack[top]=charr;
        System.out.println(stack[top]);
        return;
    }
    static void pop()
    {
        if(top!=-1)
        {
            System.out.println(stack[top]);
            
            top-=1;
        }
        return;
    }

}