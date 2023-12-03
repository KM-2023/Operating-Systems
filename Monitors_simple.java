
public class Monitors_simple {
	
	/*  In this program there are two processes p1 and p2 having one shared variable shared_value.
	 * 
	 *    =  p1 adds 100 to the shared_value 
	 *    
	 *    =  p2 subtracts 100 from the shared_value
	 *    
	 *    the values were selected to showcase how monitors solution could be employed in interprocess communication
	 * 
	 * */

    static P1 p1 = new P1();	 // instantiate a new P1 object
    static P2 p2 = new P2();	 // instantiate a new P2 object
    
    static int shared_value = 0;    //variable shared by the two processes in the critical section
    
    static SharedClass shared_class = new SharedClass();    //  instantiating an object of the sharedclass that includes where the critical section is manipualted

    
    public static void main(String args[]) {         // main method of the Monitors class
    	
    	p1.start(); // addes 100 to the shared variable
        p2.start(); // subtracts 100 from the shared variable integer
       
    }

    
// =========================================================================================================================

    /***         A class for process P1         ***/
    
    static class P1 extends Thread {     // this class inherits the java Thread class, so we can utilise Thread's methods.

        public void run() {       // executed when a thread starts running. 
        	
        	while (true) {         // an endless loop always trying to add 100 to the shared variable
        		
        		// Calling the add method from using the SharedClass object. 
            	shared_class.add();
            	            	
                // suspending the thread for 1 second
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
        	}
          }
        }

    
// =========================================================================================================================

    
    /***         A class for process P2         ***/
    
    static class P2 extends Thread {         // this class inherits the java Thread class, so we can utilise Thread's methods.
    	
        public void run() {  	 // executed when a thread starts running. 
        	
        	while (true) {      // an endless loop always trying to subtract 100 from the shared variable
        		
        		// Calling the subtract method from using the SharedClass object. 
               shared_class.subtract();
            	                
               // suspending the thread for 1 second
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }        		
        	}
            
            
        }
        
    }

    
// =========================================================================================================================

   
       /***      Monitor class that holds critical section and changes on it        ***/

    static class SharedClass {
    	
    	
       
        public synchronized void add() {     /* the keyword synchronized helps to achieve mutual exclusion in a multithreaded environment
        	                                   all methods with this keyword are blocked when this thread is executing */
        	
        	shared_value = shared_value + 100;     // updating critical section variable by adding 100 to it 
        	
        	System.out.println("Value after P1 adds is: " + shared_value);    // printing the updated shared value      
    
        }

        // =========================================================================================================================

        public synchronized void subtract() {
            
        	shared_value = shared_value - 100;    // updating critical section variable by subtracting 100 from it 
        	
        	
        	System.out.println("Value after P2 subtracts is is: " + shared_value);      // printing the updated shared value
        	

        }

        // ===============================   Ending of Simple Monitor Implementation=================================================================

    }
}
