#!/bin/false
# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
#
# Copyright (C) 2013 Gordon Williams <gw@pur3.co.uk>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# ----------------------------------------------------------------------------------------
# This file contains information for a specific board - the available pins, and where LEDs,
# Buttons, and other in-built peripherals are. It is used to build documentation as well
# as various source and header files for Espruino.
# ----------------------------------------------------------------------------------------

import pinutils;
info = {
 'name' : "STM32 F0 Discovery",
 'link' :  [ "http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/PF253215" ],
 'variables' : 1720,
};
chip = {
  'part' : "STM32F051R8T6",
  'family' : "STM32F0",
  'package' : "LQFP64",
  'ram' : 8,
  'flash' : 64,
  'speed' : 48,
  'usart' : 2,
  'spi' : 2,
  'i2c' : 2,
  'adc' : 1,
  'dac' : 1,
};
# left-right, or top-bottom order
board = {
  'left' : [ '3V','GND','VBAT','C13','C14','C15','F0','F1','GND','NRST','C0','C1','C2','C3','A0','A1','A2','A3','F4','F5','A4','A5','A6','A7','C4'.'C5','B0','B1','B2','B10','B11','B12','GND' ],
  'right' : [ '5V','GND','B9','B8','VDD','BOOT0','B7','B6','B5','B4','B3','B2','C12','C11','C10','A15','A14','F7','F6','A13','A12','A11','A10','A9','A8','C9','C8','C7','C6','B15','B14','B13','GND' ],
};
devices = {
  'OSC' : { 'pin_1' : 'F0',
            'pin_2' : 'F1' },
  'OSC_RTC' : { 'pin_1' : 'C14',
                'pin_2' : 'C15' },
  'LED1' : { 'pin' : 'C9' },
  'LED2' : { 'pin' : 'C8' },
  'BTN1' : { 'pin' : 'A0' },
};


board_css = """
#board {
  width: 630px;
  height: 947px;
  left: 200px;
  background-image: url(img/STM32F0DISCOVERY.jpg);
}
#boardcontainer {
  height: 947px;
}
#left {
  top: 82px;
  right: 505px;
}
#right  {
  top: 82px;
  left: 505px;
}
""";

def get_pins():
  pins = pinutils.scan_pin_file([], 'stm32f303.csv', 3, 6, 7)
  pins = pinutils.scan_pin_af_file(pins, 'stm32f303_af.csv', 1, 2)
#  print(json.dumps(pins, sort_keys=True, indent=2))  
#  return pinutils.only_from_package(pinutils.fill_gaps_in_pin_list(pins), chip["package"])
  return pinutils.fill_gaps_in_pin_list(pins)
