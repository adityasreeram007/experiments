import java.util.*;
class oddevensort{
    public static void main(String[] args)
    {
        int input[]={13,2, 4,15,12,10,5};
        ArrayList <Integer> odd=new ArrayList<Integer>();
        ArrayList <Integer> even=new ArrayList<Integer>();
     
        
        int i=0;
        
        while(i<input.length)
        {
            odd.add(input[i]);
            if(i+1<input.length){
            even.add(input[i+1]);}
            //System.out.println(i);
            
            i+=2;
        }Collections.sort(even);
        Collections.sort(odd,Collections.reverseOrder());
        System.out.println(odd);
        System.out.println(even);
        ArrayList<Integer> newer=new ArrayList<Integer>();
        Iterator e=odd.iterator();
        Iterator f=even.iterator();
        while(true)
        {
            if(e.hasNext() || f.hasNext())
            {
                if(e.hasNext()){
                newer.add((Integer)e.next());}
                if(f.hasNext()){
                    newer.add((Integer)f.next());
                }
            }
            
            else{
                break;
            }
        }
        System.out.println(newer);
    }
    
}