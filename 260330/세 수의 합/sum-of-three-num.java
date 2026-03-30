import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static long K;
    static long[] nums;
    static int[] selected;
    static HashMap<Long, List<int[]>> map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Long.parseLong(st.nextToken());

        st = new StringTokenizer(br.readLine());

        nums = new long[N];
        selected = new int[2];

        for (int i = 0; i < N; i++) {
            nums[i] = Long.parseLong(st.nextToken());
        }

        comb(0, 0);

        long cnt = 0;
        for (int i = 0; i < N; i++) {
            long findNum = K - nums[i];

            if (map.containsKey(findNum)) {
                for (int[] arr : map.get(findNum)) {
                    if (arr[0] != i && arr[1] != i) {
                        cnt++;
                    }
                }
            }
        }

        System.out.println(cnt / 3);
    }

    static void comb(int idx, int cnt) {
        if (cnt == 2) {
            long sum = nums[selected[0]] + nums[selected[1]];

            map.putIfAbsent(sum, new ArrayList<>());
            map.get(sum).add(new int[]{selected[0], selected[1]});
            return;
        }

        for (int i = idx; i < N; i++) {
            selected[cnt] = i;
            comb(i + 1, cnt + 1);
        }
    }
}