#Hottest Wheels

Do you not dislike loving Mario Kart? Do you even like Need 4 Speed? Do you particularly fancy Paul Walker and you'd like to live _exactly the same_ lifestyle? Well don't even not start it, no.

Hottest Wheels aims to bring you the _hottest_, _wheelest_ (could use tracks tbf) RC racing experience around. Capture the thrill as you drive off course, your wheels fall off, you fall over IRL, or you pull up in last place because you are absolute trash.

#Enough already, what the heck is it?

The general idea is bastardize some lego technics to handle a Raspberry Pi Zero W hooked up to some gear motors, control it with a bluetoot xbox controller, and have them internet connected so that we can do speed penalties and other banterous things to the cars.

The track can be set up anywhere we have cellular access as the cars can connect to hot spots on our phones for the penalties/tracking

Going forwards we would want to implement RFID checkpoints so that we can have a reasonably live leaderboard, or bluetooth beacons for live tracking and mapping.

Penalties can be delivered over wifi. The car in last place can get a speed boost. If a car is too far ahead it can be speed limited. This means we can also issue power ups like:

- Steering reversed
- Every other car neutralised
- Slow downs
- Car only goes in reverse

And generally whatever the hell we like that we can code. I'd also like to see small packets of ball bearings being deployed, or oil slicks, pillars that can be knocked down to crush opponents, swinging pendulums, jumps, loops, etc.

# Materials

- Technics car £30
https://www.amazon.co.uk/42093-Technic-Chevrolet-Collectible-Construction/dp/B07FNW6WQ4/ref=pd_sbs_21_1/259-6728634-0569741
- Motor shield £23
https://shop.pimoroni.com/products/adafruit-dc-stepper-motor-bonnet-for-raspberry-pi
- 50:1 Micro Gear motors (Might need 3 in case both rear wheels need to be driven if the torque isn't enough) £15
https://shop.pimoroni.com/products/micro-metal-gearmotor-extended-back-shaft?variant=3073681025
- Optical encoders for motors £8.75 (to handle stepping for steering)
https://shop.pimoroni.com/products/optical-encoder-pair-kit-for-micro-metal-gearmotors-3-3v
- Gear motor lego shim £3
https://shop.pimoroni.com/products/micro-metal-gearmotor-to-lego-axle-adaptor

Total Cost £79.95

## Additional components
- I think we all own xbox one controllers
- Gearmotor housing to connect to the lego can be ripped from something like this: https://www.thingiverse.com/thing:991997
- Lego pi zero enclosure can be 3d printed as well
- String/twisties for securing weaker bits of lego (can use a glue gun for races)
- AWS/Pusher free tiers
- RFID stickers/readers

# General Approach

- Get the xbox controller sending input to the pi and driving the motors
- Hook up speed penalties via the wifi
- Get tracking for the cars

# Road map

- Motocross style start gate controlled over IoT
- Some form of display to determine current penalties and leaderboard/map
