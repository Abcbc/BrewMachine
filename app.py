from multiprocessing import Manager


def main():
    manager = Manager()
    data = manager.dict({"current_temp": 0.0,
                         "desired_temp": 0.0,
                         "max_temp": 60.0,
                         "pc_heat_level": 0.0,
                         "error": False})

if __name__ == "__main__":
    main()