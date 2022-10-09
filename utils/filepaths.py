BASEDIR = ""

# Assets
LOGO_L = BASEDIR + "misc/assets/Blue L.png"
LOGO_LT = BASEDIR + "misc/assets/Blue L+T.png"

# Subdirs
GPS = "Parsed/GPS/"
PRIMARY = "Parsed/primary/"
SECONDARY = "Parsed/secondary/"

# Primary


# Secondary
GYRO  = SECONDARY + "IMU_ANGULAR_RATE.csv"
ACCEL = SECONDARY + "IMU_ANGULAR_RATE.csv"
PEDALS = SECONDARY + "PEDALS_OUTPUT.csv"
STEER = SECONDARY + "STEERING_ANGLE.csv"
CONTROL = SECONDARY + "CONTROL_OUTPUT.csv"

# GPS
PVT = GPS + "GPS_NAV_PVT.csv"
DOP = GPS + "GPS_NAV_DOP.csv"
LLH = GPS + "GPS_NAV_HPPOSLLH.csv"

# All files
CSV_FILES = [
    GYRO,
    ACCEL,
    PEDALS,
    STEER,
    CONTROL,
    PVT,
    DOP,
    LLH,
]