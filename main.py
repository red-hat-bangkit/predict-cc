import uvicorn

# ---------------
# Single app init
# ---------------
from predict.main import app
# ----------------
# Multi app init
# ----------------
# from fastapi import FastAPI
# app = FastAPI()
# app.mount("predict", predict_app)

def run(args):
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, headers=[("server", "bangkitws")])

if __name__ == "__main__":
    from settings.core import parser

    parser.set_defaults(func=run)

    args = parser.parse_args()
    args.func(args)