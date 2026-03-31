import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] word = br.readLine().toCharArray();

        HashMap<Character, Integer> map = new HashMap<>();

        for (int i = 0 ; i < word.length; i ++){
            if(map.containsKey(word[i])) map.put(word[i], map.get(word[i]) + 1);
            else map.put(word[i], 1);
        }

        String ans = "None";

        for (int i = 0 ; i < word.length ; i ++){
            if(map.get(word[i]) == 1){
                ans = "" + word[i];
                break;
            }
        }

        System.out.println(ans);
    }
}