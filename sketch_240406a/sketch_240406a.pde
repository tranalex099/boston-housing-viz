color backgroundColor = #333333; // dark background color
color dormantColor = #999966; // initial color of the map
color highlightedColor = #CBCBCB; // color for selected points
color unhighlightedColor = #66664C; // color for points that are not selected
color badColor = #FFFF66; // text color when nothing found

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

void draw( ) {
  int xx = (int) TX(x);
  int yy = (int) TY(y);
  set(xx, yy, #000000);
}

public void draw( ) {
  background(255);
  for (int i = 0; i < placeCount; i++) {
    places[i].draw( );
  }
}

float TX(float x) {
  return map(x, minX, maxX, mapX1, mapX2);
}
float TY(float y) {
  return map(y, minY, maxY, mapY2, mapY1);
}

PFont font;
String typedString = "";
char typedChars[] = new char[5];
int typedCount;
int typedPartials[] = new int[6];
float messageX, messageY;
int foundCount;
