public class HCF {
    public static void main(String[] args) {
        int n1 = 56; 
        int n2= 64;

        int ans = Math.min(n1,n2); 

        while(ans>0){
        if(n1%ans==0 && n2%ans==0){
            System.out.println("HCF Found" + "  " + ans);
            break;
        } 
            ans--; 
        }

    }
}
