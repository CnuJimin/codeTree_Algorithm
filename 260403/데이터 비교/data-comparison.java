import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        HashSet<Integer> set1= new HashSet<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < N ; i ++){
            set1.add(Integer.parseInt(st.nextToken()));
        }


        N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        int[] arr = new int[N];

        for (int i = 0 ; i < N ; i ++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        StringBuilder sb = new StringBuilder();
        for(int i : arr){
            if(set1.contains(i)) sb.append(1).append(" ");
            else sb.append(0).append(" ");
        }

        System.out.println(sb);



    }
}