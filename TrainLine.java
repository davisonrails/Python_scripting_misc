import java.util.Arrays;
import java.util.Random;

public class TrainLine {

	private TrainStation leftTerminus;
	private TrainStation rightTerminus;
	private String lineName;
	private boolean goingRight;
	public TrainStation[] lineMap;
	public static Random rand;

	public TrainLine(TrainStation leftTerminus, TrainStation rightTerminus, String name, boolean goingRight) {
		this.leftTerminus = leftTerminus;
		this.rightTerminus = rightTerminus;
		this.leftTerminus.setLeftTerminal();
		this.rightTerminus.setRightTerminal();
		this.leftTerminus.setTrainLine(this);
		this.rightTerminus.setTrainLine(this);
		this.lineName = name;
		this.goingRight = goingRight;

		this.lineMap = this.getLineArray();
	}

	public TrainLine(TrainStation[] stationList, String name, boolean goingRight)
	/*
	 * Constructor for TrainStation input: stationList - An array of TrainStation
	 * containing the stations to be placed in the line name - Name of the line
	 * goingRight - boolean indicating the direction of travel
	 */
	{
		TrainStation leftT = stationList[0];
		TrainStation rightT = stationList[stationList.length - 1];

		stationList[0].setRight(stationList[stationList.length - 1]);
		stationList[stationList.length - 1].setLeft(stationList[0]);

		this.leftTerminus = stationList[0];
		this.rightTerminus = stationList[stationList.length - 1];
		this.leftTerminus.setLeftTerminal();
		this.rightTerminus.setRightTerminal();
		this.leftTerminus.setTrainLine(this);
		this.rightTerminus.setTrainLine(this);
		this.lineName = name;
		this.goingRight = goingRight;

		for (int i = 1; i < stationList.length - 1; i++) {
			this.addStation(stationList[i]);
		}

		this.lineMap = this.getLineArray();
	}

	public TrainLine(String[] stationNames, String name,
			boolean goingRight) {/*
									 * Constructor for TrainStation. input: stationNames - An array of String
									 * containing the name of the stations to be placed in the line name - Name of
									 * the line goingRight - boolean indicating the direction of travel
									 */
		TrainStation leftTerminus = new TrainStation(stationNames[0]);
		TrainStation rightTerminus = new TrainStation(stationNames[stationNames.length - 1]);

		leftTerminus.setRight(rightTerminus);
		rightTerminus.setLeft(leftTerminus);

		this.leftTerminus = leftTerminus;
		this.rightTerminus = rightTerminus;
		this.leftTerminus.setLeftTerminal();
		this.rightTerminus.setRightTerminal();
		this.leftTerminus.setTrainLine(this);
		this.rightTerminus.setTrainLine(this);
		this.lineName = name;
		this.goingRight = goingRight;
		for (int i = 1; i < stationNames.length - 1; i++) {
			this.addStation(new TrainStation(stationNames[i]));
		}

		this.lineMap = this.getLineArray();

	}

	// adds a station at the last position before the right terminus
	public void addStation(TrainStation stationToAdd) {
		TrainStation rTer = this.rightTerminus;
		TrainStation beforeTer = rTer.getLeft();
		rTer.setLeft(stationToAdd);
		stationToAdd.setRight(rTer);
		beforeTer.setRight(stationToAdd);
		stationToAdd.setLeft(beforeTer);

		stationToAdd.setTrainLine(this);

		this.lineMap = this.getLineArray();
	}

	public String getName() {
		return this.lineName;
	}

	public int getSize() {

		// YOUR CODE GOES HERE
		int counter = 1;
		
		TrainStation thisStation;
		
		thisStation = leftTerminus;
		
		while(!thisStation.equals(rightTerminus)) {
			thisStation = thisStation.getRight();
			counter++;
		}
		
		return counter;
		
	}

	public void reverseDirection() {
		this.goingRight = !this.goingRight;
	}

	// You can modify the header to this method to handle an exception. You cannot make any other change to the header.
	public TrainStation travelOneStation(TrainStation current, TrainStation previous) {

		// YOUR CODE GOES HERE
		if(current.hasConnection && previous.getTransferStation() != current) {
			return current.getTransferStation();
		} else {
			return getNext(current);
		}
		// change this!
	}

	// You can modify the header to this method to handle an exception. You cannot make any other change to the header.
	public TrainStation getNext(TrainStation station) {

		// YOUR CODE GOES HERE
		int counter = 0;
		
		for(int i=0; i < lineMap.length; i ++) {
			if(station.equals(lineMap[i])) {
				counter++;
			}
		}
		
		if(counter < 1) {
			throw new StationNotFoundException(station.getName());
		}
		
		
		if (goingRight && !station.equals(rightTerminus)) {
			return station.getRight();
		} else if (!goingRight && !station.equals(leftTerminus)){
			return station.getLeft();
		} else if (goingRight && station.equals(rightTerminus)){
			reverseDirection();
			return station.getLeft();
		} else if (!goingRight && station.equals(leftTerminus)){
			reverseDirection();
			return station.getRight();
		} 
		throw new StationNotFoundException(station.getName());
		// change this!
	}

	// You can modify the header to this method to handle an exception. You cannot make any other change to the header.
	public TrainStation findStation(String name) {

		// YOUR CODE GOES HERE
		for(int i=0; i < lineMap.length; i++) {
			if(name.equals(lineMap[i].getName())) {
				return lineMap[i];
			}
		}
		throw new StationNotFoundException(name);
		// change this!
	}

	public void sortLine() {

		// YOUR CODE GOES HERE
        for (int i = 0; i < lineMap.length-1; i++) { 
            for (int j = 0; j < lineMap.length-i-1; j++) {
            	if (lineMap[j].getName().compareTo(lineMap[j+1].getName()) > 0) {
                    TrainStation temp = lineMap[j];
                    lineMap[j] = lineMap[j+1];
                    lineMap[j+1] = temp;
                }
            }
        }
        
        for(int i=0; i < lineMap.length; i++) {
			lineMap[i].setNonTerminal();
			if (i == 0) { 
				leftTerminus = lineMap[i];
				lineMap[i].setLeft(null);
				lineMap[i].setLeftTerminal();
			}
			if(i != 0) {
				lineMap[i].setLeft(lineMap[i-1]);
			}
			if (i == lineMap.length - 1) {
				rightTerminus = lineMap[i];
				lineMap[i].setRightTerminal();
				lineMap[i].setRight(null);
				
			}
			if(i != lineMap.length - 1) {
				lineMap[i].setRight(lineMap[i+1]);
			}
		}
        
        
	}

	public TrainStation[] getLineArray() {

		// YOUR CODE GOES HERE
		TrainStation[] deepCopied = new TrainStation[getSize()];
		
		deepCopied[0] = leftTerminus;
		int i = 1;
		
		while(!deepCopied[i-1].equals(rightTerminus) && i < getSize()) {
			deepCopied[i] = deepCopied[i-1].getRight();
			i++;
		}
		
		return deepCopied; // change this
		
	}

	private TrainStation[] shuffleArray(TrainStation[] array) {
		Random rand = new Random();

		for (int i = 0; i < array.length; i++) {
			int randomIndexToSwap = rand.nextInt(array.length);
			TrainStation temp = array[randomIndexToSwap];
			array[randomIndexToSwap] = array[i];
			array[i] = temp;
		}
		this.lineMap = array;
		return array;
	}

	public void shuffleLine() {

		// you are given a shuffled array of trainStations to start with
		TrainStation[] lineArray = this.getLineArray();
		TrainStation[] shuffledArray = shuffleArray(lineArray);

		// YOUR CODE GOES HERE
		
		for(int i=0; i < shuffledArray.length; i++) {
			lineMap[i].setNonTerminal();
			if (i == 0) { 
				leftTerminus = lineMap[i];
				lineMap[i].setLeft(null);
				lineMap[i].setLeftTerminal();
			}
			if (i == shuffledArray.length - 1) {
				rightTerminus = lineMap[i];
				lineMap[i].setRightTerminal();
				lineMap[i].setRight(null);
				
			}
			if(i != 0) {
				lineMap[i].setLeft(lineMap[i-1]);
			}
			if(i != shuffledArray.length - 1) {
				lineMap[i].setRight(lineMap[i+1]);
			}
		}
		
	}

	public String toString() {
		TrainStation[] lineArr = this.getLineArray();
		String[] nameArr = new String[lineArr.length];
		for (int i = 0; i < lineArr.length; i++) {
			nameArr[i] = lineArr[i].getName();
		}
		return Arrays.deepToString(nameArr);
	}

	public boolean equals(TrainLine line2) {

		// check for equality of each station
		TrainStation current = this.leftTerminus;
		TrainStation curr2 = line2.leftTerminus;

		try {
			while (current != null) {
				if (!current.equals(curr2))
					return false;
				else {
					current = current.getRight();
					curr2 = curr2.getRight();
				}
			}

			return true;
		} catch (Exception e) {
			return false;
		}
	}

	public TrainStation getLeftTerminus() {
		return this.leftTerminus;
	}

	public TrainStation getRightTerminus() {
		return this.rightTerminus;
	}
}

//Exception for when searching a line for a station and not finding any station of the right name.
class StationNotFoundException extends RuntimeException {
	String name;

	public StationNotFoundException(String n) {
		name = n;
	}

	public String toString() {
		return "StationNotFoundException[" + name + "]";
	}
}
