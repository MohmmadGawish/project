public class Professor {
    String nameprof;
    String department;
    Course teachingCourse;
    public Professor(String nameprof, String department,Course teachingCourse) {
        this.nameprof = nameprof;
        this.department = department;
        this.teachingCourse = teachingCourse;
    }
    public void displayProfessorInfo(){
        System.out.print("Name of Prof : "+nameprof);
        System.out.print("Name of department : "+department);
        System.out.println();
        System.out.print("Name of Teaching Course : "+teachingCourse.title);
    }
}
