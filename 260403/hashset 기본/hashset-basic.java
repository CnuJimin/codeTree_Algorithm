import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        HashSet<Integer> hs = new HashSet<>();

        while(N -- > 0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            if(command.equals("add")) hs.add(Integer.parseInt(st.nextToken()));
            else if(command.equals("remove")) hs.remove(Integer.parseInt(st.nextToken()));
            else{
                int num = Integer.parseInt(st.nextToken());
                if(hs.contains(num))System.out.println("true");
                else System.out.println("false");
            }
        }
    }
}