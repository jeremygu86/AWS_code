CREATE TABLE uwhivetest (
	eventId string, 
	miscHeader struct <vin: string>,
	snapshots struct <
		samples: array <
			struct <
	  			ambientAirTemp: float, 
	  			catIntakeGasTemp: float, 
	  			catOutletGasTemp: float, 
	  			engCoolantTemp: float, 
	  			engineSpeed: int 
  			>
		>
	>,
	state string,
	vehicleData struct <totalDistance: int, totalEngineHours: int>)
clustered by (eventId) into 5 buckets 
stored as orc;