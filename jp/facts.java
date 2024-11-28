import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class facts extends JFrame implements ActionListener {
    JLabel i1, i2, i3;
    JTextField tf1, tf2;
    JButton b1;

    public facts() {
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        FlowLayout g = new FlowLayout();
        setLayout(g);
        i1 = new JLabel("enter value");
        i1.setForeground(Color.BLUE);
        add(i1);
        tf1 = new JTextField(5);
        tf1.setText("0");
        add(tf1);
        b1 = new JButton("compute");
        b1.addActionListener(this);
        add(b1);
        i3 = new JLabel();
        add(i3);
        i2 = new JLabel("factorial:");
        i2.setForeground(Color.BLUE);
        add(i2);
        tf2 = new JTextField(5);
        add(tf2);
    }

    public void actionPerformed(ActionEvent ae) {
        long n = Integer.parseInt(tf1.getText());
        long f = 1;
        while (n != 0) {
            f = f * n;
            n--;
        }
        tf2.setText(String.valueOf(f));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            fact frame = new fact();
            frame.setVisible(true);
        });
    }
}