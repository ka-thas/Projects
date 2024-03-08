class Solution {
    public boolean isPalindrome(int x) {
        String y = Integer.toString(x);
        
        String reversed = "";
        for (int i = 0; i < y.length(); i++){
            reversed = y.charAt(i) + reversed;
        }

        return y.equals(reversed);
    }
}

class Løsningsforslag {
    public boolean isPalindrome(int x) {
        // Effektivisering
        if (x < 0 || (x > 10) && (x % 10 == 0)) {
            return false;
        } else if (x < 10) {
            return true;
        }
        
        // Reverserer x som int
        int r = 0;
        while (x > r) {
            r *= 10;
            r += x % 10;
            x /= 10;
        }
        
        if (x == r || (x * 10 + r % 10 == r && x != 0)) {
            return true;
        } else {
            return false;
        }
    }
}