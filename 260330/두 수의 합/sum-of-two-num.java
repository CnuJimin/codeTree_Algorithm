import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        long K = Long.parseLong(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int cnt = 0;

        HashMap<Long, Integer> map = new HashMap<>();

        while(N -- > 0){
            long num = Long.parseLong(st.nextToken());

            long findNum = K - num;

            if(map.containsKey(findNum)){
                cnt += map.get(findNum);
            }


            if(map.containsKey(num)){
                map.put(num, map.get(num) + 1);
            }else{
                map.put(num, 1);
            }


            
        }

        System.out.println(cnt);
    }
}