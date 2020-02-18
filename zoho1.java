class zoho1
{
    
    static void repeat(String s,int start, int end)
    {
        if(start+1==end)
        {
            return;
        }
        System.out.print(s.charAt(end));
        repeat(s,start,end+1);

    }
    public static void main(String[] args)
    {
        String inp="Incredible hulk at his best";
        int c=inp.length();
        int start=c-1;
        int end=0;
        for (int i=c-1;i>0;i--)
        {
            if(inp.charAt(i)==' ')
            {
                end=i;
                repeat(inp,start,end);
                start=end;
            }
        }
        //System.out.print(" ");
        //System.out.print(" ");
        repeat(inp,start,0);
    }
}