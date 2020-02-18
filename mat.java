import java.util.regex.*;
import java.util.*;
class mat{
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args)
    {
        String inp=sc.next();
        Pattern p=Pattern.compile("([(]*[a-z][+*-/][a-z+-/*]*[a-z][)]*)*");
        Matcher m=p.matcher(inp);
        System.out.println(m.matches());
        if(m.matches())
        {
            System.out.println(inp+" valid");
        }
        else{
            System.out.println("NOt valid");
        }
        
    }
}