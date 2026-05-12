import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int numA = Integer.parseInt(st.nextToken());
        int numB = Integer.parseInt(st.nextToken());

        HashSet<Integer> originA = new HashSet<>();
        HashSet<Integer> originB = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < numA ; i ++){
            originA.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < numB ; i ++){
            originB.add(Integer.parseInt(st.nextToken()));
        }

        int ans = 0 ;

        for(int a : originA){
            if(!originB.contains(a)) ans ++;
        }

        for(int b : originB){
            if(!originA.contains(b)) ans ++;
        }

        System.out.println(ans);


    }
}