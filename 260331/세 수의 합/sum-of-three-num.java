import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < N ; i ++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        HashMap<Integer, Integer> freq = new HashMap<>(); // <원소, 등장한 횟수>

        for(int num : arr){
            if(freq.containsKey(num)){
                freq.put(num, freq.get(num) + 1);
            }else{
                freq.put(num, 1);
            }
        }

        int ans = 0 ;
        for (int i = 0 ; i < N ; i ++){
            if(freq.containsKey(arr[i])){
                freq.put(arr[i], freq.get(arr[i]) - 1);
            }

            for (int j = 0 ; j < i ; j ++){
                if(freq.containsKey(K - arr[i] - arr[j])){
                    ans += freq.get(K - arr[i] - arr[j]);
                }
            }
        }

        System.out.println(ans);

    }
}