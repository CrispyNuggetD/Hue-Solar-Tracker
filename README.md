# Hue-Solar-Tracker
Finding the correlation between Luxmeter in Philips Hue Motion Sensor. (Using Philips Hue Developer API).

I can't find the equation for this, so I just went ahead and did it as I needed a makeshift luxmeter for a project on solar energy sustainability in Singapore.
If you have related knowledge, please do not hesitate to contact me.

## Preface
A given amount of light will illuminate a surface more dimly if it
is spread over a larger area, so illuminance is inversely proportional to area when the luminous flux is held constant.
One lux is equal to one lumen per square metre: 1 lx = 1 lm/m2 = 1 cd·sr/m2.
Hence, we use the exponential function to find the standard curve equation

## Instructions:
1. Point iPhone LED light at sensor from a distant between 0 - 1.0 meter
2. Obtain value of sensor photodiode reading using Philips Hue Developer Sensor APIs. (E.g. Using Mac’s Terminal Application to run Python script with JSON to API)
3. Use Apple Home app to obtain calibrated Lux Value.
4. Confirm reliability (R2 = 0.9999)

![Standard Curve](https://user-images.githubusercontent.com/6136369/149661712-20b37faa-8b3d-4508-bc62-64fb5c751514.jpg)
