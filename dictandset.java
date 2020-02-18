import java.util.*;
class dictandset{
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args)
    {
    Set<Character> charset=new HashSet<Character>();
    String str1,str2;
    str1=sc.next();
    str2=sc.next();
    String str3=str1+str2;
    for (int i=0;i<str3.length();i++)
    {
        charset.add(str3.charAt(i));
    }
    System.out.println(charset);
    HashMap<Character,Integer> map1=new HashMap<Character,Integer>();
    HashMap<Character,Integer> map2=new HashMap<Character,Integer>();

    for (char temp:charset)
    {
        map1.put(temp,0);
        map2.put(temp,0);
    }
        for (int i=0;i<str1.length();i++)
    {
        int c=map1.get(str1.charAt(i));
        c+=1;
        map1.put(str1.charAt(i),c);

    }
            for (int i=0;i<str2.length();i++)
    {
        int c=map2.get(str2.charAt(i));
        c+=1;
        map2.put(str2.charAt(i),c);

    }
    System.out.println(map1);
    System.out.println(map2);
    
    for(char check:charset)
    {
        if(map1.get(check)!=map2.get(check))
        {
            System.out.println("Not a anagram");
            return;
            
        }
    }
    System.out.println("ANAGRAM");}
}