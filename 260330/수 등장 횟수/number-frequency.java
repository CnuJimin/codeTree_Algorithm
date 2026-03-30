import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();

        HashMap<Integer, Integer> map = new HashMap<>(); // <해당 수, 등장 횟수>

        st = new StringTokenizer(br.readLine());
        while(N -- > 0){
            int num = Integer.parseInt(st.nextToken());

            if(!map.containsKey(num)){
                map.put(num, 1);
            }else{
                map.put(num, map.get(num) + 1);
            }
        }

        st = new StringTokenizer(br.readLine());

        while(M -- > 0){
            int num = Integer.parseInt(st.nextToken());

            if(map.containsKey(num)){
                sb.append(map.get(num)).append(" ");
            }else{
                sb.append(0).append(" ");
            }
        }

        System.out.println(sb);


    }
}