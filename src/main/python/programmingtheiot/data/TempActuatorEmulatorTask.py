from programmingtheiot.data.ActuatorData import ActuatorData

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
