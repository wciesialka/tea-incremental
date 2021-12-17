import pickle
import argparse
import pathlib
import os
from tea_incremental.game.tea_game import TeaGame

SAVE_PATH = pathlib.Path(os.path.expanduser("~/Documents")) / "My Games" / "Tea Incremental" / "save.tea"

def parse_args():
    argparser = argparse.ArgumentParser("tea", description="Incremental game about tea!")
    argparser.add_argument("--load", "-l", type=argparse.FileType("rb"), help="Save file.")
    return argparser.parse_args()

def load_game(load):
    game = None
    if not load is None:
        try:
           game = pickle.load(load)
        except:
            print(f"Could not load file {load.name}!")
        finally:
            load.close()
    if game is None:
        if(SAVE_PATH.exists() and SAVE_PATH.is_file()):
            with open(SAVE_PATH,"rb") as f:
                game = pickle.load(f)
        else:
            game = TeaGame()
    return game

def save_game(game, save_to):
    '''Save game to file.'''
    path_parent = os.path.dirname(save_to)
    os.makedirs(path_parent, exist_ok=True)
    with open(save_to, "wb") as f:
        pickle.dump(game, f)

def main():
    args = parse_args()

    game = load_game(args.load)

    save_game(game, SAVE_PATH if args.load is None else args.load.name)


if __name__ == "__main__":
    main()