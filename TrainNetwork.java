class TrainNetwork {
	final int swapFreq = 2;
	TrainLine[] networkLines;

    public TrainNetwork(int nLines) {
    	this.networkLines = new TrainLine[nLines];
    }
    
    public void addLines(TrainLine[] lines) {
    	this.networkLines = lines;
    }
    
    public TrainLine[] getLines() {
    	return this.networkLines;
    }
    
    public void dance() {
    	System.out.println("The tracks are moving!");
    	//YOUR CODE GOES HERE
    	for(int i=0; i < networkLines.length; i++) {
    		networkLines[i].shuffleLine();
    	}
    	
    }
    
    public void undance() {
    	//YOUR CODE GOES HERE
    	for(int i=0; i < networkLines.length; i++) {
    		networkLines[i].sortLine();
    	}
    }
    
    public int travel(String startStation, String startLine, String endStation, String endLine) {
    	
    	TrainLine curLine = getLineByName(startLine); //use this variable to store the current line.
    	TrainStation curStation = curLine.findStation(startStation); //use this variable to store the current station. 
    	
    	
    	int hoursCount = 0;
    	int counter = 0;
    	System.out.println("Departing from "+startStation);
    	
    	//YOUR CODE GOES HERE
    	TrainStation previous = curStation; 
    	
    	while(!curStation.getName().equals(endStation)) {
    		
    		TrainStation temp = curStation;
    		
    		if(hoursCount == 168) {
    			System.out.println("Jumped off after spending a full week on the train. Might as well walk.");
    			return hoursCount;
    		}
    		
    		counter++;
    		hoursCount = counter;
    		curStation = curLine.travelOneStation(curStation, previous);
    		previous = temp;
    		curLine = curStation.getLine();
    		
    		
    		//prints an update on your current location in the network.
	    	System.out.println("Traveling on line "+curLine.getName()+":"+curLine.toString());
	    	System.out.println("Hour "+hoursCount+". Current station: "+curStation.getName()+" on line "+curLine.getName());
	    	System.out.println("=============================================");
	    	
	    	if(hoursCount != 0 && hoursCount % 2 == 0) {
	    		dance();//remove this! this break is only there so the template compiles.
	    	}
    	}
	    	
	    System.out.println("Arrived at destination after "+hoursCount+" hours!");
	    return hoursCount;
    }
    
    
    //you can extend the method header if needed to include an exception. You cannot make any other change to the header.
    public TrainLine getLineByName(String lineName){
    	//YOUR CODE GOES HERE
    	TrainLine[] theLines = getLines();
    	for(int i=0; i < theLines.length; i++) {
    		if(theLines[i].getName().equals(lineName)) {
    			return theLines[i];
    		}
    	}
    	throw new LineNotFoundException(lineName);
    	//change this
    }
    
  //prints a plan of the network for you.
    public void printPlan() {
    	System.out.println("CURRENT TRAIN NETWORK PLAN");
    	System.out.println("----------------------------");
    	for(int i=0;i<this.networkLines.length;i++) {
    		System.out.println(this.networkLines[i].getName()+":"+this.networkLines[i].toString());
    		}
    	System.out.println("----------------------------");
    }
}

//exception when searching a network for a LineName and not finding any matching Line object.
class LineNotFoundException extends RuntimeException {
	   String name;

	   public LineNotFoundException(String n) {
	      name = n;
	   }

	   public String toString() {
	      return "LineNotFoundException[" + name + "]";
	   }
	}