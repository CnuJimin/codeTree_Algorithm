import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] cnt = new int[N];

        HashMap<Character, Integer>[] mapArr = new HashMap[N];

        // for (int i = 0 ; i < N ; i ++){
        //     mapArr[i] = new HashMap<>();
        // }

        int mapCnt = 0;

        for (int i = 0 ; i < N ; i ++){
            char[] word = br.readLine().toCharArray();
            HashMap<Character, Integer> temp = new HashMap<>();
            for (int j = 0 ; j < word.length ; j ++){
                if(temp.containsKey(word[j])) temp.put(word[j], temp.get(word[j]) + 1);
                else temp.put(word[j], 1); 
            }

            boolean isNew = true;
            for (int j = 0 ; j < mapCnt ; j ++){
                boolean flag = true;
                HashMap<Character, Integer> compareMap = mapArr[j];

                for(char key : temp.keySet()){
                    if (temp.size() != compareMap.size()) {
                        flag = false;
                        break;
                    }
                    if(!compareMap.containsKey(key)) {
                        flag = false;
                        break;
                    }
                    if(temp.get(key) != compareMap.get(key)) {
                        flag = false;
                        break;
                    }
                }

                if(flag){
                    isNew = false;
                    cnt[j] ++;
                }
            }

            if(isNew){
                mapArr[mapCnt] = temp;
                cnt[mapCnt] = 1;
                mapCnt++;
            }
        }

        int ans = 0;

        for (int i = 0 ; i < mapCnt ; i ++){
            ans = Math.max(ans, cnt[i]);
        }

        System.out.println(ans);



    }
}