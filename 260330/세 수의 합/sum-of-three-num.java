import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static long K;
    static long[] nums;
    static int[] selected;
    static HashMap<Long, List<long[]>> map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Long.parseLong(st.nextToken());

        st = new StringTokenizer(br.readLine());

        nums = new long[N];
        selected = new int[2];
        for (int i = 0 ; i < N ; i++){
            nums[i] = Long.parseLong(st.nextToken());
        }

        //2개 골라 
        comb(0, 0);
        int cnt = 0;
        for (int i = 0 ; i < N ; i ++){
            long findNum = K - nums[i];
            if(map.containsKey(findNum)){
                for(long[] arr : map.get(findNum)){
                    if(arr[0] != i && arr[1] != i){
                        cnt ++;
                    }
                }
            }
        }

        System.out.println(cnt);

    }

    static void comb(int idx, int cnt){
        if(cnt == 2){
            // System.out.println(Arrays.toString(selected));
            long sum = 0 ;
            for (long i : selected){
                sum += i;
            }
            map.put(sum, new ArrayList<>());
            map.get(sum).add(new long[]{selected[0], selected[1]});
            return;
        }

        for (int i = idx ; i < N ; i ++){
            selected[cnt] = i;
            comb(i + 1, cnt + 1);
        }
    }
}