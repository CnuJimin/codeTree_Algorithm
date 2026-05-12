import java.io.*;
import java.util.*;

public class Main {

    static int N, G; 
    static int[] remain;
    static ArrayList<Integer>[] numsList;
    static HashSet<Integer> [] groups;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        G = Integer.parseInt(st.nextToken());
        numsList = new ArrayList[N + 1];
        groups = new HashSet[N + 1];
        for(int i = 0 ; i < N + 1 ; i ++){
            numsList[i] = new ArrayList<>();
            groups[i] = new HashSet<>();
        }

        remain = new int[G];

        for(int i = 0 ; i < G ; i ++){
            st = new StringTokenizer(br.readLine());
            int cnt = Integer.parseInt(st.nextToken());
            remain[i] = cnt;

            for(int j = 0 ; j < cnt ; j ++){
                int num = Integer.parseInt(st.nextToken());
                groups[i].add(num);
                numsList[num].add(i);
            }
        }

        HashSet<Integer> invited = new HashSet<>();
        invited.add(1);

        ArrayDeque<Integer> remainOnes = new ArrayDeque<>();

        for(int idx : numsList[1]) {
            
            groups[idx].remove(1);
            if(groups[idx].size() == 1){
                remainOnes.add(idx);
            }
        }

        while(true){
            // System.out.println(Arrays.toString(invited.toArray()));
            if(remainOnes.isEmpty()) break;

            int idx = remainOnes.poll(); // 하나 남은 그룹의 idx
            // 그 그룹가서 하나 남은게 뭔지 확인하고 초대장 주기 
            int val = -1;
            for(int v : groups[idx]){
                val = v;
            }

            if(val == -1){
                continue;
            }

            invited.add(val);

            for(int i : numsList[val]){ // 초대장 받은 사람이 포함된 그룹에 가서 받은거 체크해주기 
                groups[i].remove(val);
                remain[i] -- ;
                if(groups[i].size() == 1){
                    remainOnes.add(i);
                }
            }
            
        }

        System.out.println(invited.size());

    }
}