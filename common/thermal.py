from thermal_subscriber import ThermalCameraSubscriber

def main():
    thermal = ThermalCameraSubscriber(save=True)
    thermal.listen()

if __name__ == "__main__":
    main()