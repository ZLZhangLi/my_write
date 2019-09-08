import java.util.*;
import java.io.*;
import java.lang.reflect.Array;
public class Main {
    
    public static void main(String[] args) throws Exception{
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        int[] num = new int[n*m];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                num[i * m +j] = (i+1)*(j+1);
            }
        }
        Arrays.sort(num);
        System.out.println(num[n*m - k]);
    }
    }