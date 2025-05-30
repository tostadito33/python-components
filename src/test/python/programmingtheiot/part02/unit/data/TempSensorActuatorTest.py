import unittest
import random
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.ActuatorData import ActuatorData

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

class TempActuatorEmulatorTask:
	def __init__(self, threshold=25.0):
		self.threshold = threshold

	def processTelemetry(self, sensorData) -> ActuatorData:
		actuatorData = ActuatorData(name="FanActuator")
		temp = sensorData.getValue()

		if temp > self.threshold:
			actuatorData.setCommand(1)
			actuatorData.setStateData("Ventilador encendido")
			print("[Actuador] Temperatura alta. Ventilador ENCENDIDO.")
		else:
			actuatorData.setCommand(0)
			actuatorData.setStateData("Ventilador apagado")
			print("[Actuador] Temperatura normal. Ventilador apagado.")

		actuatorData.setValue(temp)
		return actuatorData

class TempSensorActuatorTest(unittest.TestCase):

	def setUp(self):
		self.sensor = TempSensorEmulatorTask()
		self.actuator = TempActuatorEmulatorTask(threshold=25.0)

	def testActuatorTriggered(self):
		class FakeSensor:
			def getValue(self): return 26.5
		response = self.actuator.processTelemetry(FakeSensor())
		self.assertEqual(response.getCommand(), 1)
		self.assertIn("encendido", response.getStateData().lower())

	def testActuatorNotTriggered(self):
		class FakeSensor:
			def getValue(self): return 23.0
		response = self.actuator.processTelemetry(FakeSensor())
		self.assertEqual(response.getCommand(), 0)
		self.assertIn("apagado", response.getStateData().lower())

if __name__ == '__main__':
	# Ejecutar como demo principal:
	print("=== EJECUCIÓN DEMO: SENSOR + ACTUADOR ===")
	sensor = TempSensorEmulatorTask()
	actuator = TempActuatorEmulatorTask()

	sd = sensor.generateTelemetry()
	ad = actuator.processTelemetry(sd)

	print("\n=== EJECUCIÓN DE TESTS UNITARIOS ===")
	unittest.main(argv=['first-arg-is-ignored'], exit=False)
