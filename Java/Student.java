public class Student {
    String studentName;
    int studentID;
    String major;

    public Student(String studentName, String major, int studentID) {
        this.studentName = studentName;
        this.major = major; //التخصص بتاع الواد الغلبان
        this.studentID = studentID;
    }
    public void printStudentInfo(){
        System.out.print("Name is : " + studentName);
        System.out.println();
        System.out.print("ID is : " + studentID);
        System.out.println();
        System.out.print("dep is : " + major);
    }
}
