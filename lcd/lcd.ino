#include <LiquidCrystal_I2C.h>
#include <Firmata.h>
#include <Wire.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
int lastLine = 1;

int i;



void stringDataCallback(char *stringData){
   if ( lastLine ) {
     lastLine = 0;
     lcd.clear();
   } else {
     lastLine = 1;
     lcd.setCursor(1,0);
   }
   lcd.print(stringData);
}

void setup() {
  lcd.begin();
  Firmata.setFirmwareVersion( FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION );
  Firmata.attach( STRING_DATA, stringDataCallback);
  Firmata.begin();  
}

void loop() {
  while ( Firmata.available() ) {
    Firmata.processInput();
  }
 for (i=0; i <= 10; i++){
  lcd.scrollDisplayLeft();
  delay(200);
 }
}
