#!/usr/bin/env python
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from smarthub_extension.server import server

if __name__ == "__main__":
    server.run()