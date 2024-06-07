import java.util.ArrayList;
import java.util.Random;

class NavetArrangerer {
    static String navet() {
    String[] arr = {"10", "0000", "0", "111"};
    
    String output = "";

    for (String tall : arr) {
        output += Integer.parseInt(tall, 2);
    }
    return output;
    }

static String NavetFacts(String noeKult) {
    ArrayList<String> navetFacts = new ArrayList<String>();
    navetFacts.add(noeKult);
    navetFacts.add("Navet har et arrangement nesten her tirsdag og torsdag!");
    navetFacts.add("DNB er Navets samarbeidspartner.");
    navetFacts.add("En kul fact her hadde vart lurt...");
    
    Random random = new Random() ;
    int randomIndex = random.nextInt(navetFacts.size( ));
    String randomElement = navetFacts.get (randomIndex);
    
    return randomElement;
}

public static void main(String[] args) {
    String navetFacts = NavetFacts("Navet tar inn nye interne hvert semester.");
    System.out.println("Dette aret et spessielt for Navet, " + navet());
    }
} 