import java.io.*;
import java.util.*;

public class Main {

    static int[][] nums;
    static int N;
    static long ans;
    static HashMap<Integer, Integer> map1 = new HashMap<>();
    static HashMap<Integer, Integer> map2 = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        nums = new int[4][N];

        for (int i = 0; i < 4; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                nums[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        makeSum(0, 1, map1);
        makeSum(2, 3, map2);

        ans = 0;
        for (int key : map1.keySet()) {
            if (map2.containsKey(-key)) {
                ans += (long) map1.get(key) * map2.get(-key);
            }
        }

        System.out.println(ans);
    }

    public static void makeSum(int idx1, int idx2, HashMap<Integer, Integer> map) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int sum = nums[idx1][i] + nums[idx2][j];
                map.put(sum, map.getOrDefault(sum, 0) + 1);
            }
        }
    }
}