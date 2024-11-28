class CallByValue {
    public void example(int x, int y) {
        x++;
        y++;
    }
}

public class Main {
    public static void main(String[] args)
    {
    int a = 10;
    int b = 20;

    CallByValue object = new CallByValue();
    System.out.println("Value of a: " + a + " & b: " + b);

    object.example(a, b);

    System.out.println("Value of a: " + a + " & b: " + b);
    }
}