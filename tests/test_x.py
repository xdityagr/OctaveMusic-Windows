
import os 
from pathlib import Path
RESOURCES_FOLDER = Path("resources")
BACKGROUNDS_FOLDER = RESOURCES_FOLDER.joinpath("backgrounds")
bgs = os.listdir(RESOURCES_FOLDER.joinpath("backgrounds"))

inbuiltbackgrounds: list[tuple[str, Path]] = [{Path(bgname).stem: BACKGROUNDS_FOLDER.joinpath(Path(bgname))} for bgname in bgs]

print(inbuiltbackgrounds)