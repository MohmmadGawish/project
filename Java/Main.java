import java.util.*;

import static java.lang.System.in;
import static java.lang.System.out;
public class Main {


    public static void main(String[] args) {

       Location C1 = new Location("CS",100,"MO");
       Course javaCourse = new Course("Java","J551",90,C1);
       Professor DrMo = new Professor("Mohammad","CS",javaCourse);
       Student MO = new Student("MOmo","CS",55110);
        // طباعة "تقرير" عن الحالة اللي إحنا عملناها
        System.out.println("--- Reborte ---");
        DrMo.displayProfessorInfo();
        javaCourse.displayDetails();
        MO.printStudentInfo();
        out.println("is Done");
    }
}