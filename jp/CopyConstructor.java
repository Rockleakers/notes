class Rectangle {
    int length;
    int breadth;

    Rectangle(int l, int b) {
        length = l;
        breadth = b;
    }

    Rectangle(Rectangle obj) {
        System.out.println("Copy Constructor Invoked");
        length = obj.length;
        breadth = obj.breadth;
    }

    int area() {
        return (length * breadth);
    }
}

class CopyConstructor {
    public static void main(String[] args) {
        Rectangle firstRect = new Rectangle(5, 6);
        Rectangle secondRect = new Rectangle(firstRect);
        System.out.println("Area of First Rectangle : " + firstRect.area());
        System.out.println("Area of First Second Rectangle : " + secondRect.area());
    }
}