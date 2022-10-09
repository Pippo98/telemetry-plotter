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

# All files
CSV_FILES = [
    GYRO,
    ACCEL,
    PEDALS,
    STEER,
    CONTROL,
]


UNITS = {
    GYRO: {"ang_rate_x": "g", "ang_rate_y": "g", "ang_rate_z": "g"},
    ACCEL: {"accel_x": "g", "accel_y": "g", "accel_z": "g"},
    PEDALS: {"apps": "%", "bse_front": "bar", "bse_rear": "bar"},
    STEER: {"angle": "degrees"},
    CONTROL: {""}
}