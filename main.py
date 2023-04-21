import glob
import os
from typing import List
import argparse
import sentencepiece as tokenizer

__author__ = "Aubertin Emmanuel"
__copyright__ = "2021, CERI"
__credits__ = ["Aubertin Emmanuel"]
__license__ = "GPL"
__version__ = "1.0.0"

parser = argparse.ArgumentParser(description="""
        Check and return CPU usage per connected user.
        """,
        usage="""
            main.py -auth 'auth0'
        """,
        epilog="version {}, license {}, copyright {}, credits {}".format(__version__,__license__,__copyright__,__credits__))
parser.add_argument('-auth', '--auth', type=str, nargs='?', help='enable auth for api', default=False)

args = parser.parse_args()
model = None

if __name__ == "__main__":
    # Check if there is file with .model or .srl extension  in ./models/

    print("##### Checking for model #####")
    if not os.path.exists("./models/tokenizer.model"):
        print("There is no model in folder./models/\nPlease you have to train the model or download a model")
        print("😩 \033[1;31mNo model in folder ./models/\033[0m 😩")
        exit(1)
    print("🤗 \033[1;32mModel found\033[0m 🤗")

    # Loading the model
    print("##### Loading model #####")
    model = tokenizer.SentencePieceProcessor(model_file='models/tokenizer.model')
    print("🤭 \033[1;32mModel loaded\033[0m 🤭")

    # Checking for SSL mode
    print("##### Checking for SSL mode #####")
    if os.path.exists("./cert/key.pem") and os.path.exists("./cert/cert.pem"):
        print("✅ \033[1;32mSSL mode enabled\033[0m ✅")
        ssl = True
    else:
        print("❌ \033[1;31mSSL mode disabled\033[0m ❌\n👁️ \033[1;31mYou must use SSL you in production.\033[0m 👁️ \nMore info here: https://github.com/emmanuel-aubertin/SentencePieceMicroS")
        ssl = False

    # Strating the FastAPI
    print("##### Strating FastAPI #####")

    import uvicorn
    if args.auth:
        from api.api_auth import app, set_model
        set_model(model)
    else:
        from api.api import app
    if ssl:
        uvicorn.run(app, host="0.0.0.0", port=8000,
                    ssl_keyfile="./cert/key.pem", 
                    ssl_certfile="./cert/cert.pem")
    else:
        uvicorn.run(app, host="0.0.0.0", port=8000)









