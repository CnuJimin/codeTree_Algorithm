import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        TreeSet<Integer> ts = new TreeSet<>();
        TreeSet<Integer> dist = new TreeSet<>();
        
        ts.add(0);

        for(int i = 0 ; i < N ; i ++){
            int num = sc.nextInt();

            ts.add(num);

            Integer high = ts.higher(num);
            Integer low = ts.lower(num);

            if(high == null){
                dist.add(Math.abs(low - num));
            }else if (low == null){
                dist.add(Math.abs(high - num));
            }else{
                dist.add(Math.min(Math.abs(low - num), Math.abs(high - num)));
            }

            System.out.println(dist.first());
        }
    }
}