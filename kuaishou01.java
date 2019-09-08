import java.util.*;
import java.io.*;
import java.lang.reflect.Array;

public class Main {
 public static void main(String[] args) {
  Scanner in = new Scanner(System.in);
  int k = in.nextInt();
  int n = in.nextInt();
  String[] str = new String[n];
  String[] res = new String[n+1];
  Queue<String> queue = new LinkedList<>();
  for(int i = 0; i< n;i++){
    str[i] = in.next();
    if(str[i].charAt(0) == 'P'){
     queue.add(str[i]);
    }
  }
  int j =0,index = 0;
  boolean flag = true;
  for(int i = 0; i< n;i++){
   if(str[i].charAt(0) == 'P' && flag == true){
    flag = false;   
    res[j++] = queue.poll();
    index = i;
    break;
   } else{
    res[j++] = str[i];
   }
  }  
  for(int i = index+1; i < n;i++){
   if(str[i].charAt(0) == 'P'){
    if(res[j-1].charAt(0) !='P' && res[j-2].charAt(0)!='P')
       res[j++]=queue.poll();
    
   } else if (str[i].charAt(0) == 'V'){
    res[j++] = str[i];
    if(res[j-1].charAt(0) =='V' && res[j-2].charAt(0)=='V')
       res[j++]=queue.poll();
    
   }
  }
  int s = 0;
  for (int i = 0; i < res.length; i++) {
   if(res[i] == null)
    continue;
   else s++;
  }
  System.out.println(s);
  for (int i = 0; i < s; i++) {
   System.out.println(res[i]);
  }
  
 }
}