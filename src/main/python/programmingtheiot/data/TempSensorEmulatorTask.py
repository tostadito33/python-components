import random
from programmingtheiot.data.SensorData import SensorData

class TempSensorEmulatorTask:
	def __init__(self, minTemp=20.0, maxTemp=30.0):
		self.minTemp = minTemp
		self.maxTemp = maxTemp

	def generateTelemetry(self) -> SensorData:
		temp = round(random.uniform(self.minTemp, self.maxTemp), 2)
		sd = SensorData(name="TemperatureSensor")
		sd.setValue(temp)
		print(f"[Sensor] Temperatura simulada: {temp}°C")
		return sd
