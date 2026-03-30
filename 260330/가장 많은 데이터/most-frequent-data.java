import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int max = -1;

        HashMap<String, Integer> map = new HashMap<>();
        while (N -- > 0){
            String word = br.readLine();

            if(map.containsKey(word)){
                map.put(word, map.get(word) + 1);
                max = Math.max(max, map.get(word));
            }else{
                map.put(word, 1);
                max = Math.max(max, map.get(word));

            }
            
        }

        System.out.println(max);

    }
}