class Place {
  int code;
  String name;
  float x;
  float y;
  
  public Place(int code, String name, float x, float y) {
    this.code = code;
    this.name = name;
    this.x = x;
    this.y = y;
  }
  
  void draw( ) {
    int xx = (int) TX(x);
    int yy = (int) TY(y);
    set(xx, yy, #000000);
  }
}
