from python_graphql_client import GraphqlClient
import feedparser
import httpx
import json
import pathlib
import re
import os
import datetime

root = pathlib.Path(__file__).parent.resolve()


if __name__ == "__main__":
    readme = root / "README.md"

    rewritten = "demo hub status === "
    readme.open("w").write(rewritten)
