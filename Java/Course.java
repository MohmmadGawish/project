public class Course {

        String title;
        String code;
        int studentNumber;
        Location courseLocation;
        private int studentMax;
    public Course(String title, String code, int max, Location location) {
        this.title = title;
        this.code = code;
        this.studentMax = max;
        this.studentNumber = 0;
        this.courseLocation = location;
    }
    public void addStudent() {
        if (studentNumber < studentMax) {
            studentNumber++;
            System.out.println("Done : " + title);
        } else {
            System.out.println("Sorry " + title + " is Done ");
        }
    }
    public void displayDetails() {
        System.out.println(" Name of course :  " + title);
        System.out.println(" ID of course :  " + code);
        System.out.println(" Number of Students " + studentNumber + " to " + studentMax);
    }
}



