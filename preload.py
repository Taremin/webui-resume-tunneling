import os
from modules import paths

def preload(parser):
    parser.add_argument("--share-token-path", type=str, help="Save share token for resume", default=None)

