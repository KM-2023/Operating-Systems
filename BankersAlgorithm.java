
import java.util.Scanner;   // to read order of processes from user


//Java implementation of Bankers Algorithm
public class BankersAlgorithm
{
	/*                                     Map of methods in this class 
	 * 
	 *      initializemetrices  = method to initialize the availability, allocated, maximum need matrices and variables used thruought the program
	 *                          = two initializations sets are provided : 1 for SAFE example, 1 for UNSAFE example (commented out)
	 *      system_safe_state = method to evaluate if a state is safe or not
	 * 
	 * */
	
/* To implement Banker's algorithm the initial values to the allocation, maximum_neededimum need, available matrix were taken from the tutorial on Banker's algorithm.*/
	
	// declaring and initializing variables
	int n = 5;          // Number of processes: P1 - P5
	int m = 3;          // Number of resources: A B C
	
	int remaining_need[][] = new int[n][m];            //remaining need matrix
	int [][]maximum_needed;               // maximum_neededimum need column
	int [][]allocation;       //allocated matrix (for all processes across all resources )
	int []available;         //available column
	
	int safeSequence[] = new int[n];     // an array to store the sequence of processes if they do not result in deadlock condition
	
//==========================================================================================================================================================
	
   //	a method that initializes the values of the allocation, maximum_neededimum need, availability and remaining need metrices. 
	void initializemetrices()
		{
		
				
        /** Multiprocess SAFE **/
		
//		// Allocation Matrix 
//		int [] P1 = { 0, 1, 0 };
//		int [] P2 = { 2, 0, 0 };
//		int [] P3 = { 3, 0, 2 };
//		int [] P4 = { 2, 1, 1 };
//		int [] P5 = { 0, 0, 2 };
//		
//		//maximum_neededimum needed resources matrix initialization
//		int[] maxP1 = { 7, 5, 3 };
//		int[] maxP2 = { 3, 2, 2 };
//		int[] maxP3 = { 9, 0, 2 };
//		int[] maxP4 = { 2, 2, 2 };
//		int[] maxP5 = { 4, 3, 3 };
//		
//		// available resources 
//		int[] available_resources = new int[] { 3, 3, 2 }; 	
		
				  /** Multiprocess UNSAFE **/
		
//         P1, P2, P3, P4, P5 are the Process names here 
		// Allocation Matrix 
		int [] P1 = { 0, 1, 0 };
		int [] P2 = { 2, 0, 0 };
		int [] P3 = { 3, 0, 2 };
		int [] P4 = { 2, 1, 1 };
		int [] P5 = { 0, 0, 3 };
		int [][] processes_order = new int [5][3];
			
		//maximum_neededimum needed resources matrix initialization
		int[] maxP1 = { 7, 5, 3 };
		int[] maxP2 = { 3, 2, 2 };
		int[] maxP3 = { 9, 0, 2 };
		int[] maxP4 = { 2, 2, 2 };
		int[] maxP5 = { 4, 3, 3 };
		
		// available resources 
		int[] available_resources = new int[] {1 , 0,  2};
        
		

		
		//assigning the process values reordered according to the order specified by user
		allocation = new int[][] {P1,P2, P3,P4, P5};
		
	    //assigning the process values reordered according to the order specified by user
	    maximum_needed = new int[][] { maxP1,maxP2, maxP3,maxP4, maxP5};  //calling the method to reorder maximum avilable resources according to resource order

	    // Available Resources 
		available = available_resources; 
		
		// calculating remaining_need by subtracing allocation from maximum_need for every process
		for (int i = 0;i < n; i++)
		{
			for (int j = 0;j < m; j++)
			{
			remaining_need[i][j] = maximum_needed[i][j]-allocation[i][j];    // finding the difference between maximum need and allocated to find remaining need
			}
		}	 
	}

//==========================================================================================================================================================

	// a method to check if the sequence of processes leads to a safe state of the system or an unsafe one
	
	void system_safe_state() {
		int count = 0;
		boolean visited[] = new boolean [n];   // an array to check if a process has already been added to the safe sequence array
		                                       //initialised with false values by default
		//work array to store the copy of available resources
		int work[] = new int[m]; 
		for (int i = 0;i < m; i++)
		{
			work[i] = available[i];
		}
		
		while (count<n) {    // iterating until all processes are added in a sequence that is safe if it can be
			                 // however, if the processs result in unsafe system, the program will exit the while loop
			                 // so this while loop is exited only when either all the processes are added (safe) or interrupt (due to unsafe)
			
			boolean flag = false;  // boolean variable to be used to detect if at least one process can be safely assigned the needed resources within one iteration of all the processes
			                       // will be set to true if a process has been found 
			
			for (int i = 0;i < n; i++)
			{
				if (visited[i] == false)  // that is if this process hasn't been added to the safe list 
				{
					int j;
					
					// for selecting process check if all the resources' remaining_need instance is less than the available(work)
					for (j = 0;j < m; j++)
					{	
						// if 
						if (remaining_need[i][j] > work[j])
						break;
					}
					
					if (j == m)   // all resources requested by this process can be granted and the process will be added to the safelist
					{
						safeSequence[count++]=i;
						visited[i]=true;         //updating the visited so that it is not visited again
						flag = true;
						// Updating the work with the allocation + previous work (availability values)
						
						// this updated work of the resources indicate potential resources that could be assigned to the upcoming processes 
						// (the work is summed/added to the allocation because we assume a resource allocated to a process will be released once it completes execution
						// and thus an available resources )
						
						for (j = 0;j < m; j++)
						{
							work[j] = work[j]+allocation[i][j];
						}	
							
					}
				}
			}
			// if none of the processes can be given the resources needed due to the needed instances being higher than the available for all processes
			// then there is no need to iterate again as there is no use
			// if flag has been set to true however, it means that at least once process can safely be given the needed resources
			// then we can check for the rest processes by usig the work (allocated + prior work)
			if (flag == false)
			{
				break;
			}
			
		}
		// After inspect all the processes specified we shall determine if a system is safe or not
		if (count < n)
		{
			System.out.println("The System with the provided processes and resource request is UNSAFE!\n");
			
			System.out.println("Potentially, it could result in a deadlock situation. ");
			// at least one process could not be assigned the needed resources, and therefore by definition is unsafe system
		}
		else
		{
			// By definition since all processes were given the needed processes the system is safe
			
			System.out.print("The system is SAFE, with the sequence of processes: ");
					for (int i = 0;i < n; i++)
			{
				System.out.print("P" + safeSequence[i]);
				if (i != n-1)
				System.out.print(" -> ");
			}
			System.out.print("\n\nConsequently, the system cannot be in a deadlock situation (by definition).");
		}
	}
	
//==========================================================================================================================================================
	
	
	public static void main(String[] args)           // main method of the BankersAlgorithm class
	{ 
		// creating a BankersAlgorithm object 
		BankersAlgorithm banker = new BankersAlgorithm();
			
		// a method to initialize the allocated, maximum_need, remaining_need and available matrices and vectors
		banker.initializemetrices(); 

		// Check whether system is in safe state or not 
		banker.system_safe_state();			
	
	}
}


//=====================================================The End =======================================================================================


/** Single-process SAFE **/

//int[] p1_single = {0 , 1 , 0};
//int [] max_single = {4, 3, 2};
//int[] available_resources = {1 , 0,  2};
/** Single-process UNSAFE **/
//
//int[] p1_single = {0 , 1 , 0};
//int [] max_single = {4, 3, 2};
//int[] available_resources ={4 , 2,  2};

