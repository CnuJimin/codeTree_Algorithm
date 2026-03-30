import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<String, String> stringMap = new HashMap<>();

        for(int i = 1 ; i <= N ; i ++){
            String word = br.readLine();
            stringMap.put(word, String.valueOf(i));
            stringMap.put(String.valueOf(i), word);
        }

        StringBuilder sb = new StringBuilder();

        while(M -- > 0){
            sb.append(stringMap.get(br.readLine())).append("\n");
        }

        System.out.println(sb);

    }
}