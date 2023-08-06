import os
from view.view import UI
import configparser

CONFIG_F = "config.ini"
ui = UI


def initConfig():
    dbpath = ui.getUserInput(
        "Where do you want to store the data base ?", "./db/database.db"
    )

    if os.path.exists(dbpath):
        config = configparser.ConfigParser()
        config["CONFIG"] = {"db_path": dbpath}

        with open(CONFIG_F, "w") as configFile:
            config.write(configFile)

        return True
    else:
        ui.displayError(404, "Wrong input path")
        return False
