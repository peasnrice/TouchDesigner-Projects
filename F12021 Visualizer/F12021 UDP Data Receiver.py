# me - this DAT
#
# dat - the DAT that received the data
# rowIndex - is the row number the data was placed into
# message - an ascii representation of the data
#           Unprintable characters and unicode characters will
#           not be preserved. Use the 'bytes' parameter to get
#           the raw bytes that were sent.
# bytes - a byte array of the data received
# peer - a Peer object describing the originating message
#   peer.close()    #close the connection
#   peer.owner  #the operator to whom the peer belongs
#   peer.address    #network address associated with the peer
#   peer.port       #network port associated with the peer
#

import struct
def onReceive(dat, rowIndex, message, bytes, peer):

    encoded_data = bytes

    packetFormat = struct.unpack_from('H', encoded_data , 0)
    gameMajorVersion = struct.unpack_from('B', encoded_data, 2)
    gameMinorVersion = struct.unpack_from('B', encoded_data, 3)
    packetVersion = struct.unpack_from('B', encoded_data, 4)
    packetID = struct.unpack_from('B', encoded_data, 5)
    sessionUID = struct.unpack_from('Q', encoded_data, 6)
    sessionTime = struct.unpack_from('f', encoded_data, 14)
    frameIdentifier = struct.unpack_from('L', encoded_data, 18)
    playerCarIndex = struct.unpack_from('B', encoded_data, 22)
    secondaryPlayerCarIndex = struct.unpack_from('B', encoded_data, 23)

    # B = uint8
    # H = uint16
    # f = float32
    # Q = uint64

    # Motion
    if packetID[0] == 0:
        carsOnTrack = 1
        x = 0
        worldPositionX = struct.unpack_from('f', encoded_data , 24 + x*56)
        worldPositionY = struct.unpack_from('f', encoded_data , 28 + x*56)
        worldPositionZ = struct.unpack_from('f', encoded_data , 32 + x*56)
        worldVelocityX = struct.unpack_from('f', encoded_data , 36 + x*56)
        worldVelocityY = struct.unpack_from('f', encoded_data , 40 + x*56)
        worldVelocityZ = struct.unpack_from('f', encoded_data , 44 + x*56)
        worldForwardDirX = struct.unpack_from('H', encoded_data , 48 + x*56)
        worldForwardDirY = struct.unpack_from('H', encoded_data , 50 + x*56)
        worldForwardDirZ = struct.unpack_from('H', encoded_data , 52 + x*56)
        worldRightDirX = struct.unpack_from('H', encoded_data , 54 + x*56)
        worldRightDirY = struct.unpack_from('H', encoded_data , 56 + x*56)
        worldRightDirZ = struct.unpack_from('H', encoded_data , 58 + x*56)
        gForceLateral = struct.unpack_from('f', encoded_data , 60 + x*56)
        gForceLongitudinal = struct.unpack_from('f', encoded_data , 64 + x*56)
        gForceVertical = struct.unpack_from('f', encoded_data , 68 + x*56)
        yaw = struct.unpack_from('f', encoded_data , 72 + x*56)
        pitch = struct.unpack_from('f', encoded_data , 76 + x*56)
        roll = struct.unpack_from('f', encoded_data , 80 + x*56)
        
        suspensionPositionRL = struct.unpack_from('f', encoded_data , 1344)
        suspensionPositionRR = struct.unpack_from('f', encoded_data , 1348)
        suspensionPositionFL = struct.unpack_from('f', encoded_data , 1352)
        suspensionPositionFR = struct.unpack_from('f', encoded_data , 1356)
        suspensionVelocityRL = struct.unpack_from('f', encoded_data , 1360)
        suspensionVelocityRR = struct.unpack_from('f', encoded_data , 1364)
        suspensionVelocityFL = struct.unpack_from('f', encoded_data , 1368)
        suspensionVelocityFR = struct.unpack_from('f', encoded_data , 1372)
        suspensionAccelerationRL = struct.unpack_from('f', encoded_data , 1376)
        suspensionAccelerationRR = struct.unpack_from('f', encoded_data , 1380)
        suspensionAccelerationFL = struct.unpack_from('f', encoded_data , 1384)
        suspensionAccelerationFR = struct.unpack_from('f', encoded_data , 1388)
        wheelSpeedRL = struct.unpack_from('f', encoded_data , 1392)
        wheelSpeedRR = struct.unpack_from('f', encoded_data , 1396)
        wheelSpeedFL = struct.unpack_from('f', encoded_data , 1400)
        wheelSpeedFR = struct.unpack_from('f', encoded_data , 1404)
        wheelSlipRL = struct.unpack_from('f', encoded_data , 1408)
        wheelSlipRR = struct.unpack_from('f', encoded_data , 1412)
        wheelSlipFL = struct.unpack_from('f', encoded_data , 1416)
        wheelSlipFR = struct.unpack_from('f', encoded_data , 1420)
        localVelocityX = struct.unpack_from('f', encoded_data , 1424)
        localVelocityY = struct.unpack_from('f', encoded_data , 1428)
        localVelocityZ = struct.unpack_from('f', encoded_data , 1432)
        angularVelocityX = struct.unpack_from('f', encoded_data , 1436)
        angularVelocityY = struct.unpack_from('f', encoded_data , 1440)
        angularVelocityZ = struct.unpack_from('f', encoded_data , 1444)
        angularAccelerationX = struct.unpack_from('f', encoded_data , 1448)
        angularAccelerationY = struct.unpack_from('f', encoded_data , 1452)
        angularAccelerationZ = struct.unpack_from('f', encoded_data , 1456)
        frontWheelsAngle = struct.unpack_from('f', encoded_data , 1460)
        
        op('Motion')[0, 0] = "parameter"
        op('Motion')[0, 1] = "value"
        op('Motion')[1, 0] = "yaw"
        op('Motion')[1, 1] = struct.unpack_from('f', encoded_data , 72 + x*56)[0]
        op('Motion')[2, 0] = "pitch"
        op('Motion')[2, 1] = struct.unpack_from('f', encoded_data , 76 + x*56)[0]
        op('Motion')[3, 0] = "roll"
        op('Motion')[3, 1] = struct.unpack_from('f', encoded_data , 80 + x*56)[0]

    elif packetID[0] == 1:
        x = 0
    elif packetID[0] == 2:
        x = 0
    elif packetID[0] == 3:
        x = 0
    elif packetID[0] == 4:
        x = 0
    elif packetID[0] == 5:
        x = 0

    # Car Telemetry
    elif packetID[0] == 6:
        speed = struct.unpack_from('H', encoded_data , 24)
        throttle = struct.unpack_from('f', encoded_data , 26)
        steer = struct.unpack_from('f', encoded_data , 30)
        brake = struct.unpack_from('f', encoded_data , 34)
        clutch = struct.unpack_from('B', encoded_data , 38)
        gear = struct.unpack_from('b', encoded_data , 39)
        engineRPM = struct.unpack_from('H', encoded_data , 40)
        drs = struct.unpack_from('B', encoded_data , 42)
        revLightPercent = struct.unpack_from('B', encoded_data , 43)
        revLightBitValue = struct.unpack_from('H', encoded_data , 44)
        brakesTemperatureRL = struct.unpack_from('H', encoded_data , 46)
        brakesTemperatureRR = struct.unpack_from('H', encoded_data , 48)
        brakesTemperatureFL = struct.unpack_from('H', encoded_data , 50)
        brakesTemperatureFR = struct.unpack_from('H', encoded_data , 52)
        tyresSurfaceTemperatureRL = struct.unpack_from('B', encoded_data , 54)
        tyresSurfaceTemperatureRR = struct.unpack_from('B', encoded_data , 55)
        tyresSurfaceTemperatureFL = struct.unpack_from('B', encoded_data , 56)
        tyresSurfaceTemperatureFR = struct.unpack_from('B', encoded_data , 57)
        tyresInnerTemperatureRL = struct.unpack_from('B', encoded_data , 58)
        tyresInnerTemperatureRR = struct.unpack_from('B', encoded_data , 59)
        tyresInnerTemperatureFL = struct.unpack_from('B', encoded_data , 60)
        tyresInnerTemperatureFR = struct.unpack_from('B', encoded_data , 61)
        engineTemperature = struct.unpack_from('H', encoded_data , 62)
        tyresPressureRL = struct.unpack_from('f', encoded_data , 64)
        tyresPressureRR = struct.unpack_from('f', encoded_data , 68)
        tyresPressureFL = struct.unpack_from('f', encoded_data , 72)
        tyresPressureFR = struct.unpack_from('f', encoded_data , 76)
        surfaceTypeRL = struct.unpack_from('B', encoded_data , 80)
        surfaceTypeRR = struct.unpack_from('B', encoded_data , 81)
        surfaceTypeFL = struct.unpack_from('B', encoded_data , 82)
        surfaceTypeFR = struct.unpack_from('B', encoded_data , 83)
       
        op('CarTelemetry')[0, 0] = "parameter"
        op('CarTelemetry')[0, 1] = "value"
        op('CarTelemetry')[1, 0] = "speed"
        op('CarTelemetry')[1, 1] = struct.unpack_from('H', encoded_data , 24)[0]
        op('CarTelemetry')[2, 0] = "throttle"
        op('CarTelemetry')[2, 1] = struct.unpack_from('f', encoded_data , 26)[0]
        op('CarTelemetry')[3, 0] = "steer"
        op('CarTelemetry')[3, 1] = struct.unpack_from('f', encoded_data , 30)[0]
        op('CarTelemetry')[4, 0] = "brake"
        op('CarTelemetry')[4, 1] = struct.unpack_from('f', encoded_data , 34)[0]
        
    elif packetID[0] == 7:
        x = 0
    elif packetID[0] == 8:
        x = 0
    elif packetID[0] == 9:
        x = 0
    elif packetID[0] == 10:
        x = 0
    elif packetID[0] == 11:
        x = 0
    else:
        print("no package found for " + packetID[0])
    return