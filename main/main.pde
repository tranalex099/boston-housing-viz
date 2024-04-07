// column numbers in the data file
static final int CODE = 0;
static final int X = 1;
static final int Y = 2;
static final int NAME = 3;

int totalCount; // total number of places
Place[] places;
int placeCount; // number of places loaded

// min/max boundary of all points
float minX, maxX;
float minY, maxY;

public void setup( ) {
  readData( );
}

void readData( ) {
  String[] lines = loadStrings("zips.tsv");
  parseInfo(lines[0]); // read the header line
  places = new Place[totalCount];
  for (int i = 1; i < lines.length; i++) {
    places[placeCount] = parsePlace(lines[i]);
    placeCount++;
  }
}

void parseInfo(String line) {
  String infoString = line.substring(2); // remove the #
  String[] infoPieces = split(infoString, ',');
  totalCount = int(infoPieces[0]);
  minX = float(infoPieces[1]);
  maxX = float(infoPieces[2]);
  minY = float(infoPieces[3]);
  maxY = float(infoPieces[4]);
}

Place parsePlace(String line) {
  String pieces[] = split(line, TAB);
  
  int zip = int(pieces[CODE]);
  float x = float(pieces[X]);
  float y = float(pieces[Y]);
  String name = pieces[NAME];
  
  return new Place(zip, name, x, y);
}

// Border of where the map should be drawn on screen
float mapX1, mapY1;
float mapX2, mapY2;

public void setup( ) {
  size(720, 453, P3D);
  mapX1 = 30;
  mapX2 = width - mapX1;
  mapY1 = 20;
  mapY2 = height - mapY1;
  readData( );
}
