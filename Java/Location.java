public class Location {
    String roomName;
    String building;
    int capacity; //سعة القاعه

    public Location(String building, int capacity, String roomName) {
        this.building = building;
        this.capacity = capacity;
        this.roomName = roomName;
    }
    public void displayLocation(){
        System.out.println();
        System.out.print("Sashan in " +building+"room"+ roomName);
    }
}