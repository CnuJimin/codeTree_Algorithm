import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        while(T -- > 0){
            int n = Integer.parseInt(br.readLine());
            TreeSet<Integer> ts = new TreeSet<>();

            for(int i = 0 ; i < n ; i ++){
                st = new StringTokenizer(br.readLine());
                String command = st.nextToken();
                int num = Integer.parseInt(st.nextToken());
                if(command.equals("I")){
                    ts.add(num);
                }else if (command.equals("D")){
                    if(ts.isEmpty()) continue;
                    if(num == 1){
                        ts.remove(ts.last());
                    }else{
                        ts.remove(ts.first());
                    }
                }
            }

            if(ts.isEmpty()){
                System.out.println("EMPTY");
            }else{
                System.out.println(ts.last() + " " + ts.first());
            }

        }
    }
}